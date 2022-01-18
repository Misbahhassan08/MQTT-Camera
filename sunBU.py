import json
import time
import paho.mqtt.client as mqtt
from helpers import get_now_string,base64_to_pil
import os
from PyQt5.QtCore import QThread, pyqtSignal

class Sub(QThread):
    signal_sub = pyqtSignal(str,  name='m_signals')
    signal_log = pyqtSignal(str,  name='m_signals')
    def __init__(self, server , port ,path, ID) :
        QThread.__init__(self)
        self.clientMqtt = mqtt.Client()  # Sub is for Payload
        self.clientMqtt.connect(server, port, 60) #Connecting Sub to mosquitto
        self.payload = None  # payload Variable
        self.topic = "pro1/rpi/#"  # Topic Address Variable
        self.path = path
        self.ID = ID
        self.new_mesg = False
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
        now = get_now_string()
        print("message on " + str(msg.topic) + f" at {now}")
        self.new_mesg = True
        try:
            
            data = json.loads(msg.payload)
            if data['data_type'] == 'image':
                image_base64 = data['image']
                image = base64_to_pil(image_base64)
                #image = image.convert("RGB")
                rpi_id = data['RPI_ID']
                if rpi_id == self.ID:
                    # save file in images
                    _in = '{}.{}'.format(data['image_name'], data['format'])
                    save_file_path = f'Images/{_in}'
                    image.save(save_file_path)
                    print(f"Saved {save_file_path}")
                else:
                    if not os.path.exists(f'RPI{rpi_id}'):
                        os.makedirs(f'RPI{rpi_id}')
                    _in = '{}.{}'.format(data['image_name'], data['format'])
                    save_file_path = f'RPI{rpi_id}/{_in}'
                    image.save(save_file_path)
                    print(f"Saved {save_file_path}")
                    self.signal_sub.emit('{"data_type":"feedback","imageName":'+data['_in']+',"sender":'+self.ID+', "topic":'+msg.topic+'}')
            elif data['data_type'] == 'feedback':
                print('feedback from another device')
                # {'data_type':'feedback','imageName':data['_in'],'sender':self.ID, 'topic':msg.topic}
                _imgName = data['imageName']
                __id = data['sender']
                _sender = f'RPI{__id}'
                new_output = '{"imgName":'+_imgName+', "RPI": '+_sender+'}'
                self.signal_log.emit(new_output)
                
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





