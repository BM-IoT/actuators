import json
import paho.mqtt.client as mqtt
from playsound import playsound

def on_message(client, userdata, msg):
    print(f"Received msg from brain {msg.payload.decode()}")
    playsound("evac.mp3")

def warn_on_message(client, userdata, msg):
    print(f"Received msg from brain {msg.payload.decode()}")
    playsound("warn.mp3")

mqtt_evac = mqtt.Client()
mqtt_evac.on_message = on_message
mqtt_evac.user_data_set([])

mqtt_warn = mqtt.Client()
mqtt_warn.on_message = warn_on_message
mqtt_warn.user_data_set([])

mqtt_evac.connect("localhost", 1883, 60)
mqtt_evac.subscribe("actuator/evac")
mqtt_evac.loop_forever()

mqtt_warn.connect("localhost", 1883, 60)
mqtt_warn.subscribe("actuator/warn")
mqtt_warn.loop_forever()
