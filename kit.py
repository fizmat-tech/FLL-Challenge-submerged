from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
rightHand = Motor(Port.A)
leftHand = Motor(Port.B)
leftMotor = Motor(Port.E, positive_direction=Direction.COUNTERCLOCKWISE, reset_angle=True)
rightMotor = Motor(Port.F, positive_direction=Direction.CLOCKWISE, reset_angle=True)

base = DriveBase(leftMotor,rightMotor, 56, 111)
base.use_gyro(True)
base.settings(900, 660, 800, 300)

base.straight(-730)
base.turn(45)
base.straight(-190)
leftHand.run_angle(1000, 600)
leftHand.run_angle(1000, -50)
leftHand.run_angle(1000, 300)




'''
base.straight(370, then=Stop.BRAKE)
base.straight(-500, then=Stop.BRAKE)
'''

