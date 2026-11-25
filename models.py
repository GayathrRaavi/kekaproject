
from pydantic import BaseModel, Field, model_validator
from datetime import date
from enum import Enum


class VehType(str, Enum):
    Car = "Car"
    Bike = "Bike"
    
class CarEntry(BaseModel):

    carreg: int = Field(gt=0)
    cartype: VehType

class CarExit(BaseModel):

    Ticketid: int = Field(gt=0)
    slot:int
    cartype: VehType
    status:str
    


