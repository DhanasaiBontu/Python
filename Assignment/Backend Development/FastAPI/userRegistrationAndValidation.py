from fastapi import FastAPI,HTTPException
from typing import Optional
from pydantic import BaseModel,field_validator
import re

app=FastAPI()

class User(BaseModel):
    username:str
    email:str
    password:str
    age:int

    @field_validator("password")
    @classmethod
    def passwd_validate(cls,value):
        if(len(value)<8):
            raise ValueError("Password length should be at least 8 characters")
        return value
    
    @field_validator("age")
    @classmethod
    def age_validate(cls,value):
        if(value<18):
            raise ValueError("Age must be 18 or more")
        return value
    
    @field_validator("email")
    @classmethod
    def email_validate(cls,value):
        pattern=r'^[A-Za-z0-9_]+@[a-z]+\.[a-z]+$'
        if(re.match(pattern,value) is None):
            raise ValueError("Email is invalid")
        return value
    
@app.post("/register")
def registerUser(user:User):
    return user