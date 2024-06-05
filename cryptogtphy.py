from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def aes_encrypt(key, data):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data.encode('utf-8'))
    return base64.b64encode(nonce + ciphertext).decode('utf-8')

def aes_decrypt(key, data):
    raw_data = base64.b64decode(data)
    nonce = raw_data[:16]
    ciphertext = raw_data[16:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext).decode('utf-8')
    return plaintext

# Örnek kullanım
key = get_random_bytes(16)
data = "Merhaba, dünya!"
encrypted_data = aes_encrypt(key, data)
print(f"Şifreli: {encrypted_data}")
decrypted_data = aes_decrypt(key, encrypted_data)
print(f"Çözüldü: {decrypted_data}")
