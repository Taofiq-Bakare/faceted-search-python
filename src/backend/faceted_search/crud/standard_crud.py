"""The basic crud functions for the standards"""

from fastapi import HTTPException, status
from sqlmodel import Session, select
from src.backend.faceted_search.models.standard import Standard, StandardCreate


def create_new_standard(standard: StandardCreate, db: Session):
    statement = select(Standard).where(Standard.catalog_id == standard.catalog_id)
    # with db as db:
    db_data = db.exec(statement=statement).first()
    if db_data:
        raise HTTPException(
            status_code=status.HTTP_208_ALREADY_REPORTED,
            detail=f"The standard with the catalog id={standard.catalog_id} already exists.",
        )
    new_standard = Standard(
        catalog_id=standard.catalog_id,
        catalog_name=standard.catalog_name,
        topic=standard.topic,
        sub_topic=standard.sub_topic,
    )
    db.add(new_standard)
    db.commit()
    db.refresh(new_standard)
    return new_standard
