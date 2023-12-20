"""The CRUD endpoints for standards"""

from fastapi import APIRouter, status
from src.backend.faceted_search.api.utils_api import get_db
from src.backend.faceted_search.crud.standard_crud import create_new_standard

from src.backend.faceted_search.models.standard import StandardCreate, StandardReturn

router = APIRouter()


@router.post("/standard", response_model=StandardReturn, status_code=status.HTTP_200_OK)
def create_standard(new_standard: StandardCreate):
    response_data = create_new_standard(standard=new_standard, db=get_db())
    return response_data
