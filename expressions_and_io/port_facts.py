# RFC 9293: TCP header Source Port and Destination Port are 16 bits
# RFC 791: Addresses are fixed length of four octets (32 bits)

PORT_BITS = 16
IP_BITS = 32

num_ports = 2 ** PORT_BITS
max_port = 2 ** PORT_BITS - 1
num_ipv4 = 2 ** IP_BITS

print(f"Number of possible port numbers: {num_ports}")
print(f"Highest port number: {max_port}")
print(f"Number of possible IPv4 addresses: {num_ipv4}")