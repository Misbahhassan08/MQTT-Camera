import time
import json
import os
import paho.mqtt.client as mqtt
from PIL import Image
from helpers import capture_pil,get_now_string,pil_to_base64
from PyQt5.QtCore import QThread, pyqtSignal

class Pub(QThread):
    signal_pub = pyqtSignal(str,  name='m_signals')
    signal_shoot = pyqtSignal(str,  name='m_signals')
    def __init__(self, ID, server, port) :
        QThread.__init__(self)
        self.clientMqtt = mqtt.Client()  
        self.clientMqtt.connect(server, port, 60)  # Connecting Sub to mosquitto
        self.payload = None  # payload Variable
        self.topic = "pro1/rpi/RPI{}".format(ID)  # Topic Address Variable
        self.ID = ID
        self.ROOT = os.getcwd()
        self.path = f'{self.ROOT}/Images/'
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
    
    def messageToTopic(params):
        #b64_img = pil_to_base64(img, params['params'])
        print('message to topic is ',params)
        pass # end of messageToTopic(params) function
    
    def message(self,_from, params, path):
        if _from == 'fromMain':
            try:
                img = capture_pil(params)
                imageName = params['imageName']
                _format = params['raw']
                _time = params['time']
                _imageName = f'RPI{self.ID}_{imageName}_{time}.{_format}'
                img.save(f'{path}{_imageName}')
                #b64_img = pil_to_base64(img, params)
                # save configurations in DB  (pending)
                output = {
                    'data_type':'image',
                    'params':params,
                    'RPI_ID': self.ID
                               }
                output_json = json.dumps(output)
                print(output_json)
                (rc, mid) = self.clientMqtt.publish(self.topic, output_json)  # publishing
                print(f'rc : {rc}, mid: {mid}')
            except Exception as error:
                print(error)
        elif _from == 'fromSub':
            
            pass
        elif _from == 'toTopic': # get trigger from other RPI , get the ID of rpi and then send shoot
            try:
                # {'data_type':'feedback','imageName':data['_in'],'sender':self.ID, 'topic':msg.topic}
                output = josn.loads(params)
                new_topic = str(output['topic'])
                output_json = json.dumps(output)
                (rc, mid) = self.clientMqtt.publish(new_topic, output_json)  # publishing
                print(f'rc : {rc}, mid: {mid}')
                pass
            except Exception as error:
                print('ERROR : in Publish function of :fromSub: ',error)
                pass
            pass
        self.signal_pub.emit(str(self.path))
        

        pass

    
    pass # end of class 





