from PIL import Image


def image(name):
    image = Image.open(name)
    width, height = image.size
    width = width // 4
    height = height // 4
    for i in range(4):
        for j in range(4):
            if i != 3 or j != 3:
                left = ((95 * j), (95 * i))
                right = ((95 * (j + 1)), (95 * (i + 1)))
                kords = left + right
                im_crop = image.crop(kords)
                name = 'image' + str(i * 4 + j) + '.png'
                im_crop.save(name)
    return width, height
