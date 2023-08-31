from .appState import State
import reflex as rx
import plotly.graph_objects as go
import plotly.express as px
from plotly.graph_objs import *
import pandas as pd
# maybe split this state into multiple smaller state?
# state for model params
# state for model name
# state for anything else?
class ModelsPageState(State):
    
    models: list[str] = [f"model_{i}" for i in range(3)]
    datasets: list[str] =  [f"dataset_{i}" for i in range(3)]

    show_model_button:bool = False
    show_dataset_button:bool = False
    

    # item to be set
    model:list[str] = []
    parameters:dict = {}
    training_dataset:list[str] = []
    evaluation_dataset:list[str] = []
    validation_dataset:list[str] = []

    def show_add_model(self):
        self.show_model_button = True
        return
    def hide_add_model(self):
        self.show_model_button = False
        return
    
    def show_add_dataset(self):
        self.show_dataset_button = True
        return
    def hide_add_dataset(self):
        self.show_dataset_button = False
        return
    

    def get_models_and_artifacts(self):
        # TODO start query on db? is it from database? sqlalchemy?
        #  to get model artifact on given projects

        # with rx.session() as session:
        #     self.projects = session.query()
        pass

    @rx.var
    def modelOptions(self) -> list[str]:
        # TODO go through library? or read from current selected model
        return ["FCRN", "MaskRCNN", "RNN"]
    
    @rx.var
    def parameterOptions(self) -> dict:
        # TODO go through parameters from model options? or from selected model?
        return {"lr":1, "checkpoint":2}

    @rx.var
    def targetModels(self) -> list[tuple[str,str]]:
        return [(item, f"{self.current_page}?project={self.projectName}&model={item}") for item in self.models]

    @rx.var
    def targetDatasets(self) -> list[tuple[str,str]]:
        # TODO what is datasets/item? CVAT?
        # maybe embed CVAT?
        return [(item, "datasets/"+item) for item in self.datasets]

    @rx.var
    def projectName(self):
        return self.get_query_params().get("project")
    
    @rx.var
    def modelName(self):
        return self.get_query_params().get("model")
    
    @rx.var
    def loss_plot(self) -> go.Figure:
        # load from database the plot
        # TODO how to make this transparent?
        loss: list[float] = [i/10 for i in range(10,0, -1)]
        iteration: list[int] = [i for i in range(0,10, 1)]
        layout = Layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',

            )
        
        return go.Figure(data=go.Scatter(x=iteration, y=loss), layout=layout)
    
    def delete_models(self):
        # try delete model from database?
        return
    
    def add_models(self):
        # create new models, add to database
        return
    
    def delete_datasets(self):
        # try delete dataset from database?
        return
    
    def add_datasets(self):
        # popup dataset list, and add one?
        return
    
    def handle_params(self, param_data:dict):
        self.parameters = param_data
        print("ALL PARAM", self.parameters)
        return
    
    
    