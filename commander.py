from netmiko import ConnectHandler
import getpass
import pandas as pd


device_file = open("devices.txt", "r")
device_content = device_file.read()
device_content_list = device_content.split(",")
device_file.close()

command_file = open("command.txt", "r")
command_content = command_file.read()
command_content_list = command_content.split(",")
command_file.close()




username = input("Enter Username: ")
pswd = getpass.getpass()

import pandas as pd

for cmm in command_content_list:
    dict1 = {}
    for i in device_content_list:
            devices = [
            {
                    'device_type': 'cisco_xr',
                    'ip': i,
                    'username': username,
                    'password': pswd ,
                    'port': 22,
            },
            ]

            for device in devices:
                try:
                    print("Connected to the device:"+i)
                    net_connect = ConnectHandler(**device)
                    net_connect.send_command("terminal monitor disable")
                    outpt = net_connect.send_command_expect(cmm)
                    net_connect.disconnect()
                    print("Connection terminated.")
                    print("\n")
                    dict1[i] = outpt
                except:
                    print("Connection error: "+i)
                    dict1[i] = "Error"
    df = pd.DataFrame(data=dict1, index=[0])
    df = (df.T)
    print (df)
    df.to_excel(f'{cmm}-output.xlsx')
