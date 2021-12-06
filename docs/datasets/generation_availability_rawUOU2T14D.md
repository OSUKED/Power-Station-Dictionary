---
hide:
  - toc
---

# Insights.Api



<br>
**Additional Metadata**

| Attribute   |   Value(s) |
|:------------|-----------:|
| version     |          1 |

<br>
<br>

### Endpoints


Endpoint URL: [https://data.elexon.co.uk/bmrs/api/v1/generation/availability/rawUOU2T14D](https://data.elexon.co.uk/bmrs/api/v1/generation/availability/rawUOU2T14D)

Keywords: Availability



<br>
**Request Parameters**

| Parameters          | Type          | Nullable   | In    | Format    | Description          |
|:--------------------|:--------------|:-----------|:------|:----------|:---------------------|
| FuelType            | array, string | True       | query | -         | -                    |
| PublishDate         | string        | True       | query | date-time | -                    |
| PublishDateTimeFrom | string        | True       | query | date-time | -                    |
| PublishDateTimeTo   | string        | True       | query | date-time | -                    |
| NgcBmUnit           | array, string | True       | query | -         | -                    |
| OrderBy             | string        | True       | query | -         | -                    |
| PageNumber          | integer       | -          | query | int32     | -                    |
| PageSize            | integer       | -          | query | int32     | -                    |
| format              | -             | -          | query | -         | Response data format |

<br>

**Response Fields**

| Field                | Type    | Nullable   | Format    |
|:---------------------|:--------|:-----------|:----------|
| dataset              | string  | True       | -         |
| fuelType             | string  | True       | -         |
| ngcBmUnit            | string  | True       | -         |
| publishTime          | string  | True       | date-time |
| systemZone           | string  | True       | -         |
| forecastDate         | string  | -          | date-time |
| forecastDateTimezone | string  | True       | -         |
| outputUsable         | integer | True       | int64     |

<br>
