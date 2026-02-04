from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from . import utils
from pydantic.types import conint


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    
class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        from_attributes = True  

class Post(PostBase):
    id: int
    title: str
    owner_id: int
    owner: UserOut
    
    class Config:
        from_attributes = True  # Changed from orm_mode = True
        
class PostOut(BaseModel):
    Post: Post  # Aapka purana Post schema
    votes: int

    class Config:
        from_attributes = True # Agar Pydantic v2 hai, v1 ke liye orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    
    class Config:
        from_attributes = True # Changed from orm_mode = True
 
        
class UserLogin(BaseModel):
    email: str
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    id: Optional[str] = None
    
class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
    
    
    