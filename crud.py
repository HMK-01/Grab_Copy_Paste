from app.models import Gesture
from sqlalchemy.orm import Session
from schemas import GestureCreate

def create_gesture (db:Session, gesture: GestureCreate):
    new_gesture = Gesture(gesture_type= gesture.gesture_type)
    db.add(new_gesture)
    db.commit()
    db.refresh(new_gesture)
    return new_gesture
