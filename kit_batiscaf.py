from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
rightHand = Motor(Port.A,positive_direction=Direction.COUNTERCLOCKWISE)
leftHand = Motor(Port.B,positive_direction=Direction.COUNTERCLOCKWISE)
leftMotor = Motor(Port.E, positive_direction=Direction.COUNTERCLOCKWISE, reset_angle=True)
rightMotor = Motor(Port.F, positive_direction=Direction.CLOCKWISE, reset_angle=True)

base = DriveBase(leftMotor,rightMotor, 56, 111)
base.use_gyro(True)
base.settings(1000, 660, 800, 300)

bluemotor.run_angle(1000,350, then=Stop.HOLD)
base.straight(612, then=Stop.BRAKE, wait=True)
base.turn(78)
base.straight(328, then=Stop.BRAKE, wait=True)
bluemotor.run_angle(1000,-330,then=Stop.HOLD)
bluemotor.run_angle(1000,330)
base.straight(10, then=Stop.BRAKE, wait=True)
base.straight(-180, then=Stop.BRAKE, wait=True)
base.turn(50)
base.straight(-375, then=Stop.BRAKE, wait=True)
redmotor.run_angle(1000,280)
base.turn(55)
base.straight(-380, then=Stop.BRAKE, wait=True)
base.straight(200)

