from sqlalchemy import Column, Integer, Float, String
from database import Base

class SOSAlert(Base):
    __tablename__ = "sos_alerts"

    id = Column(Integer, primary_key=True, index=True)
    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)
    timestamp = Column(String, nullable=False)
    status = Column(String, nullable=False, default="active")
    