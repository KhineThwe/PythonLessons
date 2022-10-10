import secrets
print('Printing integer number using secrets module')
print(secrets.token_bytes(2))#1 bytes = 8bits
print(secrets.token_hex(3))#1 byte equal to two hex digits
