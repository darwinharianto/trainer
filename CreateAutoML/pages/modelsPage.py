import reflex as rx
# from .ml_cycle.trainingPage import training_page
from .ml_cycle.trainingSettingsPage import training_settings_page
from .ml_cycle.trainingPage import training_page
from .ml_cycle.previewPage import preview_page
from .ml_cycle.outputPage import output_page
from ..states.modelsState import ModelsPageState
from .bars.logo import main_logo

def create_link_with_button(target:list[str, str]):
    return rx.hstack(
                rx.link(target[0], href=target[1]), # need to be a loop over items inside state
                rx.spacer(),
                rx.button(
                    rx.icon(tag="minus"), 
                    border_radius="1em",
                    height="1.5em",
                ),
            )

def models_dropdown():
    return rx.accordion_item(
            rx.button_group(
                rx.accordion_button(rx.accordion_icon(), "Models"), 
                rx.cond(
                    ModelsPageState.show_model_button,
                    rx.button(
                        rx.icon(tag="add"), 
                        color_scheme="gray",
                        border_radius="1em",
                        height="2em",
                        width="1em",
                    ),
                ),
                on_mouse_enter=ModelsPageState.show_add_model(),
                on_mouse_leave=ModelsPageState.hide_add_model(),
            ),
            rx.accordion_panel(
                rx.foreach(ModelsPageState.targetModels, create_link_with_button),
            )
        ) 

def datasets_dropdown():
    return rx.accordion_item(
            rx.button_group(
                rx.accordion_button(rx.accordion_icon(), "Datasets"), 
                rx.cond(
                    ModelsPageState.show_dataset_button,
                    rx.button(
                        rx.icon(tag="add"), 
                        color_scheme="gray",
                        border_radius="1em",
                        height="2em",
                        width="1em",
                    ),
                ),
                on_mouse_enter=ModelsPageState.show_add_dataset(),
                on_mouse_leave=ModelsPageState.hide_add_dataset(),
            ),
            rx.accordion_panel(
                rx.foreach(ModelsPageState.targetDatasets, create_link_with_button),
            )
        )

def dropdown():
    return rx.accordion(
        models_dropdown(),
        datasets_dropdown(),
        
        allow_toggle=True,
        width="100%",
        allow_multiple=True,
        index=[0,1],
        # rx.menu_list(  
        #     rx.menu_item("Bolt"),
        #     rx.menu_item("Single Bolt"),  
        # ),
    )

def sidebar():  
    return rx.flex(  
        rx.vstack(  
            # rx.image(src="/favicon.ico", margin="0 auto"),  
            main_logo(),
            dropdown(),
            width = "250px",  
            padding_x = "2em",
            padding_y = "1em",  
        ),  
        position = "fixed",  
        height = "100%",  
        left = "0px",  
        top = "0px",  
        z_index = "1",
        display=["none","none","flex","flex","flex"],
        background_image = "linear-gradient(#FFFFFF,#CBACF3 50%,#AFAAFF)",
    )


def model_nav_bar():
    return rx.box(
        rx.flex(
                rx.spacer(),
                rx.button(
                    "Train!",  
                    padding_y = "1em", 
                    border="1px solid #BBCCFF",
                ),
                rx.spacer(),
                rx.spacer(),
                rx.menu(
                    rx.menu_button("Settings"),
                ),
                rx.spacer(),
                rx.menu(
                    rx.menu_button("Training"),
                ),
                rx.spacer(),
                rx.menu(
                    rx.menu_button("Evaluation"),
                ),
                rx.spacer(),
                rx.menu(
                    rx.menu_button("Preview"),
                ),
                rx.spacer(),
                rx.menu(
                    rx.menu_button("Output"),
                ),
                rx.spacer(),
                rx.spacer(),
            background_image = "linear-gradient(to right, #FFFFFF,#CBACF3 50%,#AFAAFF)",
            padding_y = "0.5em",  
        ),
        width="100%",
    )

    
def models_page():
    
    return rx.box(
        rx.hstack(
        sidebar(),
        rx.box(
            rx.tabs(
                items=[
                    ("Settings", training_settings_page(state=ModelsPageState)),
                    ("Training", training_page(state=ModelsPageState)),
                    ("Evaluation", rx.text("TAB 4")),
                    ("Preview", preview_page()),
                    ("Output", output_page()),
                ],
                # shadow="lg",
                margin_left=["0px","0px","250px","250px","250px"],
                # display=["flex","flex","flex","flex","flex"],
                margin_bottom="0px",
                
            ),
            # rx.vstack(
                # model_nav_bar(),
                # training_settings_page(
                    # datasetOptions=ModelsPageState.datasets,
                    # modelOptions=ModelsPageState.modelOptions,
                    # parameterOptions=ModelsPageState.parameterOptions,
                    # state=ModelsPageState
                    # ), # this must be rx.cond
                # rx.text(ModelsPageState.projectName), # this would be based on the nav bar? settings, training, eval, preview, output
                # training_page(state=ModelsPageState),
                # width="100%",
                # bg="red"
                # margin_left=["250px","250px","250px","250px","250px"],
            # ),
            height="100%",
            width="100%",
            # bg="red",
        ),
        ),
        width="100%",
        height = "100%",  
        position="fixed",
        overflow="auto",
            background_image = "linear-gradient(to right, #FFFFFF, #FFFFFF 80%,#AFAAFF)",
    )