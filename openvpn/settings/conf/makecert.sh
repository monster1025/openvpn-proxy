openssl pkcs12 -in user.pfx -clcerts -nokeys -out user.crt.new && mv user.crt.new user.crt
openssl pkcs12 -in user.pfx -nocerts -out user_pass.key.new && mv user_pass.key.new user_pass.key
openssl rsa -in user_pass.key -out user.key.new && mv user.key.new user.key
rm -f user.crt.new user_pass.key.new user.key.new
