from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
edata= f.encrypt(b"secret message.")

val=f.decrypt(edata)
print(val)
