from pydantic import BaseModel, Field


class ParametersCreate(BaseModel):
    parameter_name: str = Field(max_length=12)


class Parameters(ParametersCreate):
    parameter_id: int

    class Config:
        orm_mode = True




