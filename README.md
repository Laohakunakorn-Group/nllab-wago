# nllab-wago
Control of solenoid valves using a Wago 750 PLC and Modbus

### Setting up Ethernet
Windows 10: Go to Control Panel, Network & Internet, Show available networks. Select the ethernet network (make sure you are connected to the internet through a different network) - you want the device to be on a separate subnet. Double click to open the Ethernet Status dialog box, then go to Properties, and Internet Protocol Version 4 (TCP/IPv4). Click Properties, and set the IP address to be 192.168.1.1, and the subnet mask to be 255.255.255.0. The first three elements must be the same as for the Wago controller.

Now set the DIP switch on Wago to be 11000000 (corresponding to the number 3, read in binary from right to left). This means that the Wago IP address is 192.168.1.3, and now the device and PC can talk to each other.
