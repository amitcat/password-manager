SERVER_BUFFER_SIZE = 1024
SERVER_IP = '0.0.0.0'
SERVER_PORT = 5555

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

class Encryption:
    def __init__(self):
        self.key =RSA.generate(SERVER_BUFFER_SIZE)
        self.public_key = self.key.publickey()
        self.private_key = self.key
    
    def export_public_key(self):
        return self.public_key.export_key()
    
    def encrypt(self, plaintext , public_key):
        # Implement code to encrypt ciphertext using symmetric encryption
        cipher = PKCS1_OAEP.new(public_key)
        ciphertext = cipher.encrypt(plaintext.encode())
        return ciphertext
    
    def decrypt(self, ciphertext ):
        # Implement code to decrypt ciphertext using symmetric encryption
        cipher = PKCS1_OAEP.new(self.private_key)
        plaintext = cipher.decrypt(ciphertext).decode()
        return plaintext




