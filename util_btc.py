import random
import ecdsa
import hashlib
import os
import base58


def base58CheckEncode(version, payload):
    '''
    生成wif格式密钥
    '''
    s = version + payload
    # print(s)
    checksum = hashlib.sha256(hashlib.sha256(
        bytes.fromhex(s)).digest()).digest()[0:4]
    result = bytes.fromhex(s + checksum.hex())
    return base58.b58encode(result).decode('ascii')


def privateKeyToPublicKey(s):
    '''
    input:hex私钥
    output:hex公钥
    '''
    sk = ecdsa.SigningKey.from_string(bytes.fromhex(s), curve=ecdsa.SECP256k1)
    return '04' + sk.verifying_key.to_string().hex().upper()


def pubKeyToAddr(s):
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(hashlib.sha256(bytes.fromhex(s)).digest())
    return base58CheckEncode('00', ripemd160.digest().hex())


if __name__ == "__main__":
    # 随机生成32bytes的hex私钥
    private_key = ''.join(['%x' % random.randrange(16) for x in range(0, 64)])
    print('pri', private_key)
    print('pub', privateKeyToPublicKey(private_key))

    print('-------------------')

    s = '0C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1D'
    print('pri', s)
    print('pri wif', base58CheckEncode('80', s) ==
          '5HueCGU8rMjxEXxiPuD5BDku4MkFqeZyd4dZ1jvhTVqvbTLvyTJ')

    print('-------------------')

    a = '18E14A7B6A307F426A94F8114701E7C8E774E7F9A47E2C2035DB29A206321725'
    s = '0450863AD64A87AE8A2FE83C1AF1A8403CB53F53E486D8511DAD8A04887E5B23522CD470243453A299FA9E77237716103ABC11A1DF38855ED6F2EE187E9C582BA6'
    print('pub', privateKeyToPublicKey(a) == s)
    print('pub wif', pubKeyToAddr(s) == '16UwLL9Risc3QfPqBUvKofHmBQ7wMtjvM')
