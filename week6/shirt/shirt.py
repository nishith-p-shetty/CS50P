import sys
import os
from PIL import Image, ImageOps

def main():
    try:
        if len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        elif len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif not ((sys.argv[1].endswith(".png") or sys.argv[1].endswith(".jpg")) and (sys.argv[2].endswith(".png") or sys.argv[2].endswith(".jpg"))):
            sys.exit("Invalid input")
        elif not ((sys.argv[1].endswith(".png") and sys.argv[2].endswith(".png")) or (sys.argv[1].endswith(".jpg") and sys.argv[2].endswith(".jpg"))):
            sys.exit("Input and output have different extensions")
        else:
            shirt = Image.open("shirt.png")
            with Image.open(sys.argv[1]) as input:
                input_cropped = ImageOps.fit(input, shirt.size)
                input_cropped.paste(shirt, mask = shirt)
                input_cropped.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()