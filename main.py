from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, sessionlocal
import model,schemas

model.Base.metadata.create_all(bind=engine)

app=FastAPI()

def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()
@app.get("/")
def root():
    return {"message":"FastAPI ,sqlalchemy is working"}
@app.get("/books")
def all_books(db: Session=Depends(get_db)):
    return db.query(model.book).all()

@app.get("/book/{book_id}")
def get_book(book_id:int ,db: Session=Depends(get_db) ):
    book=db.query(model.book).filter(model.book.id==book_id).first()
    if not book:
        return HTTPException(status_code=404,detail="This book is not present:( !")
    return book


@app.post("/book/{book_id}")
def post_book(book:schemas.add_book,db: Session=Depends(get_db)):
    new_book=model.book(name=book.name,author=book.author,rating=book.rating)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@app.put("/book/{book_id}")
def edit_book(book_id:int,book_up:schemas.update_book,db: Session=Depends(get_db)):
    book=db.query(model.book).filter(model.book.id==book_id).first()
    if not book:
        return HTTPException(status_code=404,detail="This book is not present:( !")
    if book_up.name is not None:
        book.name=book_up.name
    if book_up.author is not None:
        book.name=book_up.author   
    if book_up.rating is not None:
        book.rating=book_up.rating            
    db.commit()
    db.refresh(book)
    return book

#delete a book

@app.delete("/book/{book_id}")
def delete_book(book_id:int,db: Session=Depends(get_db)):
    book=db.query(model.book).filter(model.book.id==book_id).first()
    if not book:
        return HTTPException(status_code=404,detail="This book is not present:( !")
    db.delete(book)
    db.commit()
    
    return {"message":"Book has been deleted !","deleted book":book}