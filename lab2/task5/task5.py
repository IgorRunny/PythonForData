from PIL import Image
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("-ftype", "--ftype", type=str, default='')
namespace = parser.parse_args()
ftype = namespace.ftype.upper()

path = Path('.')

for file in path.iterdir():
    try:
        with Image.open(file) as img:
            img.thumbnail((50, 50))
            if ftype:
                if img.format == ftype:
                    img.show()
            else:
                img.show()
    except:
        pass