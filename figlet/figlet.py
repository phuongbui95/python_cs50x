import sys
from pyfiglet import Figlet
from random import randrange

def checkCommandLine():
    # print(sys.argv) # check elements after the "command word" in command-line
    if len(sys.argv)==3 and ("-f" or "--font") in sys.argv[1]:
        # print("Not Random Font")
        figletExecution(sys.argv[2])
    elif len(sys.argv)==1:
        # print("Random Font")
        figletExecution()
    else:
        print("Invalid usage")
        return sys.exit(1)

def figletExecution(f=None):
    figlet = Figlet()
    fonts = figlet.getFonts()
    if f is None:    
        randFontNum = randrange(len(fonts))
        # print(f"Font {randFontNum} is {fonts[randFontNum]}")
        figlet.setFont(font=fonts[randFontNum])
    else:
        if f not in fonts:
            print("Invalid usage")
            return sys.exit(1)
        else:
            figlet.setFont(font=f)
    
    input_str = input("Input: ")
    # Output
    return print(f"Output: {figlet.renderText(input_str)}")

# Main
if __name__ == "__main__":
    checkCommandLine()
