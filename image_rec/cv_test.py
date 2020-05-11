import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('G19_edited.jpg')

cv2.namedWindow('G19', cv2.WINDOW_NORMAL)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_bound = np.array([5, 190, 190])
upper_bound = np.array([25, 255, 255])
mask = cv2.inRange(hsv, lower_bound, upper_bound)
res = cv2.bitwise_and(img, img, mask=mask)
vector = np.nonzero(mask)  # tuple
vector = np.array([vector[0], vector[1]])  # numpy array

vector = np.transpose(vector)
# rotation matrix
R = np.array([[-1, 0],
              [0, -1]])
# rotate the coordinates
for i in range(len(vector)):
    vector[i] = np.dot(R, vector[i])
vector = np.transpose(vector)
# find mininum/maximum x/y value
minx = np.argmin(vector[0])
maxx = np.argmax(vector[0])
miny = np.argmin(vector[1])
maxy = np.argmax(vector[1])

# cutoff the first 50 pixels to make it straight
threshold = 50
cutoff = np.array([[vector[0, minx] + threshold, vector[0, minx] + threshold],
                   [vector[1, miny], vector[1, maxy]]])

args = np.argwhere(vector[0] < vector[0, minx] + threshold)
# new vector with cutoff
new_vector = np.array([np.delete(vector[0], args), np.delete(vector[1], args)])
endargs = np.argwhere(vector[0] == vector[0, minx] + threshold)
# endpoints of contour
endpoint1 = vector[1, endargs[0]]
endpoint2 = vector[1, endargs[-1]]
# horizontal distance between data points of contour
interval = 110
# use lists for upper and lower coordinates of contour because appending is easier lol
xupper = list()
yupper = list()
xlower = list()
ylower = list()
# append endpoints
xupper.append(cutoff[0, 0])
yupper.append(endpoint1[0])
xlower.append(cutoff[0, 0])
ylower.append(endpoint2[0])
# running variable
j = cutoff[0, 0] + interval
while j < vector[0, maxx]:
    endargs = np.argwhere(vector[0] == j)
    endpoint1 = vector[1, endargs[0]]
    endpoint2 = vector[1, endargs[-1]]
    xupper.append(j)
    yupper.append(endpoint1[0])
    xlower.append(j)
    ylower.append(endpoint2[0])
    j = j + interval
# not enough data points at the tip
# second for loop with finer interval
j = j - interval
interval = 20
while j < vector[0, maxx]:
    endargs = np.argwhere(vector[0] == j)
    endpoint1 = vector[1, endargs[0]]
    endpoint2 = vector[1, endargs[-1]]
    xupper.append(j)
    yupper.append(endpoint1[0])
    xlower.append(j)
    ylower.append(endpoint2[0])
    j = j + interval

# make one array of separate lists
ylower.reverse()
xlower.reverse()
xupper.extend(xlower)
yupper.extend(ylower)
shape = np.array([xupper, yupper])

# Scale and relocate
ydist = shape[1, 0] - shape[1, -1]
factor = ydist / 300
shape = shape / factor
xdist = shape[0, 0]
shape[0] = np.add(shape[0], np.full(np.shape(shape[0]), -xdist))
ydist = 150 - shape[1, 0]
shape[1] = np.add(shape[1], np.full(np.shape(shape[1]), ydist))

cv2.imshow('G19', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.plot(vector[0], vector[1], 'yx')
# plt.plot(cutoff[0],cutoff[1])
plt.plot(new_vector[0], new_vector[1], 'b+')
plt.grid()
plt.plot(shape[0], shape[1])
plt.show()

# output
f = open("G19_contour.txt", "w")  # Open file for writing
for i in range(len(shape[0])):
    line = str(shape[0, i]) + '\t' + str(shape[1, i]) + '\n'
    f.write(line)
f.close()
