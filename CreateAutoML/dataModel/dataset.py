import reflex as rx
import sqlmodel

class Dataset(rx.Model, table=True):
    __tablename__ = 'datasets'
    id: int = sqlmodel.Field(default=None, primary_key=True)
    datasetname: str
    datasetlocation:str # maybe multiple location indicates multiple dataset is combined (use datumaro)
    project:int = sqlmodel.Field(foreign_key="projects.id")

    def combine(self):
        return