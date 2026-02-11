import random
import sys
from pyfiglet import Figlet

if len(sys.argv) != 1 and len(sys.argv) != 3:
    sys.exit("invalid usage")

figlet = Figlet()

if len(sys.argv) == 1:
    input = input("input: ")
    available_fonts = figlet.getFonts()
    figlet.setFont(font = random.choice(available_fonts))
    print(figlet.renderText(input))
    
if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in figlet.getFonts():
            input = input("input: ")
            figlet.setFont(font = sys.argv[2])
            print(figlet.renderText(input))
        else:
            sys.exit("invalid usage") 
    else:
        sys.exit("invalid usage") 

