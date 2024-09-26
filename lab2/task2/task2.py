from PIL import Image
import sys

if len(sys.argv) != 2:
    print("usage: python script.py <path_to_image>")
    exit()

file = sys.argv[1]
with Image.open(file) as img:
    if img.mode != 'RGB':
        img = img.convert('RGB')

    pixels = img.load()
    numR = 0
    numG = 0
    numB = 0

    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y]
            numR += r
            numG += g
            numB += b

    maxChannels = max(numR, numG, numB)

    if maxChannels == numR:
        dominantColor = 'Red'
    elif maxChannels == numG:
        dominantColor = 'Green'
    elif maxChannels == numB:
        dominantColor = 'Blue'

    print(f"Dominant color: {dominantColor}")