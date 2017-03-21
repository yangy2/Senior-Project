import time
import thread
import almath
import argparse
from naoqi import ALProxy

NAO_IP = "192.168.1.100"
NAO_Port = 9559

motionProxy = ALProxy("ALMotion", NAO_IP, NAO_Port)
postureProxy = ALProxy("ALRobotPosture", NAO_IP, NAO_Port)
tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_Port)

#motionProxy.rest
#IT APPEARS THAT SETTING STIFFNESS DOES NOT IMPACT NAO
#AS LONG AS STIFFNESS IS NOT 0.0 (DISABLED)

MaxSpeed = 0.1 #From 0.0 to 1.0
#A NON-ZERO DELAY WILL NOT WORK IF AUTONOMOUS LIFE IS ON
SleepTime = 0.0 #Seconds to wait

#Python Syntax
#xrange is inclusive for first parameter
#xrange is exclusive for second parameter


#TO DO:
#Change function parameter from self to angle variable
#Remove function for loop
#Create threads in while loop

class Yaw:
    def Wrist(self):
        #Wrist Yaw
        for x in xrange(-104, 105):
            WRangles = x*almath.TO_RAD
            motionProxy.setAngles("LWristYaw", WRangles, MaxSpeed)
            motionProxy.setAngles("RWristYaw", -WRangles, MaxSpeed)
            time.sleep(SleepTime)
            print(x)
            print(WRangles)

    def Elbow(self):
        #Elbow Yaw
        for x in xrange(-119, -120):
            ERangles = x*almath.TO_RAD
            motionProxy.setAngles("LElbowYaw", ERangles, MaxSpeed)
            motionProxy.setAngles("RElbowYaw", ERangles, MaxSpeed)
            time.sleep(SleepTime)
            print(x)
            print(ERangles)

class Roll:
    def Shoulder(self):
        #Shoulder Roll
        for x in xrange(-18, 77):
            SRangles = x*almath.TO_RAD
            motionProxy.setAngles("LShoulderRoll", SRangles, MaxSpeed)
            motionProxy.setAngles("RShoulderRoll", -SRangles, MaxSpeed)
            time.sleep(SleepTime)
            print(x)
            print(SRangles)

    def Elbow(self):
        #Elbow Roll
        for x in xrange(-88, -3):
            ERangles = x*almath.TO_RAD
            motionProxy.setAngles("LElbowRoll", ERangles, MaxSpeed)
            motionProxy.setAngles("RElbowRoll", -ERangles, MaxSpeed)
            time.sleep(SleepTime)
            print(x)
            print(ERangles)

class Pitch:
    def Shoulder(self):
        #Shoulder Pitch
        for x in xrange(-119, 120):
            SRangles = x*almath.TO_RAD
            motionProxy.setAngles("LShoulderPitch", SRangles, MaxSpeed)
            motionProxy.setAngles("RShoulderPitch", SRangles, MaxSpeed)
            time.sleep(SleepTime)
            print(x)
            print(SRangles)

def move(part, x):
#    for x in xrange(-18, 77):
        angle = x*almath.TO_RAD
        motionProxy.setAngles(part, angle, MaxSpeed)
        time.sleep(SleepTime)
        print(x)
        print(angle)

motionProxy.setStiffnesses("LArm", 0.0)
motionProxy.setStiffnesses("RArm", 0.0)
motionProxy.setStiffnesses("Body", 1.0)

roll = Roll()
pitch = Pitch()
yaw = Yaw()

move("LElbowRoll", 60)
data = "140 90 77 22"
print(data.split(" ")[0])
print(data.split(" ")[1])
print(data.split(" ")[2])
print(data.split(" ")[3])


##tts.say("Shoulder Roll")
##thread.start_new_thread(roll.Shoulder, ())
##
##tts.say("Elbow Roll")
##thread.start_new_thread(roll.Elbow, ())
##
##tts.say("Shoulder Pitch")
##thread.start_new_thread(pitch.Shoulder, ())
##
##tts.say("Wrist Yaw")
##thread.start_new_thread(yaw.Wrist, ())
##
###Doesn't appear to be working...
##tts.say("Elbow Yaw")
##thread.start_new_thread(yaw.Elbow, ())
##
##motionProxy.setStiffnesses("LArm", 0.0)
##motionProxy.setStiffnesses("RArm", 0.0)

print("Done")

##port = 'COM10' #Subject to change
##baudrate = 9600
##
##arduino = serial.Serial(port, baudrate)
##
##while True:
##    data = arduino.readline()[:-2]
##    if data:
##
##        print "Shoulder Pitch:", data.split(" ")[0]
##        print "Shoulder Roll:", data.split(" ")[1]
##        print "Elbow Roll:", data.split(" ")[2]
##        print "Wrist Yaw:", data.split(" ")[3]
##
##        move("LShoulderPitch", data.split(" ")[0])
##        move("LShoulderRoll", data.split(" ")[1])
##        move("LElbowRoll", data.split(" ")[2])
##        move("LWristYaw", data.split(" ")[3])
##
##        thread.start_new_thread(move, ("LShoulderPitch", data.split(" ")[0])
##
##        if data == "f":
##            print data
##            motion.post.moveTo(1.0, 0, 0)
##            #tts.say("Forward")
##
##        elif data == "b":
##            print data
##            motion.post.moveTo(-1.0, 0, 0)
##            #tts.say("Backward")
##
##        elif data == "l":
##            print data
##            motion.post.moveTo(0, 1.0, 0)
##            #tts.say("Left")
##
##        elif data == "r":
##            print data
##            motion.post.moveTo(0, -1.0, 0)
##            #tts.say("Right")
##
##        elif data == "s":
##            print data
##            motion.post.stopMove()
##            #tts.say("Stop")
##            
##        elif data == "c":
##            print data
##            motion.post.moveTo(0, 0, -0.79)
##            #tts.say("Clockwise")
##
##        elif data == "k":
##            print data
##            motion.post.moveTo(0, 0, 0.79)
##            #tts.say("Counter Clockwise")
##
