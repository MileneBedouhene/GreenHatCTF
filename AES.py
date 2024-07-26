import json
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def aes_decrypt(encrypted_flag, key):
    key = key.to_bytes(32, 'big')
    b64 = json.loads(encrypted_flag)
    iv = b64decode(b64['iv'])
    ct = b64decode(b64['ciphertext'])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode('utf-8')

# Exemple d'utilisation

key =33101504605429929988144644818294662847610553853175879710826179671396651844626  
encrypted_flag = '{"iv": "JyamZXPHvw49toRWlA/xgg==", "ciphertext": "xfR7oskDwQij6R1YPdi9eDdiHbj537RTKOOQA7755fOSSzf5lLjspFgwcul3TpqN"}'

decrypted_flag = aes_decrypt(encrypted_flag, key)
print(decrypted_flag)
