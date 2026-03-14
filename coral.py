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
base.settings(1000, 660, 800, 300)


base.turn(80)
base.straight(-640)
base.turn(-115)
redmotor.run_angle(1000,135)
base.straight(-200)
redmotor.run_angle(1000,-245)
redmotor.run_angle(1000,500)
base.straight(-150)
base.straight(100)
redmotor.run_angle(1000,-345)
base.turn(115)
base.straight(1000)






