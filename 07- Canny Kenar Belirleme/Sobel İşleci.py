from PIL import Image
import math

img = Image.open("static/img/canny.jpg")
width = img.size[0]
height = img.size[1]

newimg = Image.new("RGB", (width, height), "white")

for x in range(1, width - 1):
    for y in range(1, height - 1):
        Gx = 0
        Gy = 0

        r, g, b = img.getpixel((x - 1, y - 1))

        intensity = r + g + b

        Gx += -intensity
        Gy += -intensity

        r, g, b = img.getpixel((x - 1, y))

        Gx += -2 * (r + g + b)

        r, g, b = img.getpixel((x - 1, y + 1))

        Gx += -(r + g + b)
        Gy += (r + g + b)

        # orta piksel
        r, g, b = img.getpixel((x, y - 1))

        Gy += -2 * (r + g + b)

        r, g, b = img.getpixel((x, y + 1))

        Gy += 2 * (r + g + b)

        # right column
        r, g, b = img.getpixel((x + 1, y - 1))

        Gx += (r + g + b)
        Gy += -(r + g + b)

        r, g, b = img.getpixel((x + 1, y))

        Gx += 2 * (r + g + b)

        r, g, b = img.getpixel((x + 1, y + 1))

        Gx += (r + g + b)
        Gy += (r + g + b)

        length = math.sqrt((Gx * Gx) + (Gy * Gy))

        length = length / 4328 * 255

        length = int(length)

        newimg.putpixel((x, y), (length, length, length))

newimg.save("static / img / canny_sobel.bmp")
