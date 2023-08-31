from rxconfig import config
from ..states.appState import State
import reflex as rx

class TaskState(State):  
    supportedTasks: list[str] = ["Detection", "Classification", "Segmentation"] 
   
    def navigate_to(self):  
        print(f"navigate to {self.supportedTasks[0]}")


def make_card(taskname:str): 
    card = rx.link(
            rx.card(
                rx.image(src="/images/"+taskname+".png", height="8em", width="auto"),
                header=rx.heading(taskname, size="sm"),
                width="10em",
                height="auto",
                _hover={"cursor": "pointer", "box_shadow": "2xl"},
                # on_click=TaskState.navigate_to,
            ),
            href = "/tasks/"+taskname,

        )
    return card

def task(name:str):
    return rx.vstack(
                rx.box(
                    rx.heading(f"{name}"),
                    width="100%", # this makes it go to the left??
                    padding_left="5%"
                ),
                rx.divider(border_color="#000000"),
                rx.spacer(),
                rx.responsive_grid(
                    rx.foreach(TaskState.supportedTasks, make_card),
                    columns=[i+1 for i in range(6)],
                    spacing="3em",
                ),
                width="100%"
            )
