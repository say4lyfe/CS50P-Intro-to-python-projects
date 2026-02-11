import sys
from PIL import ImageOps
from PIL import Image
import os

while True:
    try:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")

        if len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")

        root1, extension1 = os.path.splitext(sys.argv[1])
        root2, extension2 = os.path.splitext(sys.argv[2])

        if extension1 != extension2:
            sys.exit("Input and output have different extensions")

        elif  extension2.lower() not in (".jpg" , ".jpeg" , ".png"):
            sys.exit("Invalid output")

        else:
            shirt = Image.open("shirt.png")
            image = Image.open(sys.argv[1])
            shirt = ImageOps.fit(shirt, size = (600, 600))
            image = ImageOps.fit(image, size = (600, 600))
            image.paste(shirt, mask = shirt)
            image.save(sys.argv[2])
            break

    except(FileNotFoundError):
        sys.exit("Input does not exist")



