from fastapi import FastAPI, HTTPException, Path
import uvicorn
from demo.schemas import EmployeeClass
from typing import List



employees_db: List[EmployeeClass] = []


app = FastAPI(
    title="Employee API",
    version="1.0.0"
)


#CREATE-
@app.post("/employees")
def add_employee(new_employee: EmployeeClass):

    for employee in employees_db:
        if employee.id == new_employee.id:
            raise HTTPException(status_code=409, detail="Employee Id alreday exists!") 

    employees_db.append(new_employee)      

    return {'message': 'Successfully added to database!'}




#READ- fetch all employees
@app.get("/employees", response_model= List[EmployeeClass])
def fetch_all_employees():

    return employees_db



#READ- fetch specific employee
@app.get("/employee/{emp_id}", response_model= EmployeeClass)
def fetch_employee(emp_id: int = Path(..., description="Id of the employee", examples="1")):

    for employee in employees_db:
        if employee.id == emp_id:
            
            return employee

    raise HTTPException(status_code=404, detail="Employee id do not exist!")


#UPDATE - specific employee
@app.put("/employee/{emp_id}")
def update_employee(emp_id: int, updated_employee: EmployeeClass):

    for index, employee in enumerate(employees_db):
        if employee.id == emp_id:
            employees_db[index] = updated_employee

            return {'message': 'successfully updated'}
    
    raise HTTPException(status_code=404, detail="Employee id do not exist!")
            


#DELETE- employee
@app.delete("/employee/{emp_id}")
def delete_employee(emp_id: int = Path(..., description="Enter the id of the employee to delete the data", examples="1")):

    for index, employee in enumerate(employees_db):
        if employee.id == emp_id:
            del employees_db[index] 

            return {'message': 'Successfully deleted from the database!'}
    
    raise HTTPException(status_code=404, detail="Employee id do not exist")





if __name__ == "__main__":
    uvicorn.run(
        app= "main:app",
        host= "127.0.0.1",
        port= 8000,
        reload= True,
        log_level= "info"
    )



