import time
import thread
import almath
import argparse
import serial
from naoqi import ALProxy

NAO_IP = "192.168.1.100"
NAO_Port = 9559

##motionProxy = ALProxy("ALMotion", NAO_IP, NAO_Port)
##postureProxy = ALProxy("ALRobotPosture", NAO_IP, NAO_Port)
##tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_Port)
##
###IT APPEARS THAT SETTING STIFFNESS DOES NOT IMPACT NAO
###AS LONG AS STIFFNESS IS NOT 0.0 (DISABLED)
##
##MaxSpeed = 0.1 #From 0.0 to 1.0
##
###A NON-ZERO DELAY WILL NOT WORK IF AUTONOMOUS LIFE IS ON
##SleepTime = 0.2 #Seconds to wait
##
###TO DO: Include exception handling at some point if angle is out of bounds
##def move(part, x):
##    angle = x*almath.TO_RAD
##    motionProxy.setAngles(part, angle, MaxSpeed)
##    time.sleep(SleepTime)
##    print(x)
##    print(angle)
##
##motionProxy.setStiffnesses("LArm", 0.0)
##motionProxy.setStiffnesses("RArm", 0.0)
##motionProxy.setStiffnesses("Body", 1.0)
##
##move("LElbowRoll", 60)

port = 'COM10' #Subject to change
baudrate = 9600

arduino = serial.Serial(port, baudrate)

while True:
    data = arduino.readline()[:-2]
    if data:

        print(data.split(" ")[0])
        print(data.split(" ")[1])
        print(data.split(" ")[2])
        print(data.split(" ")[3])

        #NOTE: If mirroring motion from one arm to the other, multiply roll and yaw by -1
        thread.start_new_thread(move, ("LShoulderPitch", data.split(" ")[0]))
        thread.start_new_thread(move, ("LShoulderRoll", data.split(" ")[1]))
        thread.start_new_thread(move, ("LElbowRoll", data.split(" ")[2]))
        thread.start_new_thread(move, ("LWristYaw", data.split(" ")[3]))
