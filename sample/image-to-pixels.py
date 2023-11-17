import cv2
import numpy as np

imageFile = './image.png'
img = cv2.imread(imageFile, 1)
img_height, img_width, len = img.shape

size = 64

newImage = np.zeros((size, size, len), dtype=img.dtype)

new_height = img_height // size
new_width = img_width // size

for j in range(size):
    for i in range(size):
        y = j * new_height
        x = i * new_width
        pixel = img[y:y + new_height, x:x + new_width]
        for k in range(len):
            newImage[j,i,k] = cv2.mean(pixel)[k]

cv2.imshow('sample', cv2.resize(newImage, (640, 404)))
cv2.waitKey()
cv2.destroyAllWindows()
