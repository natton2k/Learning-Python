from cryptography.fernet import Fernet
import hashlib
import base64
fermat_prime = b'65537'
key = hashlib.sha3_256(fermat_prime)
key_bytes = key.digest()
fernet_key = base64.urlsafe_b64encode(key_bytes)
print(fernet_key)
cipher = Fernet(fernet_key)
text = b'gAAAAABaSsmdCFRxbqA6n-L0CMIMuhn26uGiIk5Wtx-V7wEPLBZYA67nGbNWyZziGyorwIlHqp3M5xrtzQj5tCab8XfBRCmdJXZYD1Fwp68AtD8WEMhblQ4I2DKDNFzqULH1DDETry3ptZnGZUgVo5gdDlnihqu1_oX-KboNpyRQ6J0DmeWTsm3L31btF_O6sX81rj3rBVI0qVuT7QdRT2burisQRnw5htA05llYgc1_fMkN_PSxCwY='
print(cipher.decrypt(text))