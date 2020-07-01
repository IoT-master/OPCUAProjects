from time import sleep

from opcua import Client

client = Client('opc.tcp://localhost:4840')
client.connect()
root = client.get_root_node()
print("Root node is: {:s} ".format(str(root)))
print(root)
object_node = client.get_objects_node()
for node in object_node.get_children():
    print(node.get_display_name())
print(object_node.get_children()[1].get_children()[0])
print(object_node.get_children()[1].get_children()[0].get_display_name())
while True:
    print(object_node.get_children()[1].get_children()[0].get_value())
    sleep(2)

