#!/bin/bash
3proxy /3pr.cfg
python3 /generate.py
openvpn --config /etc/openvpn/client.ovpn --auth-user-pass /auth.txt
