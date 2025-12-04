from PIL import Image, ImageDraw

green = (0, 155, 58)
yellow = (254, 209, 0)
black = (0, 0, 0)

userX = int(input("Var ska flaggan ritas? Ange X-koordinat (0-200): "))
userY = int(input("Var ska flaggan ritas? Ange en Y-koordinat (0-100): "))

flag = Image.new("RGB", (200, 100), black)
flagDraw = ImageDraw.Draw(flag)

#Create green (upper triangle first then lower)
flagDraw.polygon([(userX+20, userY-1), (userX+100, userY+40), (userX+180, userY-1)], fill=green, outline=0, width=1)
flagDraw.polygon([(userX+20, userY+100), (userX+100, userY+60), (userX+180, userY+100)], fill=green, outline=0, width=1)

#Create yellow (top left to bottom right line then top right to bottom left)
flagDraw.line([(userX, userY), (userX+200, userY+100)], fill=yellow, width=22)
flagDraw.line([(userX+200, userY), (userX, userY+100)], fill=yellow, width=22)

flag.save("jamaicaFlag.png")