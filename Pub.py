import paho.mqtt.client as mqtt
client = mqtt.Client("test")
client.connect('localhost', 2666)
client.subscribe("chatPub")

def on_message(client, userdata, message):
    print(message.payload.decode())

client.on_message = on_message
client.loop_start()
while True: 
    client.publish("chatSub" , input("message: "))