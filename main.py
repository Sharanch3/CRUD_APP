import models, schemas, crud
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
from typing import List
import uvicorn


Base.metadata.create_all(bind = engine)

app = FastAPI(
    description="CRUD API for the employee management",
    version= "1.0.0"
)


#dependency with the DB
def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()



@app.post("/employees", response_model= schemas.EmployeeOut)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, employee)



@app.get("/employees", response_model= List[schemas.EmployeeOut])
def fetch_employees(db: Session = Depends(get_db)):
    
    return crud.fetch_employees(db)




@app.get("/employees/{emp_id}", response_model= schemas.EmployeeOut)
def fetch_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = crud.fetch_employee(db, emp_id)

    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    return employee



@app.put("/employees/{emp_id}", response_model= schemas.EmployeeOut)
def update_employee(emp_id: int, employee: schemas.EmployeeUpdate, db: Session = Depends(get_db)):

    db_employee = crud.update_employee(db, emp_id, employee)

    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    return db_employee



@app.delete("/employees/{emp_id}", response_model= schemas.EmployeeOut)
def delete_employee(emp_id: int, db: Session = Depends(get_db)):

    employee = crud.delete_employee(db, emp_id)

    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    return employee



if __name__ == "__main__":

    uvicorn.run(
        app= "main:app",
        host="127.0.0.1",
        port= 8000,
        reload= True,
        log_level= "info"
    )
