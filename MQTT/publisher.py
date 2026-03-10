import paho.mqtt.client as mqtt

client = mqtt.Client()

client.connect("broker.hivemq.com",1883,60)

message = input("Enter message: ")

client.publish("home/test", message)

print("Message sent!")