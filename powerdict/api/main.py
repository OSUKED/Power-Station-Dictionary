import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from powerdict.api import frictionless, authentication, assets, website


# Inputs
load_dotenv()
middleware_secret_key = os.environ["MIDDLEWARE_SECRET_KEY"]
environment = os.environ["ENVIRONMENT"]
static_dir = os.environ["STATIC_DIR"]
root_url = os.environ["ROOT_URL"]

# Initialisation
app = FastAPI(
    title="Asset Dictionary",
    description=f'Welcome to the Asset Dictionary API.\n\nThe main website can be found [here]({root_url})',
    version="0.1.0"
)

app.mount("/static", StaticFiles(directory=static_dir), name="static")
app.add_middleware(SessionMiddleware, secret_key=middleware_secret_key)

app.include_router(assets.router, prefix="/dictionary")
app.include_router(frictionless.router, prefix="/frictionless")
app.include_router(authentication.router, prefix="/authentication")
app.include_router(website.router)
