from sqlalchemy import Column, Integer, String
from database import Base

class Gesture(Base):
    __tablename__ = "gestures"
    id = Column(Integer, primary_key = True, index = True)
    gesture_type = Column(String, index=True)
    # timestamp = Column(DateTime, default=datetime.datetime.utcnow)

