from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()


from pybricks.tools import hub_menu


selected = hub_menu('1', '2', '3', '4', '5', '6', '7', '8',)

if selected == '1':
    import osminog1
if selected == '2':
    import sborka
if selected == '3':
    import skubaChest
if selected == '4':
    import a
if selected == '5':
    import a
if selected == '6':
    import lodka
if selected == '7':
    import a
if selected == '8':
    import a
