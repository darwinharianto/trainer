import reflex as rx
from ..states.appState import State




def login_page():
    return rx.box(
        rx.hstack(
            rx.image(src="/images/login.jpg", html_height="100vh", html_width="50%"),
            rx.vstack(
                
                rx.input(placeholder="Username", on_change=State.set_username),
                rx.input(placeholder="Password", on_change=State.set_password, type_="password"),
                rx.cond(
                    State.login_fail,
                    rx.alert(
                        rx.alert_icon(),
                        rx.alert_title("Login Failed, username or password is incorrect"),
                        status="error",
                    ),
                ),
                rx.hstack(
                    rx.button("Login", on_click= State.user_login),
                    rx.button("register", on_click= State.register_user),

                ),

                # rx.link(
                    # "Login",
                    # href="/projects",
                    # border="0.1em solid",
                    # padding="0.5em",
                    # border_radius="0.5em",
                    # _hover={
                    #     "color": rx.color_mode_cond(
                    #         light="rgb(107,99,246)",
                    #         dark="rgb(179, 175, 255)",
                    #     )
                    # },
                # ), # change this to button to trigger authentications
                align_items="center",
                justify_content="center"
            ),
            height = "100%"
        ),
        width="100vw", 
        height="100vh",
        # bg="red",
    )
    return rx.box(
        rx.hstack(
            rx.box(
                rx.image(src="/images/login.jpg", html_height="100vh", html_width="100%"),
                width="50%",
            ),
            rx.vstack(
                rx.input(placeholder="Username"),
                rx.input(placeholder="Password", type="password"),
                rx.button("Login"),
                align_items="center",
                justify_content="center"
            ),
        ),
        width="100%",
        height="100vh",
        bg="lightgreen"
    )