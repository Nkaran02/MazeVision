import cv2

class Imageprocess:
    def __init__(self, img_path: str):
        self.img_path = img_path

    def load_image(self):
        image = cv2.imread(self.img_path)

        if image is None:
            raise FileExistsError(
                f"Unable to load image {self.img_path}"
            )

        return image


