from PIL import Image, ImageDraw, ImageFont

def CreateImage(num):
    w, h = 100, 100
    image = Image.new('RGB', (w, h), 'white')
    draw = ImageDraw.Draw(image)

    draw.rectangle([(0, 0), (99, 99)], outline='blue', width=5)
    font = ImageFont.load_default(30)

    _, _, text_width, text_height = draw.textbbox((0, 0), str(num), font)
    text_position = ((w - text_width) // 2, (h - text_height) // 2)

    draw.text(text_position, str(num), font=font, fill='red')

    return image


def main():
    for i in range(1, 4):
        image = CreateImage(i)
        image.show()
        image.save(f'image{i}.png', 'PNG')


main()