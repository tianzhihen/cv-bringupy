from PIL import Image


def crop_image(image, roi_box):
    return image.crop(roi_box)


if __name__ == '__main__':
    image_input_path = "/media/cv-bringupy/test.jpg"
    image_output_path = "/media/cv-bringupy/test_crop.png"

    img = Image.open(image_input_path)

    roi_box = [100, 100, 400, 400]

    img_crop = crop_image(img, roi_box)
    img_crop.save(image_output_path)
