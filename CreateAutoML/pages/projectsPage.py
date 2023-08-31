import reflex as rx
from ..states.projectState import ProjectState
from .bars import *



def make_card(header:str): 
    
    card = rx.link(
            rx.card(
                rx.heading(header, size="sm"),
                width="10em",
                height="auto",
                _hover={"cursor": "pointer", "box_shadow": "2xl"},
            ),
            href = "models?project="+header,
        )
    return card

def new_project_form():
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="Project Name",
                    id="name",
                ),
                rx.input(
                    placeholder="metadata", id="metadata"
                ),
                rx.hstack(
                    rx.button("Submit", type_="submit"),
                    rx.button("Cancel", on_click=ProjectState.toggle_show_project_form),
                )
            ),
            on_submit=ProjectState.add_project,
        ),
    )
 
def modal_form():

    return rx.modal(
        rx.modal_overlay(
            rx.modal_content(
                rx.modal_header("Create New Project"),
                new_project_form(),
                # rx.modal_footer(
                #     rx.button("Cancel", on_click=ProjectState.toggle_show_project_form)
                # ),
                # bg="rgba(0, 0, 0, 1)",
            ),
        ),
        is_open=ProjectState.show_project_form,
    )
    

def projects_page():


    return rx.vstack(
        # add filter search
        rx.flex(
            rx.heading("Discover Projects"),
            rx.spacer(),
            rx.button("Create New Project", on_click=ProjectState.toggle_show_project_form),
            justify="space-between",
            width="100%",
            padding_left= "1em",
            padding_right= "1em",
        ),
        
        rx.text_area(
            placeholder="Filter search",
        ),
        rx.responsive_grid(rx.foreach(ProjectState.projects, make_card), 
                           spacing="3em",
                           columns=[i+1 for i in range(6)]
                           ),
        rx.foreach(ProjectState.projects2, rx.text), 
        modal_form(), 
        padding_top="5em"
    )