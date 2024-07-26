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
    pt = cipher.decrypt(ct)
    return pt.decode('utf-8')

# Exemple d'utilisation

key =112374476872014624591276898161978042815099170765827274764402705083321630869961  
encrypted_flag = '{"iv": "xTq149TR2u3yDOsTrEu8TQ==", "ciphertext": "IcqsfTIMS8V1ESD/a4VZwFcf2N/lOLvDGVtyPjW9DO1PNv7+D6sevNqtQiqT0UTY"}'

decrypted_flag = aes_decrypt(encrypted_flag, key)
print(decrypted_flag)
