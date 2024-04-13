from PIL import Image
import math
import random as rand

r_sum = 0
g_sum = 0
b_sum = 0

def printPixels(x, y, image):
    global r_sum, g_sum, b_sum
    for i in range(x):
        for j in range(y):
            r, g, b = image.getpixel((i, j))

            r_sum += r
            g_sum += g
            b_sum += b
    return (r_sum/(x * y), g_sum/(x * y), b_sum/(x * y))

def changePixels(x, y, image):
    global r_mean, g_mean, b_mean
    for i in range(x):
        for j in range(y):
            r, g, b = image.getpixel((i, j))
            # add random value to change some more
            randomVal = rand.randint(0, 255)
            image.putpixel((i, j), (math.ceil((r + r_mean + randomVal)/3), math.ceil((g + r_mean + randomVal)/3), math.ceil((b + r_mean + randomVal)/3)))

try:
    img = Image.open("src/banana-grayscale.png")
    img.show();
    # print(img.histogram());
    width, height = img.size
    
    r_mean, g_mean, b_mean = printPixels(width, height, img)
    r_mean, g_mean, b_mean = math.ceil(r_mean), math.ceil(g_mean), math.ceil(b_mean)

    # print(math.ceil(r_mean), math.ceil(g_mean), math.ceil(b_mean))

    # let's define a custom filter 
    # test change all the r, g, b values with their means and make a new image
    # (r + r_mean)/2
    changePixels(width, height, img)
    img.show()

except:
    print("Unable to load image")