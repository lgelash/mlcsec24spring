# Assignment #1: Print Your Name
print("Levan")

# Assignment #2: Simple Math Operations:
a = 10
b = 5

c = a + b
d = a - b
e = a * b
f = a / b

print(c)
print(d)
print(e)
print(f)

# Assignment #3: Area of a Circle:
import math

radius = 10
area = math.pi * radius ** 2
print(area)

# Assignment #4: Convert Minutes to Seconds:

minutes = float(input("Enter the number of minutes: "))
seconds: minutes * 60
print(minutes, "minutes is equal to", minutes * 60, "seconds.")


# Assignment #5: Print IP addresses:

import ipaddress

network_address = "192.168.0.3/24"

network = ipaddress.IPv4Network(network_address, strict=False)

print("All IP addresses within the network:")
for ip_address in network:
    print(ip_address)