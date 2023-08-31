import reflex as rx
from ..pages.bars import navbar
import functools

def add_navbar(func):
    def wrapper(*args, **kwargs):
        return rx.vstack(
            navbar(),
            func(*args, **kwargs)
        )
    return wrapper




def add_block_header(_func=None, *, headerName="test"):
    def decorator_header(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            return rx.vstack(
                rx.box(
                    rx.heading(headerName, text_align="left", border_bottom="1px solid black"),
                    text_align="left",
                    width="100%"
                ),
                func(*args, **kwargs),
                width="100%",
                padding_left="2em",
                padding_top="2em",
                padding_right="2em",
            )
        return wrapper

    if _func is None:
        return decorator_header
    else:
        return decorator_header(_func)

