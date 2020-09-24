import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect('localhost', 2666)

def on_connect(client, userdata, flags, rc):
    print("Connected")
    client.subscribe("chatSub")

def on_message(client, userdata, message):
    #print(message.payload.decode("utf-8"))
    #print("recieved")
    client.publish("chatPub", "Recieved")


client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()
#client.publish()
    
