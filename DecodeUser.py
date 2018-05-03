import binascii, random

class usercode:
    def __init__(self):
        return None
        
    def encode(self, String):
        a = binascii.b2a_hex(str.encode(String))
        b = int(a, 16)
        c = b + 123
        d = str(c)
        out = ''
        for i in range(len(d)):
            out += d[i]
            out += hex(random.randint(1,1000))[-1]
        return out
        
    def decode(self, String):
        c = ''
        for i in range(len(String)):
            if i%2 ==0:
                c += String[i]
        b = int(c) - 123
        b = int(b)
        a = hex(b).split('x')[-1]
        c = binascii.a2b_hex(a)
        return c.decode()