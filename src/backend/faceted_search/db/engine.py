"""sqlite engine"""


from sqlmodel import SQLModel, create_engine, Session


engine = create_engine("sqlite:///database.db", echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# local_session = Session(engine)
