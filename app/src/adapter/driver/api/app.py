import os
from functools import lru_cache
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from src.adapter.driver.api.api_v1.api import router as api_router
from src.adapter.driver.api import config

load_dotenv()

root_path = os.getenv("ENV", default="")


@lru_cache()
def get_settings():
    return config.Settings()


app = FastAPI(
    title="FastAPI Clean Architecture",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    root_path=f"/{root_path}",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")
