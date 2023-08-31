import reflex as rx
from ...states.mlCycleStates.outputState import OutputState

def output_page():
    # 
    downloadLink = "'https://media.istockphoto.com/id/1156298839/ja/%E3%82%B9%E3%83%88%E3%83%83%E3%82%AF%E3%83%95%E3%82%A9%E3%83%88/%E8%8F%8A%E6%B1%A0%E6%B8%93%E8%B0%B7%E6%A3%AE%E6%9E%97%E3%81%AE%E6%BB%9D%E3%81%A8%E5%85%89%E7%B7%9A.jpg?s=1024x1024&w=is&k=20&c=eCqOjQ-ulw-IZa1HdjkJjSRa8jLxfyXIF1CCHrDAT8w='"

    return rx.vstack(
        # rx.script(OutputState.generate_download_link()),
        rx.script("""
            function downloadFile() {
                // Create an anchor element to trigger the download
                var link = document.createElement('a');
                link.href = """+ OutputState.generate_download_link + """ 
                link.download = 'example.png';  // Replace with the desired file name
                link.style.display = 'none';
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
            }
            """),
        # rx.script(OutputState.generate_download_link()),
        rx.button("Download", on_click=rx.client_side("downloadFile()"))
    )