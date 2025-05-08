from sqlalchemy import Column, Integer, String
from database import Base

class Job(Base):
    __tablename__ = "job"

    id = Column(Integer, primary_key=True, index=True)
    verarbeitet = Column(Integer, nullable=False)
    gesamt = Column(Integer, nullable=False)
    job_status = Column(String, nullable=False)
    response_file = Column(String, nullable=True)
    result_path = Column(String, nullable=True)
