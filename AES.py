def aes_decrypt(encrypted_flag, key):
    key = key.to_bytes(32, 'big')
    b64 = json.loads(encrypted_flag)
    iv = b64decode(b64['iv'])
    ct = b64decode(b64['ciphertext'])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode('utf-8')

# Exemple d'utilisation
# La clé doit être la même que celle utilisée pour le chiffrement
key = generate_random_256bit()  # Remplacez par la clé utilisée pour chiffrer
encrypted_flag = "..."  # Remplacez par le flag chiffré JSON

decrypted_flag = aes_decrypt(encrypted_flag, key)
print(decrypted_flag)
