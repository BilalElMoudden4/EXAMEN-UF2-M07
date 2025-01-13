from typing import Optional
from pydantic import BaseModel

#Ejercicio 1 -----------------------------------------

class ItemBase(BaseModel):
    nombre: str
    apellido: str
    email: str #Campo Sensible (ejercicio3)
    descripcion: Optional[str]
    curso: int  
    año: int
    direccion: str #Campo Sensible (ejercicio3)
    cp: Optional[str]
    contraseña: str #Campo Sensible (ejercicio3)
    
#----------------------------------------------------

#Ejercicio 2
class ItemCreate(ItemBase):
    pass  

class Item(ItemBase):
    id: int 