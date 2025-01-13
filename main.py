#Ejercicio 2

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import functs
import schemas

app = FastAPI()

def get_db():
    db = SessionLocal() 
    try:
        yield db  
    finally:
        db.close()  
        
@app.post("/añadirUsuario/", response_model=schemas.Item)
def add_user(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return functs.add_user(db, item)
#----------------------------------------------------------