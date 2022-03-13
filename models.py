from sqlalchemy import Column, Integer, String
from database import Base


class Parameters(Base):
    __tablename__ = 'parameters'
    parameter_id = Column(Integer, primary_key=True, index=True)
    parameter_name = Column(String, unique=True, index=True)





