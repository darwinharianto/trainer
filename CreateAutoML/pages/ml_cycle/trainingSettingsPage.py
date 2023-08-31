import reflex as rx
from ...utilities import add_block_header

def training_dataset(options:list[str], state:rx.State):
    return rx.vstack(
        rx.heading("Training Data", size="sm"),
        rx.select(
                options, 
                placeholder="Select dataset",
                on_change= state.set_training_dataset,
                color_schemes="twitter"
            )
    )

def validation_dataset(options:list[str], state:rx.State):
    return rx.vstack(
        rx.heading("Validation Data", size="sm"),
        rx.select(
                options, 
                placeholder="Select dataset",
                on_change= state.set_validation_dataset,
                color_schemes="twitter"
            )
    )

def evaluation_dataset(options:list[str], state:rx.State):
    return rx.vstack(
        rx.heading("Evaluation Data", size="sm"),
        rx.select(
                options, 
                placeholder="Select dataset",
                on_change= state.set_evaluation_dataset,
                color_schemes="twitter"
            )
    )

def data_section(state:rx.State):
    return rx.flex(
                    training_dataset(options=state.datasets, state=state),
                    rx.spacer(),
                    validation_dataset(options=state.datasets, state=state),
                    rx.spacer(),
                    evaluation_dataset(options=state.datasets, state=state),
                    width="100%",
                    justify="space-between",
                )
         
def modeltype(state: rx.state):
    return rx.flex(
        rx.hstack(
            rx.text("Algorithm: "),
            rx.select(
                    state.modelOptions, 
                    on_change= state.set_model,
                    color_schemes="twitter",
                    default_value= state.modelOptions[0],
                )
        ),
    )

def display_hyperparam(param:list):
    return rx.hstack(rx.text(param[0]), rx.input(default_value=str(param[1]), id=param[0]))
 
def hyperparameters(state: rx.state):
    # TODO how to loop through parameters?
    return rx.flex(
            rx.form(
                rx.vstack(
                    rx.foreach(state.parameterOptions, display_hyperparam),
                    rx.button("Submit", type_="submit"),
                ),
                on_submit=state.handle_params,
            )
        )

def training_settings_page(state:rx.State):

    return rx.flex(
            rx.accordion(
                rx.accordion_item(
                    rx.accordion_button(rx.heading("Data")),
                    rx.accordion_panel(data_section(state)),
                ),
                rx.accordion_item(
                    rx.accordion_button(rx.heading("Model")),
                    rx.accordion_panel(modeltype(state)),
                ),
                rx.accordion_item(
                    rx.accordion_button(rx.heading("Advanced Parameters")),
                    rx.accordion_panel(hyperparameters(state=state)),
                ),
                width="100%",
                allow_multiple=True,
                allow_toggle=True,
                default_index=[0,1],
            ),

            width="100%",

        )