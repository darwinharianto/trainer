import reflex as rx
from ..dataModel.project import Project
from ..dataModel.user import User
from .appState import State

class ProjectState(State):
    
    projects: list[str] = [f"PROJECTS {i}" for i in range(5)]
    projects2: list[Project]
    show_project_form: bool = False

    def get_projects(self):
        # TODO start query on db to get available projects
        with rx.session() as session:
            self.projects2 = (
                session.query(Project)
                .all()
            )

    def toggle_show_project_form(self):
        self.show_project_form = not (self.show_project_form)
    
    def add_project(self):
        self.toggle_show_project_form()
        print("create new project")
        print(self.username)
        with rx.session() as session:
            alluser = (
                session.query(User)
                
                .all()
            )
            print(alluser)
            user = (
                session.query(User)
                .filter(User.username == self.username)
                .all()
            )
            print(user)
        #     session.add(
        #         Project(
        #         name=projectName,
        #         user=self.usernam,
        #         projectMetadata=metadata,
        #         )
        #     )
        #     session.commit()
    
    def delete_projects(self, project:Project):
        with rx.session() as session:
            session.delete(
                project
            )
            session.commit()
    

        