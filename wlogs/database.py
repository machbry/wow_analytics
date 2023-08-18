import json
from sqlalchemy import URL, create_engine, Column, Integer, String, TIMESTAMP, Float
from sqlalchemy.orm import declarative_base, sessionmaker

from .storage import ROOT_DIRECTORY


with open(ROOT_DIRECTORY / "postgresql_credentials.json", 'r') as f:
    url_db = URL.create(drivername="postgresql", **json.load(f))
    engine = create_engine(url_db)


class Session:
    def __init__(self):
        self._session = sessionmaker(bind=engine)()
        self._schema = "wow"

    def __enter__(self):
        self._session.connection(execution_options={"schema_translate_map": {None: self._schema}})
        return self._session.__enter__()

    def __exit__(self, *args, **kwargs):
        return self._session.__exit__(*args, **kwargs)


Base = declarative_base()


class ReportsBase(Base):
    __tablename__ = "reports"
    code = Column(String(16), primary_key=True, nullable=False)
    title = Column(String)
    segments = Column(Integer)
    guild_id = Column(Integer)
    start_time = Column(TIMESTAMP)
    end_time = Column(TIMESTAMP)
    duration = Column(Float)
