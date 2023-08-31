import reflex as rx
import sqlmodel
from typing import Optional

class MLModel(rx.Model, table=True):
    __tablename__ = 'mlmodels'
    id: int = sqlmodel.Field(default=None, primary_key=True)
    modelname:str
    project:int = sqlmodel.Field(foreign_key="Projects.id")
    owner:int = sqlmodel.Field(foreign_key="Users.id")
    traindataset:str # link to other database
    evaldataset:str # link to other database
    validationdataset:str # link to other database
    hyperparameter:str
    performance:str # link to other database
    opa_policy:Optional[str] = "mlModels.rego"
    created_at: sqlmodel.DateTime = sqlmodel.Field(default=None)
    updated_at: sqlmodel.DateTime = sqlmodel.Field(default=None)


class Snapshot(rx.Model, table=True):
    id: int = sqlmodel.Field(default=None, primary_key=True)
    snapshotname:str
    modelname:str  # link to other database
    iteration:int
    loss:float
    date:str