from pyfiglet import Figlet
from random import randrange

figlet = Figlet()
fonts = figlet.getFonts()
# for font in fonts:
#     print(font)
randFontNum = randrange(len(fonts))
print(f"Font {randFontNum} is {fonts[randFontNum]}")

figlet.setFont(font=fonts[randFontNum])
input_str = input("Input: ")
output_str = print(f"Output: {figlet.renderText(input_str)}")
