import cv2

img1 = cv2.imread('PROJECTS/photos/1.jpg', 0)
img2 = cv2.imread('PROJECTS/photos/2.jpg', 0)

height1, widht1 = img1.shape
height2, widht2 = img2.shape

for i in range(height1):
    for j in range(widht1):
        img1[i, j] = 255 - img1[i, j]

for i in range(height2):
    for j in range(widht2):
        img2[i, j] = 255 - img2[i, j]

cv2.imshow('image1', img1)
cv2.imshow('image2', img2)
cv2.waitKey()