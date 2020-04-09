import os


# PIL 可根据扩展名自动转换图片格式
def image_save_to_file(img, file_path):
    try:
        img.save(file_path)

    except Exception:
        print("can't save file: {}".format(file_path))
