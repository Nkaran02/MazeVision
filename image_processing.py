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

    def convert_to_gray(self, image):
        gray_image = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )

        return gray_image

    def convert_to_binary(self, gray_image):
        threshould_value, binary_image = cv2.threshold(
            gray_image,
            127,
            255,
            cv2.THRESH_BINARY
        )

        return binary_image
