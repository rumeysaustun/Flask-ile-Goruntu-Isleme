from PIL import Image
import math
import numpy

im = Image.open("static/img/canny.jpg")
pix = im.load()
w = im.size[0]
h = im.size[1]
img = Image.new('RGB', (w, h), "black")
pixels = img.load()
graylist = [[0] * h for x in range(w)]
for i in range(w):
    for j in range(h):
        r, g, b = im.getpixel((i, j))
        gray = (int)((r * 0.2126) + (g * 0.7152) + (b * 0.0722))
        graylist[i][j] = gray
        pixels[i, j] = (gray, gray, gray)
for m in range(1, w - 1, 1):
    for n in range(1, h - 1, 1):
        sum = ((graylist[m - 1][n - 1] * 1) + (graylist[m - 1][n] * 2) + (graylist[m - 1][n + 1] * 1) +
               (graylist[m][n - 1] * 2) + (graylist[m][n] * 4) + (graylist[m][n + 1] * 2) + (
                           graylist[m + 1][n - 1] * 1) + (graylist[m + 1][n] * 2) + (graylist[m + 1][n + 1] * 1)) / 16
        value = round(sum)
        value = int(value)
        graylist[m][n] = value
        pixels[m, n] = (value, value, value)
prewitt_x = [[-1, -1, -1],
             [0, 0, 0],
             [1, 1, 1]]
prewitt_y = [[-1, 0, 1],
             [-1, 0, 1],
             [-1, 0, -1]]
image = Image.new('RGB', (w, h), "black")
image_pix = image.load()
anglelist = [[0] * h for x in range(w)]
edgelist = [[0] * h for x in range(w)]

for x in range(1, w - 1, 1):
    for y in range(1, h - 1, 1):
        edge_x = (prewitt_x[0][0] * graylist[x - 1][y - 1]) + (prewitt_x[0][1] * graylist[x - 1][y]) +(prewitt_x[0][2] * graylist[x - 1][y + 1]) + (prewitt_x[1][0] * graylist[x][y - 1]) +    (prewitt_x[1][1] * graylist[x][y]) + (prewitt_x[1][2] * graylist[x][y + 1]) +    (prewitt_x[2][0] * graylist[x + 1][y - 1]) + (prewitt_x[2][1] * graylist[x + 1][y]) + (      prewitt_x[2][2] * graylist[x + 1][y + 1])
    edge_y = (prewitt_y[0][0] * graylist[x - 1][y - 1]) + (prewitt_y[0][1] * graylist[x - 1][y]) + (            prewitt_y[0][2] * graylist[x - 1][y + 1]) + (prewitt_y[1][0] * graylist[x][y - 1]) +    (prewitt_y[1][1] * graylist[x][y]) + (prewitt_y[1][2] * graylist[x][y + 1]) +    (prewitt_y[2][0] * graylist[x + 1][y - 1]) + (prewitt_y[2][1] * graylist[x + 1][y]) +    (prewitt_y[2][2] * graylist[x + 1][y + 1])
edge = round(math.sqrt((edge_x * edge_x) + (edge_y * edge_y)))
angle = math.degrees(math.atan2(edge_y, edge_x))

if (((angle < 22.5) and (angle > -22.5)) or (angle > 157.5) or (angle < -157.5)):
    anglelist[x][y] = 0
if (((angle > 22.5) and (angle < 67.5)) or ((angle < -112.5) and (angle > -157.5))):
    anglelist[x][y] = 45
if (((angle > 67.5) and (angle < 112.5)) or ((angle < -67.5) and (angle > -112.5))):
    anglelist[x][y] = 90
if (((angle > 112.5) and (angle < 157.5)) or ((angle < -22.5) and (angle > -67.5))):
    anglelist[x][y] = 135
edge = int(edge)
edgelist[x][y] = edge

for p in range(1, w - 1, 1):
    for q in range(1, h - 1, 1):
        if anglelist[p][q] == 0:
            if (edgelist[p][q] <= edgelist[p + 1][q]) or (edgelist[p][q] <= edgelist[p - 1][q]):
                edgelist[p][q] = 0
        elif anglelist[p][q] == 45:
            if (edgelist[p][q] <= edgelist[p + 1][q + 1]) or (edgelist[p][q] <= edgelist[p - 1][q - 1]):
                edgelist[p][q] = 0
        elif anglelist[p][q] == 90:
            if (edgelist[p][q] <= edgelist[p][q + 1]) or (edgelist[p][q] <= edgelist[p][q - 1]):
                edgelist[p][q] = 0
        else:
            if (edgelist[p][q] <= edgelist[p - 1][q + 1]) or (edgelist[p][q] <= edgelist[p + 1][q - 1]):
                edgelist[p][q] = 0

m = numpy.max(edgelist)
high_thres = m * 0.2
low_thres = m * 0.1
high_thres = int(round(high_thres))
low_thres = int(round(low_thres))
for a in range(1, w - 1, 1):
    for b in range(1, h - 1, 1):
        if edgelist[a][b] > high_thres:
            edgelist[a][b] = edgelist[a][b]
        elif (edgelist[a][b] > low_thres) and (edgelist[a][b] < high_thres):
            edgelist[a][b] = int(round(edgelist[a][b] * 0.1))
        else:
            edgelist[a][b] = 0
        e = edgelist[a][b]
        image_pix[a, b] = (e, e, e)
image.save("static/img/canny_prewitt.bmp")


