import reflex as rx
from ...states.mlCycleStates.previewState import PreviewState

def empty_preview():
    return rx.vstack(rx.button("Select File", color = "#FFAABB", bg = "white", 
                border = "1px solid #FFAABB"),
            rx.text("Drag and drop files here or click to select files"), 
    )

def image_preview(image:list):
    return rx.hstack(
                    rx.cond(image[1],
                            rx.image(src = image[0], 
                            width="100px", 
                            height="100px",
                            border="5px solid #FF0000",
                            box_shadow="0 0 10px #FFD700",
                            on_click= PreviewState.clicked_img(image[0])
                            ),
                            rx.image(src = image[0], 
                            width="100px", 
                            height="100px",
                            on_click= PreviewState.clicked_img(image[0])
                            ),
                    ),
                     rx.text(image[0]),
                )
def images():
    # List to store image components
    return rx.vstack(
            rx.foreach(
                PreviewState.imagePairs, 
                image_preview,
            )
        )

def upload_section():
    """The main view."""  
    color = "#FFAABB"
    return rx.vstack(
    rx.upload(
        rx.vstack(
            rx.cond(
                PreviewState.not_empty,
                c1=images(),
                c2=empty_preview()
            )
        ),  
        border = f"1px dotted { color }",
        no_click=True,  
        on_mouse_leave=PreviewState.handle_upload(rx.upload_files()),
        on_mouse_enter=PreviewState.handle_upload(rx.upload_files()),
        padding = "5em"),  
    padding = "PreviewState")

def mlresult():
    # this is for boxes, what about segmentation and others?
    return rx.box(
        rx.image(src=PreviewState.preview_selected_image),
        rx.table(
            rx.tbody(
                rx.tr(
                    rx.td("Bolt"),
                    rx.td("Confidence 100%"),
                ),
            ),
        ),
    )
def preview_page():

    return rx.hstack(
        upload_section(),
        mlresult()
        )