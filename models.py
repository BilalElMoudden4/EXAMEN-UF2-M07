#Ejercicio 2
from sqlalchemy import Column, Integer, String
from database import Base

class Item(Base):
    __tablename__ = 'items'  

    id = Column(Integer, primary_key=True)  
    nombre = Column(String) 
    apellido = Column(String)
    email = Column(String)
    descripcion = Column(String)  
    curso = Column(Integer)
    año = Column(Integer)
    direccion = Column(String) 
    cp = Column(String)
    contraseña = Column(String)  
    
    
    
