import sys
from pyfiglet import Figlet
import random

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
    if f is None:    
        fonts = figlet.getFonts()
        figlet.setFont(font=random.choice(fonts))
    else:    
        try:
            figlet.setFont(font=f)
        except:
            print("Invalid usage")
            return sys.exit(1)
    
    input_str = input("Input: ")
    # Output
    return print(f"Output: {figlet.renderText(input_str)}")

# Main
if __name__ == "__main__":
    checkCommandLine()
