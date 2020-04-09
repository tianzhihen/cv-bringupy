from PIL import Image


def convert_to_gray_image(image):
    return image.convert("L")


if __name__ == '__main__':
    image_input_path = "/media/cv-bringupy/test.jpg"
    image_output_path = "/media/cv-bringupy/test_gray.png"

    img = Image.open(image_input_path)

    img_gray = convert_to_gray_image(img)
    img_gray.save(image_output_path)
