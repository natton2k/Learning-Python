import hashlib
hash_obj = hashlib.sha3_256()
hash_obj.update(b'Hello')
#print(hash_obj.hexdigest())

from cryptography.fernet import Fernet
key = Fernet.generate_key()
#print(key)
cipher = Fernet(key)
#print(cipher.encrypt(b'Hello'))
other_cipher = Fernet(key)
#print(other_cipher.decrypt(cipher.encrypt(b'Hello')))


#create your all key
keyword = b'123'
key = hashlib.sha3_256(keyword)
import base64
key_bytes = key.digest()
fernet_key = base64.urlsafe_b64encode(key_bytes) #reformat the key to be suitable for fernet
print(fernet_key)