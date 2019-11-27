from time import sleep
from sense_hat import SenseHat
#get_accelerometer_raw  gives x,y,z axis data
#dont forget to change the values for the if statements

sense = SenseHat()
green = (0,255,0)
yellow = (255,255,0)
red = (255,0,0)
sense.set_imu_config(False, False, True)
ref = sense.get_accelerometer_raw()
x = ref['x']
y = ref['y']
z = ref['z']

while True:
	cur = sense.get_accelerometer_raw()
	a = cur['x']
	b = cur['y']
	c = cur['z']

	difa = abs(x-a)
	difb = abs(y-b)
	difc = abs(z-c)

	if difa > 0.3 or difb > 0.3 or difc > 0.3:
		for i in range(50):
			sense.clear(yellow)
			cur = sense.get_accelerometer_raw()
		        a = cur['x']
		        b = cur['y']
		        c = cur['z']

		        difa = abs(x-a)
		        difb = abs(y-b)
        		difc = abs(z-c)

			if difa >0.5 or difb > 0.5 or difc > 0.5:
				break
			sleep(0.05)
			sense.clear()
			sleep(0.05)
	if difa > 0.5 or difb > 0.5 or difc > 0.5:
		for i in range(100):
			sense.clear(red)
			sleep(0.05)
			sense.clear()
			sleep(0.05)
	if difa < 0.3 or difb < 0.3 or difc < 0.3:
		sense.clear(green)
