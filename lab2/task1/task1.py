from PIL import Image

file = "yacht.png"
with Image.open(file) as img:
    img.load()
    r, g, b = img.split()

    newImg = Image.new('RGB', (img.width * 4, img.height * 2))

    newImg.paste(img)
    newImg.paste(r.convert('RGB'), (img.width, 0))
    newImg.paste(g.convert('RGB'), (img.width * 2, 0))
    newImg.paste(b.convert('RGB'), (img.width * 3, 0))

    rColored = Image.merge('RGB', (r, Image.new('L', r.size, 0), Image.new('L', r.size, 0)))
    gColored = Image.merge('RGB', (Image.new('L', g.size, 0), g, Image.new('L', g.size, 0)))
    bColored = Image.merge('RGB', (Image.new('L', b.size, 0), Image.new('L', b.size, 0), b))

    newImg.paste(img, (0, img.height))
    newImg.paste(rColored, (img.width, img.height))
    newImg.paste(gColored, (img.width * 2, img.height))
    newImg.paste(bColored, (img.width * 3, img.height))

    newImg.show()
    newFile = f'{file.split(".")[0]}-channels.png'
    newImg.save(newFile, 'PNG')

