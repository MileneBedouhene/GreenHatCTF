def aes_decrypt(encrypted_flag, key):
    key = key.to_bytes(32, 'big')
    b64 = json.loads(encrypted_flag)
    iv = b64decode(b64['iv'])
    ct = b64decode(b64['ciphertext'])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode('utf-8')

# Exemple d'utilisation

key = 98050855612111536514983487793585093688673022207093278002021592952241434843579  


decrypted_flag = aes_decrypt(encrypted_flag, key)
print(decrypted_flag)