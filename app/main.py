from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exception_handlers import http_exception_handler
from app.routes import pm2_routes

app = FastAPI(title="PM2 Dashboard")
app.include_router(pm2_routes.router)