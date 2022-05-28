# openvpn-proxy
This tool can help you with over-private companies vpn servers.
It can authomatically authentificate via 'password+otp pin' schema and provide proxy access to VPN network.

### Configuration
Please specify your username, password and secret token in openvpn/settings/openvpn.env (you can use openvpn.env.sample)  
Also you can specify proxy password for authentification, username is 'admin'.

### Definitions 
Openvpn configuration file must be named 'client.ovpn' in 'openvpn/settings/conf/' directory.

## Converting Google Auth export to secrets
You can use this project to convert export url to secret key: https://github.com/dim13/otpauth

## Running
Place configuration in env file, add your vpn setting to 'openvpn/settings/conf', rename you vpn config to client.ovpn and run 'docker-compose up -d'
You will get a HTTPS proxy at 3128 port and SOCKS proxy on 1080.
