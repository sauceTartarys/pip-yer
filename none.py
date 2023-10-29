from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance


with Image.open("img.png") as pic_original:
    pic_blured = pic_original.filter(ImageFilter.BLUR)
    pic_blured.save("img_1.png")
    pic_blured.show()