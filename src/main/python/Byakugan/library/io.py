from pathlib import Path
import cv2
from app.defaults import IMG_EXTENSIONS


class IO:
    @staticmethod
    def get_images(path):
        files_list = []
        path = Path(path)
        if path.is_file():
            path = path.parents[0]
        if path.is_dir():
            for ext in IMG_EXTENSIONS:
                files_list.extend(path.glob(ext))
        return files_list

    @staticmethod
    def load_image(path):
        return cv2.imread(str(path), cv2.IMREAD_COLOR)
