import json
import time
import paho.mqtt.client as mqtt
from helpers import get_now_string,base64_to_pil

class Sub:
    def __init__(self) :
        self.clientMqtt = mqtt.Client()  # Sub is for Payload
        self.clientMqtt.connect("test.mosquitto.org", 1883, 60)  # Connecting Sub to mosquitto
        self.payload = None  # payload Variable
        self.topic = "pro1/rpi/#"  # Topic Address Variable

        # --------- Initialize the Sub functions with proper function explain
        self.clientMqtt.on_message = self.on_message
        self.clientMqtt.on_connect = self.on_connect
        self.clientMqtt.on_subscribe = self.on_subscribe
        self.clientMqtt.max_queued_messages_set(1)
        self.clientMqtt.subscribe(self.topic, 1)
        time.sleep(4)
        self.clientMqtt.loop_start()
        # -- Test Print to check whole Neuron works perfectly fine
        #print("All Done")
        pass

    def on_message(self, mqttc, obj, msg):

        now = get_now_string()
        print("message on " + str(msg.topic) + f" at {now}")

        try:
            image_base64 = json.loads(msg.payload)
            image = base64_to_pil(image_base64)
            #image = image.convert("RGB")

            save_file_path = "test.png"
            image.save(save_file_path)
            print(f"Saved {save_file_path}")

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




