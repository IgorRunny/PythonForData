from PIL import Image, ImageFont, ImageDraw

filename = 'yacht.png'
wmFilename = 'clock.png'
text = 'Igor Bolshakov'
outFilename = 'output_image.jpg'

with Image.open(filename) as img, Image.open(wmFilename) as wmImg:
    img = img.convert('RGBA')
    wmImg = wmImg.convert('RGBA')
    wmImg = wmImg.resize((100, 50))
    textImage = Image.new('RGBA', wmImg.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(textImage)
    font = ImageFont.load_default(15)
    _, _, textWidth, textHeight = draw.textbbox((0, 0), text, font)
    textPosition = ((wmImg.width - textWidth) // 2, (wmImg.height - textHeight) // 2)
    draw.text(textPosition, text, font=font, fill=(178, 0, 255, 255))
    wmRes = Image.alpha_composite(wmImg, textImage)
    wmPos = (img.width - wmImg.width - 10, img.height - wmImg.height - 10)
    outImg = Image.new('RGB', img.size)
    outImg.paste(img)
    outImg.paste(wmRes, wmPos)
    outImg.save(outFilename, 'JPEG')
    outImg.show()

