from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    id: int
    email: str
    hashed_password: str
    is_active: bool
    auth_provider: str

class UserCreate(UserBase):
    is_active: bool = True
    auth_provider: str = "email"

class UserUpdate(UserBase):
    email: str
    hashed_password: str
    is_active: bool


"""Notes Schema"""
class NoteBase(BaseModel):
    id: int
    title: str | None = None
    content: str | None = None
    label: str | None = None

class NoteCreate(NoteBase):
    pass
