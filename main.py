import cv2

from image_processing import Imageprocess

def main():
    IMAGE = "maze.png"

    process = Imageprocess(IMAGE)

    image = process.load_image()

    print("=" * 50)
    print("Image Loaded Successfully")
    print("=" * 50)

    print(f"Height : {image.shape[0]} pixels")
    print(f"Width : {image.shape[1]} pixels")
    print(f"Channels : {image.shape[2]}")

    cv2.imshow("Original MAze", image)

    cv2.waitKey(0)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
