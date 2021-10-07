from PIL import Image
import math
import numpy

image = Image.open("static/img/canny.jpg")
newmat = image.load()
wdh = image.size[0]
hgh = image.size[1]
graylist = [[0] * hgh for x in range(wdh)]
for k in range(wdh):
    for l in range(hgh):
        r, g, b = image.getpixel((k, l))
        gray = (int)((r * 0.2126) + (g * 0.7152) + (b * 0.0722))
        graylist[k][l] = gray
        newmat[k, l] = (gray, gray, gray)
meanArray = [[0] * hgh for x in range(wdh)]
for i in range(1, hgh - 1):
    for j in range(1, wdh - 1):
        meanArray[j][i] = (graylist[j][i - 1]
                           + graylist[j][i + 1]
                           + graylist[j][i]
                           + graylist[j - 1][i - 1]
                           + graylist[j - 1][i + 1]
                           + graylist[j - 1][i]
                           + graylist[j + 1][i - 1]
                           + graylist[j + 1][i + 1]
                           + graylist[j + 1][i]) / 9;
        mean_value = (int)(round(meanArray[j][i]))
        newmat[j, i] = (mean_value, mean_value, mean_value)

robertArray = [[0] * hgh for x in range(wdh)]
robert_x = [[2, 1, 0],
            [1, 0, -1],
            [0, -1, -2]]
robert_y = [[0, -1, -2],
            [1, 0, -1],
            [2, 1, 0]]
for m in range(1, hgh - 1):
    for n in range(1, wdh - 1):
        robertArray[n][m] = (int)(math.fabs(graylist[n][m] - graylist[n - 1][m - 1])) + (int)(
            math.fabs(graylist[n][m - 1] - graylist[n - 1][m]))
        rbrt_value = int(round(robertArray[n][m]))
        newmat[n, m] = (rbrt_value, rbrt_value, rbrt_value)
newangle = [[0] * hgh for x in range(wdh)]
newedge = [[0] * hgh for x in range(wdh)]
for x in range(1, wdh - 1, 1):
    for y in range(1, hgh - 1, 1):
        Gx = (robert_x[0][0] * graylist[x - 1][y - 1]
              + robert_x[0][1] * graylist[x - 1][y]
              + robert_x[0][2] * graylist[x - 1][y + 1]
              + robert_x[1][0] * graylist[x][y - 1]
              + robert_x[1][1] * graylist[x][y]
              + robert_x[1][2] * graylist[x][y + 1]
              + robert_x[2][0] * graylist[x + 1][y - 1]
              + robert_x[2][1] * graylist[x + 1][y]
              + robert_x[2][2] * graylist[x + 1][y + 1])

        Gy = (robert_y[0][0] * graylist[x - 1][y - 1]
              + robert_y[0][1] * graylist[x - 1][y]
              + robert_y[0][2] * graylist[x - 1][y + 1]
              + robert_y[1][0] * graylist[x][y - 1]
              + robert_y[1][1] * graylist[x][y]
              + robert_y[1][2] * graylist[x][y + 1]
              + robert_y[2][0] * graylist[x + 1][y - 1]
              + robert_y[2][1] * graylist[x + 1][y]
              + robert_y[2][2] * graylist[x + 1][y + 1])

        edge = round(math.sqrt((Gx * Gx) + (Gy * Gy)))
        thisAngle = math.degrees(math.atan2(Gx, Gy))

        if (((thisAngle < 22.5) and (thisAngle > -22.5)) or (thisAngle > 157.5) or (thisAngle < -157.5)):
            newangle[x][y] = 0
        if (((thisAngle > 22.5) and (thisAngle < 67.5)) or ((thisAngle < -112.5) or (thisAngle > -157.5))):
            newangle[x][y] = 45
        if (((thisAngle > 67.5) and (thisAngle < 112.5)) or ((thisAngle < -67.5) or (thisAngle > -112.5))):
            newangle[x][y] = 90
        if (((thisAngle > 112.5) and (thisAngle < 157.5)) or ((thisAngle < -22.5) and (thisAngle > -67.5))):
            newangle[x][y] = 135

        edge = int(edge)
        newedge[x][y] = edge

for p in range(1, wdh - 1, 1):
    for q in range(1, hgh - 1, 1):
        if newangle[p][q] == 0:
            if (newedge[p][q] <= newedge[p + 1][q]) or (newedge[p][q] <= newedge[p - 1][q]):
                newedge[p][q] = 0
        elif newangle[p][q] == 45:
            if (newedge[p][q] <= newedge[p + 1][q + 1]) or (newedge[p][q] <= newedge[p - 1][q - 1]):
                newedge[p][q] = 0
        elif newangle[p][q] == 90:
            if (newedge[p][q] <= newedge[p][q + 1]) or (newedge[p][q] <= newedge[p][q - 1]):
                newedge[p][q] = 0
        else:
            if (newedge[p][q] <= newedge[p - 1][q + 1]) or (newedge[p][q] <= newedge[p + 1][q - 1]):
                newedge[p][q] = 0
        nonmax_value = newedge[p][q]
        newmat[p, q] = (nonmax_value, nonmax_value, nonmax_value)
maxim = numpy.max(newedge)
thrd_hgh = maxim * 0.1
thrd_low = maxim * 0.5
high_thres = int(round(thrd_hgh))
low_thres = int(round(thrd_low))
for a in range(1, wdh - 1, 1):
    for b in range(1, hgh - 1, 1):
        if newedge[a][b] > high_thres:
            newedge[a][b] = newedge[a][b]
        elif (newedge[a][b] > low_thres) and (newedge[a][b] < high_thres):
            newedge[a][b] = int(round(newedge[a][b] * 0.1))
        else:
            newedge[a][b] = 0
        thrd_value = newedge[a][b]
        newmat[a, b] = (thrd_value, thrd_value, thrd_value)
image.save("static/img/canny_Robert.png")
