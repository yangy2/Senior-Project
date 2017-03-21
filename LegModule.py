from naoqi import ALProxy
import serial

NAO_IP = "192.168.1.100"
NAO_Port = 9559
##Attempt to create proxy object from ALMemory Module from Naoqi OS
try:
    memoryProxy = ALProxy("ALMemory", NAO_IP, NAO_Port) #(Module, Robot, Robot Port)
except Exception, e:
    print "Could not create proxy to ALMemory"
    print "Error was: ", e

##Attempt to create proxy object from ALTextToSpeech Module from Naoqi OS
try:
    tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_Port) #(Module, Robot, Robot Port)
except Exception, e:
    print "Could not create proxy to ALMemory"
    print "Error was: ", e

    
port = 'COM5' #Subject to change
baudrate = 9600

arduino = serial.Serial(port, baudrate)

while True:
    data = arduino.readline()[:-2]
    if data:
        print data
        tts.say(data)




