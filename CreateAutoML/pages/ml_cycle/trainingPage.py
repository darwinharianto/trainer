import reflex as rx

def plot_loss(state: rx.state):
    return rx.plotly(data=state.loss_plot)

def snapshot(state: rx.state):
    return rx.table(
        rx.thead(
            rx.tr(
                rx.th("Iteration"),
                rx.th("loss"),
                rx.th("Date"),
                rx.th("Snapshot"),
            )
        ),
        rx.tbody(
            rx.tr(
                rx.td("iteration 10"),
                rx.td("0.5"),
                rx.td("2022-01-01"),
                rx.td(rx.link("iteration 10", href="/aa/bb")),
            )
        )
    )


def training_page(state: rx.state):
   
    return rx.vstack(
        plot_loss(state),
        snapshot(state),
    )
