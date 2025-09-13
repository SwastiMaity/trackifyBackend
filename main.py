from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from fastapi import HTTPException
from pydantic import BaseModel
from models import SOSAlert
from typing import List

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Default root endpoint
@app.get("/")
def root():
    return {"status": "ok"}

# /api endpoint
@app.get("/api")
def api_status():
    return {"status": "ok"}

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

class SOSAlertRead(SOSAlertCreate):
    id: int

class SOSAlertUpdate(BaseModel):
    lat: float = None
    lon: float = None
    timestamp: str = None

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/sos", response_model=SOSAlertRead)
def create_sos_alert(alert: SOSAlertCreate, db: Session = Depends(get_db)):
    db_alert = SOSAlert(lat=alert.lat, lon=alert.lon, timestamp=alert.timestamp)
    db.add(db_alert)
    db.commit()
    db.refresh(db_alert)
    return db_alert

@app.get("/alerts", response_model=List[SOSAlertRead])
def get_alerts(db: Session = Depends(get_db)):
    alerts = db.query(SOSAlert).all()
    return alerts

@app.get("/alerts/{alert_id}", response_model=SOSAlertRead)
def get_alert_by_id(alert_id: int, db: Session = Depends(get_db)):
    alert = db.query(SOSAlert).filter(SOSAlert.id == alert_id).first()
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")
    return alert

@app.put("/alerts/{alert_id}", response_model=SOSAlertRead)
def update_alert(alert_id: int, alert_update: SOSAlertUpdate, db: Session = Depends(get_db)):
    alert = db.query(SOSAlert).filter(SOSAlert.id == alert_id).first()
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")
    if alert_update.lat is not None:
        alert.lat = alert_update.lat
    if alert_update.lon is not None:
        alert.lon = alert_update.lon
    if alert_update.timestamp is not None:
        alert.timestamp = alert_update.timestamp
    db.commit()
    db.refresh(alert)
    return alert

@app.delete("/alerts/{alert_id}")
def delete_alert(alert_id: int, db: Session = Depends(get_db)):
    alert = db.query(SOSAlert).filter(SOSAlert.id == alert_id).first()
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")
    db.delete(alert)
    db.commit()
    return {"message": "Alert deleted"}