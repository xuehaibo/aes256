from Crypto.Cipher import AES
import base64
import hashlib


class AES256:

    def __init__(self):
        self.key = "abcdefghijklmnop"
        self.BS = AES.block_size
        self.pad = lambda s: s + (self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS)
        self.unpad = lambda s: s[0:-ord(s.decode("utf-8")[-1])]

    def encrypt(self, message):
        cipher = AES.new(hashlib.sha256(self.key.encode("utf-8")).digest())
        cipher_text = cipher.encrypt(self.pad(message))
        return base64.b64encode(cipher_text)

    def decrypt(self, message):
        cipher = AES.new(hashlib.sha256(self.key.encode("utf-8")).digest())
        resp = cipher.decrypt(base64.b64decode(message))
        return self.unpad(resp)



if __name__ == '__main__':
    print(AES256().encrypt("123456"))
    print(AES256().decrypt("c1rTaqRXQ+jIEqiJLRFGIw=="))
