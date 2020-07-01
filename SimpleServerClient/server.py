from random import randint

from opcua import Server

server = Server()
server.set_endpoint('opc.tcp://localhost:4840')
add_space = server.register_namespace("My Simulation")
node = server.get_objects_node()
param = node.add_object(add_space, "Parameters")
temp = param.add_variable(add_space, 'Temp', 0)
temp.set_writable()
server.start()

while True:
    temp.set_value(randint(0, 255))
