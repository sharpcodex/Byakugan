from pathlib import Path
from qtpy.QtGui import QPixmap
import cv2



class IO:
    def __init__(self):
        pass

    @staticmethod
    def get_images(path):
        images_files_list = []
        path = Path(path)
        if path.is_file():
            path = path.parents[0]
        if path.is_dir():
            images_files_list = list(path.glob('*.jpg'))
        return images_files_list

    @staticmethod
    def load_image(path):
        data = cv2.imread(str(path), cv2.IMREAD_COLOR)
        return data
