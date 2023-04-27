import json
import pytz
import aiohttp
import asyncio
import requests
import threading
import datetime
import pandas as pd
from typing import Optional
from functools import lru_cache
from pydantic import parse_obj_as

from powerdict import schemas, db


def format_input_date(input_date: datetime.datetime) -> datetime.datetime:
    if isinstance(input_date, datetime.datetime):
        pass
    elif isinstance(input_date, datetime.date):
        input_date = datetime.datetime.combine(input_date, datetime.datetime.min.time())
    elif isinstance(input_date, pd.Timestamp):
        input_date = input_date.to_pydatetime()
    elif isinstance(input_date, str):
        input_date = pd.to_datetime(input_date).to_pydatetime()
    else:
        raise ValueError('`input_date` must be a datetime.datetime, datetime.date, pd.Timestamp or str')

    return input_date.astimezone(pytz.UTC)
    
def add_sps_to_settlement_calendar_df(df: pd.DataFrame) -> pd.DataFrame:
    """Mapping from Europe/London local datetime to settlement period (SP)
    * if we have gone from GMT to BST and it's a short day then 46 SPs
    * if we have gone from BST to GMT and it's a long day then 50 SPs
    * if we are in GMT or BST and it's a normal day then 48 SPs
    """
    # vectorised sp assignment with mistakes on GMT <-> BST switch dates
    s_switch_diff = df['is_dst'].astype(float).diff()
    s_sp = (df['datetime_local'].dt.hour + df['datetime_local'].dt.minute / 60).multiply(2).add(1).astype(int)

    # correcting mistakes on GMT <-> BST switch dates
    for switch_date in s_switch_diff[s_switch_diff.fillna(0)!=0].index.date:
        switch_date_idxs = df['datetime_local'].dt.date == switch_date

        s_gmt_to_bst_date_sps = s_sp.loc[switch_date_idxs]
        s_gmt_to_bst_date_sps.loc[:] = 1
        s_sp.loc[switch_date_idxs] = s_gmt_to_bst_date_sps.cumsum()

    return df.assign(sp=s_sp)

def get_settlement_calendar_df(
    start_date: datetime.datetime, 
    end_date: datetime.datetime
) -> pd.DataFrame:
    """Constructs a dataframe of datetimes and settlement periods (SPs) for a given date range

    N.b. If no timezone is specified then UTC is assumed

    Similar work:
    * https://github.com/iagw/masterdatetime/blob/57705739fdc6c1b56dcda10b1e8fb44682b661b4/masterdatetime_iso8601.py

    Args:
        start_date (datetime.datetime): Start of the settlement calendar date range
        end_date (datetime.datetime): End of the settlement calendar date range

    Returns:
        pd.DataFrame: The `df_settlement_calendar` object
    """
    start_date, end_date = format_input_date(start_date), format_input_date(end_date)
    rng_start_date, rng_end_date = start_date - pd.Timedelta(days=1), end_date + pd.Timedelta(days=1)

    dt_rng = pd.date_range(rng_start_date, rng_end_date, freq='30T')

    df_settlement_calendar = (
        pd.Series(
            dt_rng, 
            index=pd.Index(dt_rng, name='datetime_utc')
        )
        .dt.tz_convert('Europe/London')
        .apply(lambda dt: bool(dt.dst()))
        .to_frame(name='is_dst')
        .pipe(lambda df: df.assign(datetime_local=df.index.tz_convert('Europe/London')))
        .pipe(add_sps_to_settlement_calendar_df)
        .loc[start_date:end_date]
    )

    return df_settlement_calendar

def extend_settlement_calendar_df(
        start_date: datetime.datetime,
        end_date: datetime.datetime,
        df_settlement_calendar: pd.DataFrame
    ) -> tuple[pd.DataFrame, bool]:
    # identifying current and new date ranges
    current_settlement_calendar_start_date = df_settlement_calendar.index[0]
    current_settlement_calendar_end_date = df_settlement_calendar.index[-1]

    new_settlement_calendar_start_date = min(current_settlement_calendar_start_date, start_date)
    new_settlement_calendar_end_date = max(current_settlement_calendar_end_date, end_date)

    # extending date range if required
    dt_rng_extended = (
        (new_settlement_calendar_start_date < current_settlement_calendar_start_date) |
        (new_settlement_calendar_end_date > current_settlement_calendar_end_date)
    )

    if dt_rng_extended:
        # TODO create only the missing section of the calendar rather than everything
        return get_settlement_calendar_df(new_settlement_calendar_start_date, new_settlement_calendar_end_date)

    return df_settlement_calendar, dt_rng_extended


