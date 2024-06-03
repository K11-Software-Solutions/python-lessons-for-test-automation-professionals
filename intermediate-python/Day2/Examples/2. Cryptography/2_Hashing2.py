import hashlib

hash_string = "hello"

hash_bytes = hash_string.encode()

print("String bytes: ", hash_bytes)

hash_engine = hashlib.sha256(hash_bytes)

digest = hash_engine.hexdigest()

print("Digest bytes: ", digest)
