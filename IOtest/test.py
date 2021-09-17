from pymodbus.client.sync import ModbusTcpClient

client = ModbusTcpClient('192.168.1.3') # Set IP address here

# Write and read single coil
#client.write_coil(0, False)
#result = client.read_coils(512+0,1) # reading requires coil index to be shifted by 512
#print(result.bits[0])

# Write multiple coils
INPUT = '0000'+'0000'+'0000'+'0000'+'0000'+'0000'+'0000'+'0000'
for j in range(len(INPUT)):
    status = bool(int(INPUT[j]))
    client.write_coil(j, status)

# Read multiple coils
RESULT = ''
for j in range(32):
    status = client.read_coils(512+j,1)
    RESULT+=(str(int(status.bits[0])))
print(RESULT)