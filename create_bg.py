import random
from PIL import Image, ImageDraw


r = lambda: random.randint(50, 215)
rc = lambda: (r(), r(), r())
listSym = []


def create_invader(border, draw, sprite_size):
    x0, y0, x1, y1 = border
    square_size = (x1-x0) / sprite_size

    print(border)
    print(square_size)
    print()

    # adding more whites (255, 255, 255) here will reduce density
    random_colors = [rc(), rc(), rc(), (178, 34, 34)]
    for y_size_id in range(0, sprite_size):
        for x_size_id in range(0, sprite_size):
            # border
            topLeftX = x_size_id*square_size + x0
            topLeftY = y_size_id*square_size + y0
            botRightX = topLeftX + square_size
            botRightY = topLeftY + square_size
            border = (topLeftX, topLeftY, botRightX, botRightY)
            # draw
            draw.rectangle(border, random.choice(random_colors))
    print('------------------------------')


sprite_size = 2
invaders = 6
imgSize = 200

origImage = Image.new('RGB', size=(imgSize, imgSize), color=(255, 255,255,0))
draw = ImageDraw.Draw(origImage)
invaderSize = imgSize / invaders
padding = invaderSize / sprite_size
for x in range(0, invaders):
    for y in range(0, invaders):
        if y in [2, 3]:
            continue  # this leaves horizontal white space for a title

        if random.choice([True, False, False]):
            continue
        topLeftX = x*invaderSize + padding/2
        topLeftY = y*invaderSize + padding/2
        botRightX = topLeftX + invaderSize - padding
        botRightY = topLeftY + invaderSize - padding
        border = (topLeftX, topLeftY, botRightX, botRightY)
        create_invader(border, draw, sprite_size)
origImage.save("abstract_pattern.jpg")
