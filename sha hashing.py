import hashlib
str2hash = "Rokanraja"
result = hashlib.sha256(str2hash.encode())
result2 = hashlib.sha512(str2hash.encode())
print("The sha256 hexadecimal equivalent of hash is : ", end="")
print(result.hexdigest())
print("\nThe sha512 hexadecimal equivalent of hash is : ", end="")
print(result2.hexdigest())