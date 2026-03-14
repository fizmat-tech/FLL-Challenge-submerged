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

base.straight(-660)
base.turn(35)
base.straight(-115)
base.turn(-115)
rightHand.run_angle(1000,500)
base.turn(-12)
base.straight(-800)
base.turn(58)
base.straight(-185)
base.turn(-75)
base.straight(-150)
base.curve(-390,50)
base.straight(-600)


'''
base.turn(-40)
base.straight(-300)
base.turn(50)
base.straight(-405)
base.turn(20)
base.straight(-115)
base.turn(57)
redmotor.run_angle(1000,500)
base.straight(570)
base.turn(90)
base.straight(-25)
base.turn(100)
base.straight(-350)
redmotor.run_angle(1000,-500)
base.curve(-390,85)
base.straight(-400)
'''
