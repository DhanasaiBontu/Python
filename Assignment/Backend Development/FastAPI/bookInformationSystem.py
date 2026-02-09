from fastapi import FastAPI
from pydantic import BaseModel,Field
app=FastAPI()

book_db=[]
class Book(BaseModel):
    title:str
    author:str
    year:int
    isbn:str

@app.post("/books/")
def add_book(book: Book):
    book_db.append(book)
    return book

@app.get("/books/")
def get_books():
    return book_db