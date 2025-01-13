from sqlalchemy import Column, Integer, String
from database import BaseModel

#Ejercicio 1 -----------------------------------------
class Formulari(BaseModel):
    
    __tablename__ = 'items'  

    id = Column(Integer, primary_key=True)  
    nombre = Column(String) 
    apellido = Column(String)
    email = Column(String)
    description = Column(String)  
    curso = Column(Integer)
    año = Column(String)  
    direccion = Column(String)
    cp = Column(Integer)
    contrasena = Column(String)
#----------------------------------------------------


