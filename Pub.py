import time
import json
import paho.mqtt.client as mqtt
from PIL import Image
from helpers import capture_pil,get_now_string,pil_to_base64


class Pub:
    def __init__(self, ID, server, port) :
        self.clientMqtt = mqtt.Client()  
        self.clientMqtt.connect(server, port, 60)  # Connecting Sub to mosquitto
        self.payload = None  # payload Variable
        self.topic = "pro1/rpi/RPI{}".format(ID)  # Topic Address Variable

        # --------- Initialize the Sub functions with proper function explain
        self.clientMqtt.on_connect = self.on_connect
        self.clientMqtt.on_publish = self.on_publish
        #self.clientMqtt.max_queued_messages_set(1)
        pass
    
    # ---------------- When paho is publish---------------------------
    def on_publish(self, mqttc, obj, mid):
        print("mid: " + str(mid))


    # --------- When  clientMqtt is connected
    def on_connect(self, mqttc, obj, flags, rc):
        print(" Client is connected and rc: " + str(rc))

    
    def message(self, params, path):
        try:
            img = capture_pil(params)
            imageName = params['imageName']
            _format = params['raw']
            img.save(f'{path}{imageName}.{_format}')
            b64_img = pil_to_base64(img, params)
            output_json = json.dumps(b64_img)
            (rc, mid) = self.clientMqtt.publish(self.topic, output_json)  # publishing
            print(f'rc : {rc}, mid: {mid}')
        except Exception as error:
            print(error)

        pass

    
    pass # end of class 




