import pyotp
import os

user = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
secret = os.getenv('SECRET')

if user == None:
	print("USERNAME not specified")
	os._exit(-1)

if password == None:
	print("PASSWORD not specified")
	os._exit(-1)

if secret == None:
	print("SECRET not specified")
	os._exit(-1)

totp = pyotp.TOTP(secret)
token = totp.now()

f = open("/auth.txt", "w")
f.write("{}\n".format(user))
f.write('{}{}\n'.format(password, token))
f.close()

print("Generated OTP token for user ({}): {}".format(user,token))
