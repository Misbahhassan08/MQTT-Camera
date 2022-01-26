import time
import json
import os
import paho.mqtt.client as mqtt
from PIL import Image
from helpers import capture_pil,get_now_string,pil_to_base64, base64_to_pil
from PyQt5.QtCore import QThread, pyqtSignal
from config import server,port, RPI_ID, global_topic, pub_topic, sub_topic, path, ROOT
from Database import Database

class Pub(QThread):
    signal_loadImages = pyqtSignal(str,  name='m_signals3')
    signal_log = pyqtSignal(str,  name='m_signals2')
    def __init__(self) :
        QThread.__init__(self)
        self.clientMqtt = mqtt.Client(f"RPI{RPI_ID}")  
        self.clientMqtt.connect(server, port, 10)  # Connecting Sub to mosquitto
        
        self.db = Database()
        # --------- Initialize the Sub functions with proper function explain
        self.clientMqtt.on_connect = self.on_connect
        self.clientMqtt.on_publish = self.on_publish
        #self.clientMqtt.max_queued_messages_set(1)
        
        self.new_mesg = False
        self.ROOT = os.getcwd()
        # --------- Initialize the Sub functions with proper function explain
        self.clientMqtt.on_message = self.on_message
        self.clientMqtt.on_subscribe = self.on_subscribe
        self.clientMqtt.max_queued_messages_set(1)
        self.clientMqtt.subscribe(sub_topic, 1)
        time.sleep(4)
        self.clientMqtt.loop_start()
        pass
    
    # when client get published message
    def on_message(self, mqttc, obj, msg):

        if msg.topic == f'{global_topic}RPI{RPI_ID}':
            print('receiving mesg from itself')
            pass
        else:
            
            now = get_now_string()
            print("message on " + str(msg.topic) + f" at {now}")
            self.new_mesg = True
            try:
                data = json.loads(msg.payload)
                
                if data['data_type'] == 'ReposeImage':
                    if data['SERVER_RPI_ID'] == f'RPI{RPI_ID}':
                        res_rpi = data['CLIENT_RPI_ID']
                        res_rpi_name = f'{res_rpi}'
                        path = f"{self.ROOT}/{data['imageName']}_{data['time']}"#{res_rpi_name}'
                        img = data['image']
                        image = base64_to_pil(img)
                        image_name = '{}_{}_{}.{}'.format(res_rpi_name,data['imageName'],data['time'],data['raw'])
                        if not os.path.exists(path):
                            os.makedirs(path)
                        save_file = f'{path}/{image_name}'
                        image.save(save_file)
                        # trigger log (################ pending )
                        self.signal_log.emit(f'{image_name} downloaded')
                    pass
                elif data['data_type'] == 'image':
                    # send image to publisher
                    self.messageToTopic(json.dumps(data))
                    pass
            except Exception as exc:
                print(exc)

    # ---------- When clientMqtt is Subscribed
    def on_subscribe(self, mqttc, obj, mid, granted_qos):
        #print(" Client is Subscribed: " + str(mid) + " " + str(granted_qos) + " " + str(obj) + " " + str(mqttc))
        pass

    # ---------------- When paho is publish---------------------------
    def on_publish(self, mqttc, obj, mid):
        print("mid: " + str(mid))


    # --------- When  clientMqtt is connected
    def on_connect(self, mqttc, obj, flags, rc):
        print(" Client is connected and rc: " + str(rc))
        pass
    
    def messageToTopic(self,params):
        params = json.loads(params)
        img = capture_pil(params['params'])
        b64_img = pil_to_base64(img, params)
        srpi = params['RPI_ID']
        output = {
            'data_type' : 'ReposeImage',
            'image' : b64_img,
            'CLIENT_RPI_ID' : f'RPI{RPI_ID}',
            'SERVER_RPI_ID' : f'RPI{srpi}',
            'imageName' : params['params']['imageName'],
            'time' : params['params']['time'],
            'raw': params['params']['raw']
            }
        _topic_id = params['RPI_ID']
        _topic = f'{global_topic}RPI{_topic_id}'
        output_json = json.dumps(output)
        (rc, mid) = self.clientMqtt.publish(pub_topic, output_json)  # publishing
        print(f'rc : {rc}, mid: {mid}')
        pass # end of messageToTopic(params) function
    
    def message(self, params, path):
        try:
            
            output = {
                'data_type':'image',
                'params':params,
                'RPI_ID': RPI_ID
                           }
            output_json = json.dumps(output)
            print(output_json)
            (rc, mid) = self.clientMqtt.publish(pub_topic, output_json)  # publishing
            print(f'rc : {rc}, mid: {mid}')
            
            
            _path = f"{ROOT}/{params['imageName']}_{params['time']}"
            
            img = capture_pil(params)
            imageName = params['imageName']
            _format = params['raw']
            _time = str(params['time'])
            _imageName = f'RPI{RPI_ID}_{imageName}_{_time}.{_format}'
            
            if not os.path.exists(_path):
                os.makedirs(_path)              
            img.save(f'{_path}/{_imageName}')
            
            if not os.path.exists(path):
                os.makedirs(path)              
            img.save(f'{path}/{_imageName}')
            
            #b64_img = pil_to_base64(img, params)
            #result = self.db.add_entery(params) # for adding every new entry
            result = self.db.update_entry(params) # for update only last entry
            if result:
                print('DB save configurations')
            else:
                print('No Configurations saved Please check DB file')
            
            self.signal_loadImages.emit("LoadImages")
        except Exception as error:
            print(error)

        pass # end of message function

    
    pass # end of class 




