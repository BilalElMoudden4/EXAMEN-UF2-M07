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

#Ejercicio 4
@app.get("/recibirUsuario/", response_model=list[schemas.Item])
def recibir_usuario(limit: int = 10, db: Session = Depends(get_db)):
    return functs.recibirUsuario(db, limit=limit)