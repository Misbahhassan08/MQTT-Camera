import picamera

from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.start_preview()
sleep(5)
camera.capture('test.png')
camera.stop_preview()
