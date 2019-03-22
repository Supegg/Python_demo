#!/usr/bin/env python

import rsa


# 生成密钥
(pubkey, privkey) = rsa.newkeys(1024)

# 保存密钥
with open('rsa-public.pem','w') as f:
    f.write(pubkey.save_pkcs1().decode())

with open('rsa-private.pem','w') as f:
    f.write(privkey.save_pkcs1().decode())


# 导入密钥
with open('rsa-public.pem','r') as f:
    pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())

with open('rsa-private.pem','r') as f:
    privkey = rsa.PrivateKey.load_pkcs1(f.read().encode())


#公钥加密，私钥解密
message = '这是商机：...'
crypto_email_text = rsa.encrypt(message.encode(), pubkey)
print('密文：\t', crypto_email_text)

message = rsa.decrypt(crypto_email_text, privkey).decode()
print(message)


#私钥签名，公钥验证
message = '这是重要指令：...'
crypto_email_text = rsa.sign(message.encode(), privkey, 'SHA-1')#'SHA-256'

#message='hack' + message
try:
    print(rsa.verify(message.encode(), crypto_email_text, pubkey))#return HASH-METHOD name if verified
    print(message)
except rsa.pkcs1.VerificationError as error:
    print(error)#rsa.pkcs1.VerificationError


#################################
#https://www.cnblogs.com/hhh5460/p/5243410.html