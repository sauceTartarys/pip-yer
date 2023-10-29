from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance


with Image.open("img_gray.png") as pic_original:
    pic_gray = pic_original.convert("L")
    pic_gray.save("img_gray.png")
    print("зображення відкрито\nРозмір:", pic_gray.size)
    print("Формат:", pic_gray.format)
    print('Тип', pic_gray.mode)
    pic_gray.show()