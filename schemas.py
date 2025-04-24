from pydantic import BaseModel

class GestureCreate(BaseModel):
    gesture_type: str
    