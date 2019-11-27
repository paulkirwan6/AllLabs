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

window_name = 'challenge 2'

cv2.imshow(window_name, image)
raw_key = cv2.waitKey(1000)
rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)


for x in range(0,320):
	for y in range(0,240):
		if ((x-100)^2+(y-24)^2)<16:
			rgb[x,y]=255,128,0



window_name2 = 'challenge 2 squares'
cv2.imshow(window_name2, rgb)
raw_key = cv2.waitKey(20000)
