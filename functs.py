from sqlalchemy.orm import Session
from schemas import Item
from schemas import ItemBase

#Ejercicio 2 -----------------------------------------
def add_user(db: Session, item: ItemBase):
    db_item = Item(**item.dict()) 
    db.add(db_item)  
    db.commit()
    db.refresh(db_item) 
    return db_item