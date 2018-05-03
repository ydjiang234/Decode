from DecodeUser import usercode

uc = usercode()
a = '1'
b = uc.encode(a)
c = uc.decode(b)
print(b)
print(c)