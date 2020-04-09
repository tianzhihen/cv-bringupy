from PIL import Image


def resize_image(image, size_w_h):
    return image.resize(size_w_h)


if __name__ == '__main__':
    image_input_path = "/media/cv-bringupy/test.jpg"
    image_output_path = "/media/cv-bringupy/test_resize.png"

    img = Image.open(image_input_path)

    size_w_h = (200, 200)

    img_resize = resize_image(img, size_w_h)
    img_resize.save(image_output_path)
