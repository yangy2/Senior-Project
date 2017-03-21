from naoqi import ALProxy
import serial

#Movement is in meters, Rotation is in radians
#Positive values are forward/left/c-clkwise
#Negative values are backward/right/clkwise

NAO_IP = "192.168.1.100"
NAO_Port = 9559

##Attempt to create proxy object from ALMotion Module from Naoqi OS
try:
    motion = ALProxy("ALMotion", NAO_IP, NAO_Port) #(Module, Robot, Robot Port)
except Exception, e:
    print "Could not create proxy to ALMotion"
    print "Error was: ", e

##Attempt to create proxy object from ALTextToSpeech Module from Naoqi OS
try:
    tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_Port) #(Module, Robot, Robot Port)
except Exception, e:
    print "Could not create proxy to ALMemory"
    print "Error was: ", e

    
port = 'COM10' #Subject to change
baudrate = 9600

arduino = serial.Serial(port, baudrate)

while True:
    data = arduino.readline()[:-2]
    if data:
        if data == "f":
            print data
            motion.post.moveTo(1.0, 0, 0)
            #tts.say("Forward")

        elif data == "b":
            print data
            motion.post.moveTo(-1.0, 0, 0)
            #tts.say("Backward")

        elif data == "l":
            print data
            motion.post.moveTo(0, 1.0, 0)
            #tts.say("Left")

        elif data == "r":
            print data
            motion.post.moveTo(0, -1.0, 0)
            #tts.say("Right")

        elif data == "s":
            print data
            motion.post.stopMove()
            #tts.say("Stop")
            
        elif data == "c":
            print data
            motion.post.moveTo(0, 0, -0.79)
            #tts.say("Clockwise")

        elif data == "k":
            print data
            motion.post.moveTo(0, 0, 0.79)
            #tts.say("Counter Clockwise")
