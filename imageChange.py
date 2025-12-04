from PIL import Image, ImageEnhance

jakob = Image.open("otsWingspan.png")
jakobBW = jakob.convert("L")
jakobSc = ImageEnhance.Contrast(jakobBW).enhance(5.2)
jakobSc.save("jakobKung.jpg")