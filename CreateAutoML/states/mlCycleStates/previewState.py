import reflex as rx
from ..modelsState import ModelsPageState

class PreviewState(ModelsPageState):

    img: list[str] = []
    imagePairs:dict[str,bool] = {}

    @rx.var
    def not_empty(self) -> bool:
        return (len(self.img) > 0)
    
    @rx.var
    def preview_selected_image(self):
        # perform machine learning inference on selected image
        selected = [pair for pair in self.imagePairs if self.imagePairs[pair]]
        if len(selected) == 0:
            return None
        return selected[0]
    
    def clicked_img(self, imgname:str):
        for key in self.imagePairs:
            self.imagePairs[key] = False
        self.imagePairs[imgname] = True
    
    async def handle_upload(
        self, files: list[rx.UploadFile]
    ):
        """Handle the upload of file(s).

        Args:
            files: The uploaded files.
        """
        for file in files:
            upload_data = await file.read()
            outfile = rx.get_asset_path(file.filename)

            # Save the file.
            with open(outfile, "wb") as file_object:
                file_object.write(upload_data)

            # Update the img var.
            self.img.append(file.filename)
            self.imagePairs[file.filename] = False
    
    