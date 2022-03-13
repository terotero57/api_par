from typing import List
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Read
@app.get("/parameters", response_model=List[schemas.Parameters])
async def read_parameters(skip: int = 0, limit: int = 100, db:Session = Depends(get_db)):
    parameters = crud.get_parameters(db, skip=skip, limit=limit)
    return parameters


# Create
@app.post("/parameters", response_model=schemas.Parameters)
async def create_parameters(parameter: schemas.ParametersCreate, db: Session = Depends(get_db)):
    return crud.create_parameters(db=db, parameter=parameter)


# delete
@app.post("/parameters_delete", response_model=schemas.ParametersCreate)
async def delete_parameters(parameter: schemas.ParametersCreate, db: Session = Depends(get_db)):
    return crud.delete_parameters(db=db, parameter=parameter)