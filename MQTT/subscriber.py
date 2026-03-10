import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print("Received:", message.payload.decode())

client = mqtt.Client()

client.connect("broker.hivemq.com", 1883, 60)

client.subscribe("home/test")

client.on_message = on_message

print("Waiting for message...")

client.loop_forever()