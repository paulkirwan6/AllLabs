#USING PYTHON 2 and NOT PYTHON 3
from sense_hat import SenseHat

sense = SenseHat()
temperature = sense.get_temperature()
humidity = sense.get_humidity()
# temperature = 100
# humidity = 12
print " Temperature:", temperature, "*C", "\n", "Humidity:", humidity, "rH"

## 3 decimal places to capture full resolution of temperature and humidity. 