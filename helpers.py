"""
Helper functions.
Source -> https://github.com/jrosebr1/imutils/blob/master/imutils/video/webcamvideostream.py
"""
import datetime
import base64
import time
from io import BytesIO
from PIL import Image
import picamera
from fractions import Fraction

DATETIME_STR_FORMAT = "%Y-%m-%d_%H:%M:%S.%f"


def get_now_string() -> str:
    return datetime.datetime.now().strftime(DATETIME_STR_FORMAT)

def base64_to_pil(image_base64):
    return Image.open(BytesIO(base64.b64decode(image_base64)))


def buffer_to_base64(image_buffer, encoding='utf-8'):
    return base64.b64encode(image_buffer.getvalue()).decode(encoding)

def pil_to_base64(image_pil, encoding='utf-8'):
    image_buffer = BytesIO()
    image_pil.save(image_buffer, format=params['raw'])
    return buffer_to_base64(image_buffer, encoding=encoding)

def capture_buffer(params):
    with picamera.PiCamera() as camera:
        
        camera.framerate=10#Fraction(1, 6)
        camera.shutter_speed = int(str(params['expose_time']))#*1000000#6000000
        camera.resolution= params['resolution']
        camera.iso = params['iso']
        camera.exposure_mode = params['exposure_mode']#'night'
        camera.awb_mode = params['white_balance']
        camera.brightness = params['brightness']
        camera.contrast = params['contrast']
        camera.saturation = params['saturation']
        camera.sharpness = params['sharpness']
        
        
        
        print(params)
        
        stream = BytesIO()
        
        camera.start_preview()

        try:
            
            camera.capture(stream, format=params['raw'])
            stream.seek(0)
        finally:
            camera.stop_preview()
            
        return stream

def capture_pil(params):
    return Image.open(capture_buffer(params))