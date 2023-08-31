import reflex as rx
from ...states.appState import State
from .logo import main_logo
# left side icon, right side user?

def add_navbar(func):
    def wrapper(*args, **kwargs):
        return rx.vstack(
            navbar(),
            func(*args, **kwargs)
        )
    return wrapper


class NavigationState(State):
    display_menu = False

    def handle_click(self):
        self.display_menu = not self.display_menu

def avatar_with_drop_down():
    return rx.menu(
            rx.menu_button(
                rx.avatar(
                    name=NavigationState.username,
                    size="md",
                ),
                _hover={"bg": "gray", "color": "white"},
            ),
            rx.menu_list(
                rx.text(NavigationState.username),
                rx.menu_item("Logout"),
            )
        )

def navbar():
    return rx.box(
        rx.hstack(
            rx.hstack(
                main_logo(),
            ),
            rx.spacer(),
            avatar_with_drop_down(),
        ),
        position="fixed",
        width="100%",
        padding_top="5px",
        padding_left="5px",
        padding_right="5px",
        padding_bottom="5px",
        z_index="9999",
        # background_image = "linear-gradient(#AFAAFF,#CBACF3 50%,#FFFFFF)",

    )