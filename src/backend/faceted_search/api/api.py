"""The main api file"""

from fastapi import APIRouter
from src.backend.faceted_search.api.api_v1.endpoints import standard_endpoints

api_router = APIRouter()


api_router.include_router(router=standard_endpoints.router, prefix="/standard")
