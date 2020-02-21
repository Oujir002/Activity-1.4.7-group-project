import magnify
import sys
try:
    pos = input("What position do you want to magnify? (input as tuple or list) ")
    power = input("How much do you want to magnify? ")
    filename = input("What picture do you want to magnify?(input as an absolute filename with quotes and double slash \\\\) ")
except SyntaxError:
    print("[ERROR]: Don't input empty values")
    sys.exit()
print(filename)
try:
    y_pos = pos[0]
    x_pos = pos[1]
    stretch.stretch(pos[0],pos[1],power,filename)
except TypeError:
    print("[ERROR]: You are supposed to input as tuple or list")