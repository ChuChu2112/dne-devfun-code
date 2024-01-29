import json
import os

with open("interface-config.json", "r") as file:
    interfaceConfigStr = file.read()
    interfaceConfigDat = json.loads(interfaceConfigStr)
    print(interfaceConfigStr)
    print("interfaceConfigStr is a ", type(interfaceConfigStr))
    print("interfaceConfigDat is a ", type(interfaceConfigDat))
    #print(interfaceConfigDat["ietf-interfaces:interface"]["description"])
    print("This interfaces' ip is", interfaceConfigDat["ietf-interfaces:interface"]["ietf-ip:ipv4"]["address"][0]["ip"])