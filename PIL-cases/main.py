import os
from PIL import Image
from converts import convert_to_gray_image
from image_save_to_file import image_save_to_file
from image_to_thumbnail import image_convert_to_thumbnail
from filters import blur
from crop_image import crop_image
from resize_image import resize_image

if __name__ == '__main__':

    image_input_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../", "resource/origin/tly.jpg")
    output_root_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../", "resource/output/simple")

    img = Image.open(image_input_path)

    # 1. 转为灰度图
    image_gray_output_path = os.path.join(output_root_path, "test_gray.jpg")
    img_gray = convert_to_gray_image(img)
    image_save_to_file(img_gray, image_gray_output_path)

    # 2. 转为缩略图
    image_thumbnail_output_path = os.path.join(output_root_path, "test_thumbnail.jpg")
    img_thumbnail = image_convert_to_thumbnail(img.copy())
    image_save_to_file(img_thumbnail, image_thumbnail_output_path)

    # 3. 各种filter,如模糊
    image_blur_output_path = os.path.join(output_root_path, "test_blur.jpg")
    img_blur = blur(img)
    image_save_to_file(img_blur, image_blur_output_path)

    # 4. crop图像
    image_crop_output_path = os.path.join(output_root_path, "test_crop.jpg")
    roi_box = [0, 0, 300, 200]
    img_crop = crop_image(img, roi_box)
    image_save_to_file(img_crop, image_crop_output_path)

    # 5. resize图像
    image_resize_output_path = os.path.join(output_root_path, "test_resize.jpg")
    w, h = img.size
    img_crop = resize_image(img, (int(w/3), int(h/3)))
    image_save_to_file(img_crop, image_resize_output_path)



