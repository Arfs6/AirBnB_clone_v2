#!/usr/bin/env bash
# Set up server for deploying web_static
#
sudo apt update -y
sudo apt install -y nginx
sudo mkdir /data
sudo chown ubuntu:ubuntu /data
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/ 
mkdir -p /data/web_static/releases/test/
echo 'Hello!
Welcome to accessibility hub.' > /data/web_static/releases/test/index.html
ln -fs /data/web_static/releases/test/ /data/web_static/current 
sudo sed -i 's/^server {$/server {\n\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t}/' /etc/nginx/sites-enabled/default
sudo service nginx restart
