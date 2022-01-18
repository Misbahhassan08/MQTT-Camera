import time
import json
import os
import paho.mqtt.client as mqtt
from PIL import Image
from helpers import capture_pil,get_now_string,pil_to_base64
from PyQt5.QtCore import QThread, pyqtSignal
from config import server, RPI_ID, global_topic, pub_topic, sub_topic, path, ROOT
from Database import Database

class Pub(QThread):
    signal_loadImages = pyqtSignal(str,  name='m_signals')
    def __init__(self, ID, server, port) :
        QThread.__init__(self)
        self.clientMqtt = mqtt.Client()  
        self.clientMqtt.connect(server, port, 60)  # Connecting Sub to mosquitto
        self.payload = None  # payload Variable
        self.topic = pub_topic # Topic Address Variable
        self.ID = ID
        
        self.db = Database()
        self.ROOT = ROOT
        self.path = path
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
        pass
    
    def messageToTopic(self,params):
        img = capture_pil(params['params'])
        b64_img = pil_to_base64(img)
        output = {
            'data_type' : 'ReposeImage',
            'image' : b64_img,
            'RPI_ID' : f'RPI{self.ID}',
            'params' : params
            }
        _topic_id = params['RPI_ID']
        _topic = f'{global_topic}{RPI}{_topic_id}'
        (rc, mid) = self.clientMqtt.publish(_topic, output_json)  # publishing
        print(f'rc : {rc}, mid: {mid}')
        pass # end of messageToTopic(params) function
    
    def message(self, params, path):
        try:
            img = capture_pil(params)
            imageName = params['imageName']
            _format = params['raw']
            _time = str(params['time'])
            _imageName = f'RPI{self.ID}_{imageName}_{_time}.{_format}'
            img.save(f'{path}{_imageName}')
            #b64_img = pil_to_base64(img, params)
            result = self.db.add_entery(params)
            if result:
                print('DB save configurations')
            else:
                print('No Configurations saved Please check DB file')
            output = {
                'data_type':'image',
                'params':params,
                'RPI_ID': self.ID
                           }
            output_json = json.dumps(output)
            print(output_json)
            (rc, mid) = self.clientMqtt.publish(self.topic, output_json)  # publishing
            print(f'rc : {rc}, mid: {mid}')
            self.signal_loadImages.emit("LoadImages")
        except Exception as error:
            print(error)

        pass # end of message function

    
    pass # end of class 




