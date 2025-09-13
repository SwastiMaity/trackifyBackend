from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from fastapi import HTTPException
from pydantic import BaseModel
from models import SOSAlert

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Enable CORS - allow all origins (modify for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB Session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class SOSAlertCreate(BaseModel):
    lat: float
    lon: float
    timestamp: str

@app.post("/sos")
def create_sos_alert(alert: SOSAlertCreate, db: Session = Depends(get_db)):
    db_alert = SOSAlert(lat=alert.lat, lon=alert.lon, timestamp=alert.timestamp)
    db.add(db_alert)
    db.commit()
    db.refresh(db_alert)
    return {"message": "SOS alert stored", "id": db_alert.id}