"""Utility functions for the api module"""
from sqlmodel import Session
from src.backend.faceted_search.db.engine import engine


def get_db():
    with Session(engine) as session:
        return session
