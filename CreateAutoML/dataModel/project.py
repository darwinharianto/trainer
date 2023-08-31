import reflex as rx
import sqlmodel
from typing import Optional
from datetime import datetime

class Project(rx.Model, table=True):
    __tablename__ = 'projects'
    id: int = sqlmodel.Field(default=None, primary_key=True)
    name:str = sqlmodel.Column(str)
    owner:int = sqlmodel.Field(foreign_key="users.id")
    assignee:int = sqlmodel.Field(foreign_key="users.id")
    # organization:int = sqlmodel.Field(foreign_key="organizations.id")
    # user:int = sqlmodel.Field(foreign_key="users.id")
    projectMetadata:str = sqlmodel.Column(str, default=None)# maybe contain who and when user create
    opa_policy:Optional[str] = "mlProjects.rego"
    created_at = sqlmodel.Column(sqlmodel.TIMESTAMP, default=datetime.utcnow())
    updated_at = sqlmodel.Column(sqlmodel.TIMESTAMP, default=datetime.utcnow())

    def __init__(self, name, user, projectMetadata, opa_policy):
      self.name = name
      self.user = user
      self.projectMetadata = projectMetadata
      self.opa_policy = opa_policy

    def save(self):
      with rx.session() as session:
        session.add(self)
        session.commit()

    def delete(self):
      with rx.session() as session:
        session.delete(self)
        session.commit()

    def get(id):
      with rx.session() as session:
        return session.get(Project, id)

    def filter(filter_criteria):
      with rx.session() as session:
        return session.query(Project).filter(filter_criteria)

    def all():
      with rx.session() as session:
        return session.query(Project).all()

    def update(self, update_data):
      with rx.session() as session:
        session.update(self, update_data)
        session.commit()

    def to_dict(self):
      return {
        "id": self.id,
        "name": self.name,
        "user": self.user,
        "projectMetadata": self.projectMetadata,
        "opa_policy": self.opa_policy,
      }
    
class Project(rx.Model, table=True):
    __tablename__ = 'projects'
    id: int = sqlmodel.Field(default=None, primary_key=True)
    name:str
    user:int = sqlmodel.Field(foreign_key="users.id")
    projectMetadata:str # maybe contain who and when user create
    opa_policy:Optional[str] = "mlProjects.rego"


    # should this be a base implementation?
    def create_project(self, *args,**kwargs):
        print("called create_project")
        # with rx.session() as session:

        # raise NotImplementedError
        # with rx.session() as session:
        #     alluser = (
        #         session.query(User)
                
        #         .all()
        #     )
        #     print(alluser)
        #     user = (
        #         session.query(User)
        #         .filter(User.username == self.username)
        #         .all()
        #     )
        # return
    
    def read_project(self, *args,**kwargs):
        raise NotImplementedError
        return

    def delete_project(self, *args,**kwargs):
        raise NotImplementedError
        return
    
    def update_project(self, *args,**kwargs):
        raise NotImplementedError
        return