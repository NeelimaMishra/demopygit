import re

fd = open('file.txt', 'r')
buffer = fd.read()
print(buffer)
ip_addr = re.findall(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}', buffer)
print(ip_addr)

#buffer = 'sdsdlfsdklkk 100.25.25.25 ksjfkdfj' ; output ip_addresses ['100.25.25.25']
#ip_addresses = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", buffer)

