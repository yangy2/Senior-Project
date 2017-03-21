import time
import almath
import argparse
from naoqi import ALProxy

NAO_IP = "192.168.1.100"
NAO_Port = 9559

motionProxy = ALProxy("ALMotion", NAO_IP, NAO_Port)
postureProxy = ALProxy("ALRobotPosture", NAO_IP, NAO_Port)

motionProxy.rest
###IT APPEARS THAT SETTING STIFFNESS DOES NOT IMPACT NAO
###AS LONG AS STIFFNESS IS NOT 0.0 (CAN'T MOVE)
motionProxy.setStiffnesses("Head", 1.0)

# Simple command for the HeadYaw joint at 25% max speed
names            = "HeadYaw"
angles           = 0.0*almath.TO_RAD
fractionMaxSpeed = 0.25

motionProxy.setAngles(names,angles,fractionMaxSpeed)
time.sleep(1.0)

#motionProxy.setStiffnesses("Head", 0.0)

motionProxy.setStiffnesses("LArm", 1.0)

names            = "LShoulderRoll"
angles           = 100.0*almath.TO_RAD
fractionMaxSpeed = 0.25

motionProxy.setAngles(names,angles,fractionMaxSpeed)
time.sleep(0.2)

#motionProxy.setStiffnesses("LArm", 0.0)

motionProxy.setStiffnesses("LArm", 1.0)

names            = "LShoulderPitch"
angles           = 90.0*almath.TO_RAD
fractionMaxSpeed = 0.25

motionProxy.setAngles(names,angles,fractionMaxSpeed)
time.sleep(1.0)

motionProxy.setStiffnesses("LArm", 0.0)

print("Done")
