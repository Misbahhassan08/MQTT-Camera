import json
import time
import paho.mqtt.client as mqtt
from helpers import get_now_string,base64_to_pil
import os
from PyQt5.QtCore import QThread, pyqtSignal
from config import server, RPI_ID, global_topic, pub_topic, sub_topic, path, ROOT

class Sub(QThread):
    signal_sub = pyqtSignal(str,  name='m_signals')
    signal_log = pyqtSignal(str,  name='m_signals')
    def __init__(self, server , port ,path, ID) :
        QThread.__init__(self)
        self.clientMqtt = mqtt.Client()  # Sub is for Payload
        self.clientMqtt.connect(server, port, 60) #Connecting Sub to mosquitto
        self.payload = None  # payload Variable
        self.topic = sub_topic  # Topic Address Variable
        self.path = path
        self.ID = ID
        self.new_mesg = False
        self.ROOT = os.getcwd()
        # --------- Initialize the Sub functions with proper function explain
        self.clientMqtt.on_message = self.on_message
        self.clientMqtt.on_connect = self.on_connect
        self.clientMqtt.on_subscribe = self.on_subscribe
        #self.clientMqtt.max_queued_messages_set(1)
        self.clientMqtt.subscribe(self.topic, 1)
        time.sleep(4)
        self.clientMqtt.loop_start()
        # -- Test Print to check whole Neuron works perfectly fine
        #print("All Done")
        pass

    
    def on_message(self, mqttc, obj, msg):

        if msg.topic == f'{global_topic}RPI{self.ID}':
            print('receiving mesg from itself')
            pass
        else:
            
            now = get_now_string()
            print("message on " + str(msg.topic) + f" at {now}")
            self.new_mesg = True
            try:
                data = json.loads(msg.payload)
                if data['data_type'] == 'ReposeImage':
                    res_rpi = data['RPI_ID']
                    res_rpi_name = f'RPI{res_rpi}'
                    path = f'{self.ROOT}/{res_rpi_name}'
                    img = data['image']
                    image = base64_to_pil(img)
                    image_name = '{}_{}_{}.{}'.format(res_rpi_name,data['params']['imageName'],data['params']['time'],data['params']['raw'])
                    if not os.path.exist(path):
                        os.makedires(path)
                    save_file = f'{path}/{image_name}'
                    image.save(save_file)
                    # trigger log (################ pending )
                    self.signal_log.emit(f'{image_name} downloaded')
                    pass
                elif data['data_type'] == 'image':
                    # send image to publisher
                    self.signal_sub.emit(msg.payload)
                    pass
            except Exception as exc:
                print(exc)


    # --------- When  clientMqtt is connected
    def on_connect(self, mqttc, obj, flags, rc):
        print(" Client is connected and rc: " + str(rc))


    # ---------- When clientMqtt is Subscribed
    def on_subscribe(self, mqttc, obj, mid, granted_qos):
        #print(" Client is Subscribed: " + str(mid) + " " + str(granted_qos) + " " + str(obj) + " " + str(mqttc))
        pass


    
    pass # end of class 




