import cv2
import os
from piracer.cameras import Camera, MonochromeCamera

if __name__ == '__main__':
    camera = Camera()
    image = camera.read_image()

    cv2.imwrite('image.png', image)
    cv2.waitKey(0)



