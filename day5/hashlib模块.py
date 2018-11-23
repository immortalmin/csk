#Author:immortal luo
# -*-coding:utf-8 -*-
import hashlib
import hmac

# m = hashlib.md5()
# m.update(b"Hello")
# print(m.hexdigest())#十六进制
# m.update(b"It's me")
# m.update("陈".encode(encoding="utf-8"))
# print(m.digest())
# m.update

h = hmac.new(b"csk",b"lmm")
print(h.hexdigest())