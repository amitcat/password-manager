SERVER_BUFFER_SIZE = 1024
SERVER_IP = '0.0.0.0'
SERVER_PORT = 5555

from cryptography.fernet import Fernet
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

class Encryption:
    def __init__(self):
        self.key =RSA.generate(SERVER_BUFFER_SIZE)
        self.public_key = self.key.publickey()
        self.private_key = self.key
        self.key_for_password = Fernet.generate_key()
    
    def export_public_key(self):
        return self.public_key.export_key()
    
    def encrypt_msg(self, plaintext , public_key):
        # Implement code to encrypt ciphertext using symmetric encryption
        cipher = PKCS1_OAEP.new(public_key)
        chunk_size = 86 
        ciphertext = b""
        
        for i in range(0, len(plaintext), chunk_size): # Encrypt in chunks
            chunk = plaintext[i:i + chunk_size]
            encrypted_chunk = cipher.encrypt(chunk)
            ciphertext += encrypted_chunk
        return ciphertext
        # ciphertext = cipher.encrypt(plaintext.encode())
        # return ciphertext
    
    def decrypt_msg(self, ciphertext ):
        # Implement code to decrypt ciphertext using symmetric encryption
        cipher = PKCS1_OAEP.new(self.private_key)
        chunk_size = 128
        plaintext = b""
        

        for i in range(0, len(ciphertext), chunk_size): # Decrypt in chunks
            chunk = ciphertext[i:i + chunk_size]
            print(cipher.decrypt(chunk))
            decrypted_chunk = cipher.decrypt(chunk)
            plaintext += decrypted_chunk

        plaintext = plaintext.decode()
        return plaintext
        # plaintext = cipher.decrypt(ciphertext).decode()
        # return plaintext
    
    # def encrypt_password(self, password):
    #     cipher = Fernet(self.key_for_password)
    #     encrypted_password = cipher.encrypt(password.encode())
    #     return encrypted_password

    # def decrypt_password(self, encrypted_password):
    #     cipher = Fernet(self.key_for_password)
    #     decrypted_password = cipher.decrypt(encrypted_password).decode()
    #     return decrypted_password




