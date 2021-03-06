from pathlib import Path

IMG_EXTENSIONS = ['*.bmp', '*.png', '*.jpg', '*.jpeg', '*.jpe']


class PathHelpers:
    @staticmethod
    def get_images_in_path(path):
        files_list = []
        path = Path(path)
        if path.is_file():
            path = path.parents[0]
        if path.is_dir():
            for ext in IMG_EXTENSIONS:
                files_list.extend(path.glob(ext))
        return files_list
