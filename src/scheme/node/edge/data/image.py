#---------------------------------------------
from src.param import param_interface
from src.scheme.loop import scheme_update
from src.connection.HTTPS import https_client_get
from src.utils import terminal
from src.utils import daemon


class Image(daemon.Daemon):
    def thread_function(self):
        # Load current image
        image_acquired = https_client_get.get_image("edge")

        # Update image
        if(image_acquired):
            scheme_update.update_image()

    name = "Image loader";
    run_sleep = 0.1;
