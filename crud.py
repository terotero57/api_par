from sqlalchemy.orm import Session
import models, schemas


# Parameters一覧
def get_parameters(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Parameters).offset(skip).limit(limit).all()


# Parameter登録
def create_parameters(db: Session, parameter: schemas.Parameters):
    db_parameter = models.Parameters(parameter_name=parameter.parameter_name)
    db.add(db_parameter)
    db.commit()
    db.refresh(db_parameter)
    return db_parameter


# Parameter削除
def delete_parameters(db: Session, parameter: schemas.Parameters):
    delete = db.query(models.Parameters).filter(models.Parameters.parameter_name == parameter.parameter_name).one()
    db.delete(delete)
    db.commit()
    return {"parameter_name": parameter.parameter_name}

