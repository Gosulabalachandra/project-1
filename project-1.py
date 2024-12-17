import bcrypt
password=b"Balachandra"
hashed=bcrypt.hashpw(password,bcrypt.gensalt())
print(hashed)
entred_password=input("Enter password to login")
entered_password=bytes(entered_password,encoding="utf-8")
if bcrypt.checkpw(entered_password,hashed):
    print("Login successfully")
else:
    print("Invalid password")