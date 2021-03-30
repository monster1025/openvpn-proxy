import pyotp
import os

user = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
secret = os.getenv('SECRET')

if user == "":
	print("USERNAME not specified")
	os.exit(-1)

if password == "":
	print("PASSWORD not specified")
	os.exit(-1)

if secret == "":
	print("SECRET not specified")
	os.exit(-1)

totp = pyotp.TOTP(secret)
token = totp.now()

f = open("/auth.txt", "w")
f.write("{}\n".format(user))
f.write('{}{}\n'.format(password, token))
f.close()

print("Generated OTP token for user ({}): {}".format(user,token))