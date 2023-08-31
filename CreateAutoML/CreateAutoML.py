"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx
from .pages.tasksPage import *
from .pages.loginPage import login_page
from .pages.projectsPage import projects_page
from .pages.modelsPage import models_page
from .middleware import LoggingMiddleware
from .pages.bars import *

tasks_url = "http://localhost:3000//tasks"
filename = f"{config.app_name}/{config.app_name}.py"


def dropdown_menu():
    return rx.menu(
        rx.menu_button("Projects"),  
        rx.menu_button("Datasets"),  
        rx.menu_list(  
            rx.menu_item("Bolt"),
            rx.menu_item("Single Bolt"),  
        ),
    )

def sidebar():  
    return rx.box(  
        rx.vstack(  
            rx.image(src="/favicon.ico", margin="0 auto"),  
            rx.heading(  
                "Sidebar",  
                text_align = "center",
                margin_bottom = "1em",  
            ),
            dropdown_menu(),
            
            width = "250px",  
            padding_x = "2em",  
            padding_y = "1em",  
        ),  
        position = "fixed",  
        height = "100%",  
        left = "0px",  
        top = "0px",  
        z_index = "500",
        display=["none","none","flex","flex","flex"]
    )


def index() -> rx.Component:
    return rx.fragment(
        navbar(),
        rx.vstack(
            width="100%",
        ),
        rx.vstack(
            # task("Image"),
            rx.heading("Projects page", font_size="2em"),
            rx.box("Get started by logging in", rx.code(filename, font_size="1em")),
            rx.link(
                "Check out our docs!",
                href=tasks_url,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": rx.color_mode_cond(
                        light="rgb(107,99,246)",
                        dark="rgb(179, 175, 255)",
                    )
                },
            ),
            spacing="1.5em",
            font_size="2em",
            padding_top="10%",
        ),
        width="100%",
    )


# Add state and page to the app.
app = rx.App(middleware=[LoggingMiddleware()])


app.add_page(index, route="/", on_load=State.reroute())
app.add_page(task("Image"), route="/tasks", on_load=State.reroute())
app.add_page(login_page, route="/login")

# app.add_page(dataset, route="/datasets") # maybe just embed cvat?
@rx.page(route="/models", title="models", on_load=State.reroute())
# @add_navbar
def models():
    return models_page()



@rx.page(route="/projects", title="projects", on_load=State.reroute())
@add_navbar
def my_function():
    return projects_page()
    

app.compile()
