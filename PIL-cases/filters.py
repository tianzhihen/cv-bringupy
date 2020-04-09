from PIL import Image, ImageFilter


def blur(image):
    return image.filter(ImageFilter.BLUR)


def contour(image):
    return image.filter(ImageFilter.CONTOUR)


def detail(image):
    return image.filter(ImageFilter.DETAIL)


def edge_enhance(image):
    return image.filter(ImageFilter.EDGE_ENHANCE)


def emboss(image):
    return image.filter(ImageFilter.EMBOSS)


def find_edges(image):
    return image.filter(ImageFilter.FIND_EDGES)


def sharpen(image):
    return image.filter(ImageFilter.SHARPEN)


def smooth(image):
    return image.filter(ImageFilter.SMOOTH)


def smooth_more(image):
    return image.filter(ImageFilter.SMOOTH_MORE)


if __name__ == '__main__':
    image_input_path = "/media/cv-bringupy/test.jpg"
    image_blur_output_path = "/media/cv-bringupy/test-blur.jpg"
    image_contour_output_path = "/media/cv-bringupy/test-contour.jpg"
    image_detail_output_path = "/media/cv-bringupy/test-detail.jpg"
    image_edge_enhance_output_path = "/media/cv-bringupy/test-edge_enhance.jpg"
    image_emboss_output_path = "/media/cv-bringupy/test-emboss.jpg"
    image_find_edges_output_path = "/media/cv-bringupy/test-find_edges.jpg"
    image_sharpen_output_path = "/media/cv-bringupy/test-sharpen.jpg"
    image_smooth_output_path = "/media/cv-bringupy/test-smooth.jpg"
    image_smooth_more_output_path = "/media/cv-bringupy/test-smooth_more.jpg"


    img = Image.open(image_input_path)

    img_blur = blur(img)
    img_blur.save(image_blur_output_path)

    img_contour = contour(img)
    img_contour.save(image_contour_output_path)

    img_detail = detail(img)
    img_detail.save(image_detail_output_path)

    img_edge_enhance = edge_enhance(img)
    img_edge_enhance.save(image_edge_enhance_output_path)

    img_emboss = emboss(img)
    img_emboss.save(image_emboss_output_path)

    img_find_edges = find_edges(img)
    img_find_edges.save(image_find_edges_output_path)

    img_sharpen = sharpen(img)
    img_sharpen.save(image_sharpen_output_path)

    img_smooth = smooth(img)
    img_smooth.save(image_smooth_output_path)

    img_smooth_more = smooth_more(img)
    img_smooth_more.save(image_smooth_more_output_path)







