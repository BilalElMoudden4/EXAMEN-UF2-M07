from typing import Optional
from pydantic import BaseModel

#Ejercicio 1 -----------------------------------------

class ItemBase(BaseModel):
    nombre: str
    apellido: str
    email: str
    descripcion: Optional[str]
    curso: int  
    año: int
    direccion: str
    cp: Optional[str]
    contraseña: str
    
#----------------------------------------------------

#Ejercicio 2
class ItemCreate(ItemBase):
    pass  

class Item(ItemBase):
    id: int 