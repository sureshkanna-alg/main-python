import random

s = "abcdefghijklmnowxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = int(input("VALUE: "))
p =  "".join(random.sample(s,passlen ))
print(p)
