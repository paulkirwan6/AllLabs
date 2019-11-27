#
# Simple websocket server that waits for connections from clients
# and then streams accelerometer readings from SenseHat sensor
# to the client.
#

##modify the code in the python websocket server to measure how many updates per second are being served

from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
# from sense_hat import SenseHat

##importing time
import time


global count
count = 0
global timer
timer = time.time()
timerold = timer -2


class SimpleIMU(WebSocket):

    def handleMessage(self) :
        print ('incoming message')

    def handleConnected(self):
        print(self.address, 'connected')

    def handleMessage(self) :
        print ('incoming message')

    def handleClose(self):
        print(self.address, 'closed')


#
# program starts here
#

# Start server on port 9001
server = SimpleWebSocketServer('', 9001, SimpleIMU)
# sense = SenseHat()
while True :

    # x,y,z in 'g' units (range of x,y,z when not accelerating: -1 to 1 due to gravity)
    # acceleration = sense.get_accelerometer_raw()
    # x = acceleration['x']
    # y = acceleration['y']
    # z = acceleration['z']
    x = 1
    y = 2
    z = 3

    # display red ball on LED 8x8 matrix
    led_x = int(3+x*16+0.5)
    led_y = int(3+y*16+0.5)
    if (led_x < 0) :
        led_x = 0
    if (led_x > 7) :
        led_x = 7
    if (led_y < 0) :
        led_y = 0
    if (led_y > 7) :
        led_y = 7
    # clear all LEDs
    # sense.clear()
    # set red pixel (red is RGB values 255,0,0)
    # sense.set_pixel(int(led_x),int(led_y),255,0,0)

    # construct JSON message
    message = "\"x\":{}, \"y\":{}, \"z\":{}".format(x, y, z) 
    # broadcast accelerometer to all connected clients
    for client in server.connections.itervalues():
        if client.handshaked :
            count = count + 1
            timer = time.time()
            if (timer - timerold)  >  1:
                print(count)
                timerold = time.time()
                count = 0
           #print ('sending ', message , ' to ' , client.address[0], count)
            #if(time.clock() - timer == 1)
            #	print(count)
             #   timer = time.clock()
            client.sendMessage(u'{' + str(message) + u'}')

    # call this once per main loop iteration for websocket server housekeeping
    server.serveonce()

