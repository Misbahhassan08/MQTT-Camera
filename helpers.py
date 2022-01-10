"""
Helper functions.
Source -> https://github.com/jrosebr1/imutils/blob/master/imutils/video/webcamvideostream.py
"""
import datetime
import base64
import datetime
from io import BytesIO
from PIL import Image

DATETIME_STR_FORMAT = "%Y-%m-%d_%H:%M:%S.%f"


def get_now_string() -> str:
    return datetime.datetime.now().strftime(DATETIME_STR_FORMAT)

def base64_to_pil(image_base64):
    return Image.open(BytesIO(base64.b64decode(image_base64)))


def buffer_to_base64(image_buffer, encoding='utf-8'):
    return base64.b64encode(image_buffer.getvalue()).decode(encoding)

def pil_to_base64(image_pil, encoding='utf-8', format='jpeg'):
    image_buffer = BytesIO()
    image_pil.save(image_buffer, format=format)
    return buffer_to_base64(image_buffer, encoding=encoding)

def capture_buffer(camera, format='jpeg'):
    
    stream = BytesIO()
    camera.capture(stream, format=format)
    stream.seek(0)
    return stream

def capture_pil(camera, format='jpeg'):
    return Image.open(capture_buffer(camera, format=format))