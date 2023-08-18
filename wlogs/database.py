import json
from pathlib import Path
from sqlalchemy import URL, create_engine, Column, Integer, String, TIMESTAMP, Float
from sqlalchemy.orm import declarative_base, sessionmaker

from .storage import ROOT_DIRECTORY


POSTGRESQL_CREDENTIALS_PATH = ROOT_DIRECTORY / "postgresql_credentials.json"
WOW_SCHEMA = "wow"
Base = declarative_base()


def url_db_from_json(path: Path = POSTGRESQL_CREDENTIALS_PATH, drivername="postgresql") -> URL:
    with open(path, 'r') as f:
        return URL.create(drivername, **json.load(f))


engine = create_engine(url_db_from_json())


class Session:
    def __init__(self):
        self._session = sessionmaker(bind=engine)()

    def __enter__(self):
        self._session.connection(execution_options={"schema_translate_map": {None: WOW_SCHEMA}})
        return self._session.__enter__()

    def __exit__(self, *args, **kwargs):
        return self._session.__exit__(*args, **kwargs)


class ReportsBase(Base):
    __tablename__ = "reports"
    code = Column(String(16), primary_key=True, nullable=False)
    title = Column(String)
    segments = Column(Integer)
    guild_id = Column(Integer)
    start_time = Column(TIMESTAMP)
    end_time = Column(TIMESTAMP)
    duration = Column(Float)
