from picamera import PiCamera
from Pub import Pub 
from Sub import Sub
import time
import json


RPI_ID = 1

pub = Pub(RPI_ID)
sub = Sub()

camera = PiCamera()


if __name__ == '__main__':
    
    while True:
        v = input("Enter C to Capture : ")
        if v == 'C' or v == 'c':
            pub.message(camera)
            time.sleep(4)
        pass
    pass # end of main 
