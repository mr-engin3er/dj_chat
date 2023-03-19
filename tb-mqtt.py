import logging
import time
from tb_device_mqtt import TBDeviceMqttClient


def on_attributes_change(client, result, exception):
    if exception is not None:
        print("Exception: " + str(exception))
    else:
        print(result)


client = TBDeviceMqttClient("146.56.48.170", "pQpHufkkwE3uxUkaUMfl")
print("connecting")
client.connect()
print("client connected")

# print('Requesting old data')
# client.request_attributes(
#     client_keys=["Monday", ], shared_keys=["22-10-2021", ], callback=on_attributes_change)

time.sleep(1)
print('Subscribing to attributes')

# sub1 = client.subscribe_to_attribute(
#     "v1/devices/me/attributes", callback=on_attributes_change)
req = client.subscribe_to_attribute(
    "v1/devices/me/rpc/request/+", callback=on_attributes_change)
client.publish_data('{"clientKeys":"isPaused,attribute2", "sharedKeys":"22-10-2021,isPaused"}',
                    f'v1/devices/me/rpc/response/{req}', 1)
# client.subscribe_to_all_attributes(callback=on_attributes_change)

while True:
    time.sleep(1)

client.disconnect()
