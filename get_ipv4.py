import os
import re

f = os.popen("ipconfig")
data = f.read()
f.close()
ips = re.findall(r"IPv4 Address.*\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", data)
print ips[0].split()[-1]