class RunThread(threading.Thread):
    def __init__(self, func, args, kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.result = None
        super().__init__()

    def run(self):
        self.result = asyncio.run(self.func(*self.args, **self.kwargs))

def run_async_func(func, *args, **kwargs):
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = None
    if loop and loop.is_running():
        thread = RunThread(func, args, kwargs)
        thread.start()
        thread.join()
        return thread.result
    else:
        return asyncio.run(func(*args, **kwargs))


class BmrsCrawler:
    _df_settlement_calendar: pd.DataFrame = None

    def __init__(
        self,
        run_async: bool = False,
        settlement_calendar_start_date: datetime.datetime = datetime.datetime(2010, 1, 1),
        settlement_calendar_end_date: datetime.datetime = datetime.datetime(2025, 1, 1)
    ):
        self.run_async = run_async
        _ = self.get_settlement_calendar_df(settlement_calendar_start_date, settlement_calendar_end_date)

    @lru_cache
    def get_settlement_calendar_df(
        self,
        start_date: datetime.datetime = datetime.datetime(2010, 1, 1),
        end_date: datetime.datetime = datetime.datetime(2025, 1, 1)
    ):
        start_date = format_input_date(start_date)
        end_date = format_input_date(end_date)

        # checking if the calendar exists
        calendar_doesnt_exist = False

        if hasattr(self, 'df_settlement_calendar'):
            if self.df_settlement_calendar is None:
                calendar_doesnt_exist = True
        else:
            calendar_doesnt_exist = True

        if calendar_doesnt_exist:
            self.df_settlement_calendar = get_settlement_calendar_df(start_date, end_date)
            return self._df_settlement_calendar

        # extending the calendar if necessary
        df_settlement_calendar, dt_rng_extended = extend_settlement_calendar_df(start_date, end_date, self.df_settlement_calendar)

        if dt_rng_extended:
            self.df_settlement_calendar = df_settlement_calendar

        return self.df_settlement_calendar.loc[start_date:end_date]

    def get_ts_request_inputs(
        self,
        start_date: datetime.datetime,
        end_date: datetime.datetime,
        non_ts_kwargs: dict,
        settlement_date_col: str = 'settlementDate',
        settlement_period_col: str = 'settlementPeriod'
    ):
        df_settlement_calendar = self.get_settlement_calendar_df(start_date, end_date)

        request_inputs = [{settlement_date_col: dt.date(), settlement_period_col: sp} for dt, sp in df_settlement_calendar.set_index('datetime_local')['sp'].items()]
        [request_input.update(non_ts_kwargs) for request_input in request_inputs]

        return request_inputs

    async def async_request(
        self,
        url = 'https://data.elexon.co.uk/bmrs/api/v1/balancing/physical/all',
        params: Optional[dict] = None
    ) -> dict:
        if params is None:
            params = {}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as r:
                r.raise_for_status()
                return await r.json()
            
    def get_async_requests(
        self,
        params_sets: Optional[list[dict]] = None,
        url = 'https://data.elexon.co.uk/bmrs/api/v1/balancing/physical/all'
    ):
        if params_sets is None:
            params_sets = []

        async def gather_async_request(params_sets):
            tasks = [self.async_request(url, params) for params in params_sets]
            return await asyncio.gather(*tasks)

        return run_async_func(gather_async_request, params_sets)
            
    def get_sync_requests(
        self,
        params_sets: Optional[list[dict]] = None,
        url = 'https://data.elexon.co.uk/bmrs/api/v1/balancing/physical/all'
    ):
        if params_sets is None:
            r = requests.get(url)
            r.raise_for_status()
            return r.json()

        results = []

        for params_set in params_sets:
            r = requests.get(url, params=params_set)
            r.raise_for_status()
            results += [r.json()]

        return results
    
    def get_requests(
        self,   
        params_sets: Optional[list[dict]] = None,
        run_async: bool | None = None
    ):
        if run_async is None:
            run_async = self.run_async

        if run_async:
            return self.get_async_requests(params_sets)
        else:
            return self.get_sync_requests(params_sets)
            
    def get_physical_ts_batch(
        self,
        dataset: schemas.BmrsPhysicalType,
        start_date: datetime.datetime,
        end_date: datetime.datetime,
        bmUnit: str | None = None,
        format: schemas.BmrsResponseFormat = schemas.BmrsResponseFormat.json,
        run_async: bool | None = None
    ) -> schemas.BmrsPhysicalResponse:
        # preparing request inputs
        non_ts_kwargs = {
            'dataset': dataset,
            'bmUnit': bmUnit,
            'format': format
        }

        params_sets = self.get_ts_request_inputs(start_date, end_date, non_ts_kwargs)
        
        params_sets = [
            json.loads(params.json(exclude_none=True))
            for params
            in parse_obj_as(list[schemas.BmrsPhysicalRequest], params_sets)
        ]

        # running requests and extracting results data
        results = self.get_requests(params_sets, run_async)

        data = []

        for result in results:
            data += result['data']

        return data


if __name__ == "__main__":
    import time

    start_date = datetime.datetime(2023, 1, 1)
    end_date = datetime.datetime(2023, 1, 1, 0, 30)

    bmrs_crawler = BmrsCrawler()

    query_start_time = time.perf_counter()
    physical_ts_batch = bmrs_crawler.get_physical_ts_batch('PN', start_date, end_date)
    query_end_time = time.perf_counter()

    print(f'Time: {query_end_time - query_start_time} (s)')
    print(len(physical_ts_batch))
