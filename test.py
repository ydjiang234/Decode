from DecodeUser import usercode

uc = usercode()
a = ''
b = uc.encode(a)
c = uc.decode(b)
print(b)
print(c)
