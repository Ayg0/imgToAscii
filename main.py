from PIL import Image
import sys
import os

def convertToAscii(image_path):
    brightnessArray = " `.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"
    accuracy = len(brightnessArray) - 1

    try:
        image = Image.open(image_path)
    except:
        print("Error, can't Open Image", image_path)
        return 1

    image = image.resize((200, 200))
    pixels = image.load()
    width, height = image.size

    with open(os.path.splitext(image_path)[0] + '.txt', 'w') as file:
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                brightness = sum([r, g, b]) / 3
                index = int((brightness * accuracy) / 255)
                file.write(brightnessArray[index])
            file.write('\n')
    return 0
    
if (len(sys.argv) != 2):
    print("Error, you need to supply the image path.")
    exit(1)
if (convertToAscii(sys.argv[1])):
    exit(1)