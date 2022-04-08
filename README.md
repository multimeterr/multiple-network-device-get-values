# multiple-network-device-get-values
Running multiple commands on multiple network devices and listing outputs on excel.

Change commands file with your commands comma seperated, same as device file. 
I didn't add multitasking because TACACS+ etc. auth servers won't allow you to connect so many device same time.

This code running with netmiko lib so you can run it on devices which library supports.
Username-password is not static for safety, basically it's cleartext. If you want to store username/password here you can change simply but not recommended.
