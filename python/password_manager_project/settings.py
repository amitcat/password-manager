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
    
    def encrypt_msg(self, plaintext , public_key):
        # Implement code to encrypt ciphertext using symmetric encryption
        cipher = PKCS1_OAEP.new(public_key)
        chunk_size = 86 
        ciphertext = b""
        # print('plaintext >>>>>>',plaintext, type(plaintext))
        
        for i in range(0, len(plaintext), chunk_size): # Encrypt in chunks
            chunk = plaintext[i:i + chunk_size]
            encrypted_chunk = cipher.encrypt(chunk)
            ciphertext += encrypted_chunk
        # print('ciphertext >>>>>>',ciphertext, len(ciphertext))
        return ciphertext
    
        # ciphertext = cipher.encrypt(plaintext.encode())
        # return ciphertext
    
    def decrypt_msg(self, ciphertext ):
        # Implement code to decrypt ciphertext using symmetric encryption
        cipher = PKCS1_OAEP.new(self.private_key)
        chunk_size = 128
        plaintext = b""
        # print('ciphertext in decrypt >>>>>>',ciphertext, len(ciphertext))

        

        for i in range(0, len(ciphertext), chunk_size): # Decrypt in chunks
            chunk = ciphertext[i:i + chunk_size]
            # print('current chunk >>>>>>',chunk, len(chunk))
            decrypted_chunk = cipher.decrypt(chunk)
            plaintext += decrypted_chunk

        plaintext = plaintext.decode()
        return plaintext




