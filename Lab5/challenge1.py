import numpy
import PIL
import math
import time
import picamera
import numpy as np
import cv2
import matplotlib as plt
import io

stream=io.BytesIO()
with picamera.PiCamera() as camera:
	camera.resolution=(320,240)
	camera.framerate=24
	time.sleep(1)
	camera.capture(stream,format='jpeg')
data=np.fromstring(stream.getvalue(),dtype=np.uint8)
image=cv2.imdecode(data,1)

window_name = 'challenge 1'

cv2.imshow(window_name, image)
raw_key = cv2.waitKey(1000)
rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)


for x in range(120,128):
	for y in range(64,72):
		rgb[x,y]=255,128,0


window_name2 = 'challenge 1 orange square'
cv2.imshow(window_name2, rgb)
raw_key = cv2.waitKey(5000)

rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

image2=make_squareSquare(rgb,[10,10],10,[255,255,255])
image3=make_square(image2,[100,100],15,[20,255,255])
image4=make_square(image3,[50,50],20,[255,0,255])

window_name2 = 'challenge 1 squares'
cv2.imshow(window_name2, image4)
raw_key = cv2.waitKey(20000)

def make_square(img,upper_left,size,colour):

	for x in range(upperLeft[0],upperLeft[0]+size):
		for y in range(upperLeft[1],upperLeft[1]+size):
			img[x,y]=colour
	return img