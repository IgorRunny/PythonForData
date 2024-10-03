import sys
from pathlib import Path
import numpy
from skimage import io, util, transform

def make_transformation (pictures, transformation):
    for directory, img_list in pictures:
        last_num = len(img_list) - 1
        for img in img_list:
            last_num += 1
            img = (img * 255).astype(numpy.uint8)
            transformed_img = transformation(img)
            transformed_img = (transformed_img * 255).astype(numpy.uint8)
            io.imsave(f'{directory}/{str(last_num).zfill(4)}.jpg', transformed_img)

def set_transformation(property):
    def resize_image(image):
        return transform.rescale(image, 0.7, anti_aliasing=True, multichannel=True)

    def rotate_image(image):
        return transform.rotate(image, 45, resize=True)

    def flip_image(image):
        return numpy.fliplr(image)

    def make_noise_image(image):
        return util.random_noise(image)

    def translate_image(image):
        tform = transform.SimilarityTransform(translation=(15, 26))
        return transform.warp(image, tform)

    def complex_transform(image):
        image = resize_image(image)
        image = rotate_image(image)
        image = flip_image(image)
        image = make_noise_image(image)
        image = translate_image(image)
        return image

    match property:
        case 1:
            return resize_image
        case 2:
            return rotate_image
        case 3:
            return flip_image
        case 4:
            return make_noise_image
        case 5:
            return translate_image
        case 6:
            return complex_transform

def user_board():
    if len(sys.argv) != 2:
        print('Wrong number of arguments')
        return
    path = Path(sys.argv[1])
    pictures = []
    for directory in path.iterdir():
        pictures.append([str(directory), io.imread_collection(f'{directory}/*.jpg')])
    print("List of available transformation:\n"
          "1. Resize\n"
          "2. Rotate\n"
          "3. Flip\n"
          "4. Make noise\n"
          "5. Translate\n"
          "6. Complex transformation\n")
    for i in range(len(pictures) - 1, -1, -1):
        collection = pictures[i][1]
        if not len(collection):
            del pictures[i]
    while True:
        property = input("Print the number of transformation: ")
        try:
            property = int(property)
            if 1 <= property <= 6:
                break
        except:
            print("!Wrong number!")
            pass
    try:
        transformation = set_transformation(property)
        make_transformation(pictures, transformation)
        print("Success!")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    user_board()