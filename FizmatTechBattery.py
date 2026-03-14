from pybricks.hubs import PrimeHub
from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color, Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = PrimeHub()

battery_voltage = hub.battery.voltage()

full_voltage = 8200
empty_voltage = 6500

battery_percentage = ((battery_voltage - empty_voltage) / (full_voltage - empty_voltage)) * 100

battery_percentage = max(0, min(100, battery_percentage))

print(f"Уровень заряда батареи: {round(battery_percentage)}%")
hub.display.number(round(battery_percentage))
wait(1000)