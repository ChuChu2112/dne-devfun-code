import json

with open("iosxe_data.json", "r") as file:      #reads the iosxe_data file in the same folder as this script and converts it to python
    file = file.read()
    iosxeInterfaces = json.loads(file)
    
    #print(len(iosxeInterfaces["ietf-interfaces:interfaces"]["interface"][0]["ietf-ip:ipv4"]))      #prints the length of the indexed data structure

    for interface in iosxeInterfaces["ietf-interfaces:interfaces"]["interface"]:        #runs through the python file at the specified index level to extract specific info. NOtice the conditionals
        if len(interface["ietf-ip:ipv4"]) == 0:
            print(f'''Interface {interface["name"]}, currently with no IPv4 address, has a description of "{interface["description"]}" and has an enabled status of "{interface["enabled"]}"''')
        else:
            print(f'''Interface {interface["name"]}, with IPv4 address and netmask of "{interface["ietf-ip:ipv4"]["address"][0]["ip"]} and {interface["ietf-ip:ipv4"]["address"][0]["netmask"]}" respectively , has a description of "{interface["description"]}" and has an enabled status of "{interface["enabled"]}"''')

        
        