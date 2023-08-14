from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime


Base = declarative_base()


class ReportsBase(Base):
    __tablename__ = "reports"
    code = Column(String, primary_key=True)
    title = Column(String)
    segments = Column(Integer)
    guild_id = Column(Integer)
    start = Column(DateTime)
    end = Column(DateTime)
    duration = Column(DateTime)
