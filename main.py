from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import SessionLocal, Base, engine
from schemas import GestureCreate
import crud
from app.models import Gesture

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,             # list of allowed frontend origins
    allow_credentials=True,
    allow_methods=["*"],               # allow all HTTP methods
    allow_headers=["*"],               # allow all headers
)

@app.get('/')
def read_root():
    return {"message" : "Welcome to Pinch Motion backend"}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/gesture")
def add_gesture(gesture: GestureCreate, db: Session = Depends(get_db)):
    return crud.create_gesture(db=db, gesture=gesture)

@app.get("/gestures")
def get_all_gestures(db: Session = Depends(get_db)):
    return db.query(Gesture).all()