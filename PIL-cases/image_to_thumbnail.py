from PIL import Image


def image_convert_to_thumbnail(image, scale=0.1):
    w, h = image.size
    image.thumbnail((w * scale, h * scale))
    return image


if __name__ == '__main__':
    image_input_path = "/media/cv-bringupy/test.jpg"
    image_output_path = "/media/cv-bringupy/test_thumbnail.jpg"

    img = Image.open(image_input_path)
    img_thumbnail = image_convert_to_thumbnail(img)
    img_thumbnail.save(image_output_path)
