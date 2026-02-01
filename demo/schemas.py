from pydantic import BaseModel, Field, StrictInt
from typing import Optional



class EmployeeClass(BaseModel):
    id: StrictInt = Field(..., gt= 0, description="Id of the Employee that is unique", examples=[1, 2])
    
    name: str = Field(..., min_length=3, max_length=30)
    
    department:str = Field(..., min_length= 3, max_length= 30)
    
    age: StrictInt = Field(..., gt=18, le= 80, description="Age of the employee")

    gender: Optional[str] = Field(default= None, description="Gender of the employee")