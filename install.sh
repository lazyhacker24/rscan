#!/bin/bash

echo "Installing RSCAN dependencies..."

sudo apt update && sudo apt install -y python3 python3-pip nmap git

pip3 install -r requirements.txt

echo "Installation completed!"
echo "Run tool: python3 rscan.py"
