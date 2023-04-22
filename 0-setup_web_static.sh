#!/usr/bin/env bash
# Script that sets up your web servers for the deployment of web_static.

# Installing Nginx if it is not installed
sudo apt-get update
sudo apt-get install -y nginx

# Creating /data/ directory if it doesn't exist
if [ ! -d "/data/" ]
then
	mkdir /data/
fi

# Creating /data/web_static if it doesn't exist
if [ ! -d "/data/web_static/" ]
then
	mkdir /data/web_static/
fi

# Creating /data/web_static/releases/ if it doesn't exist
if [ ! -d "/data/web_static/releases/" ]
then
	mkdir /data/web_static/releases/
fi

# Creating /data/web_static/shared if it doesn't exist
if [ ! -d "/data/web_static/shared/" ]
then
	mkdir /data/web_static/shared/
fi

# Creating /data/web_static/releases/test/ if it doesn't exist
if [ ! -d "/data/web_static/releases/test/" ]
then
	mkdir /data/web_static/releases/test/
fi

# Creating fake HTML file /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    <h1>Hello World!</h1>
    <p>This is a test</p>
  </body>
</html>" > /data/web_static/releases/test/index.html

# Creating a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder.
if [ ! -L "/data/web_static/current" ]
then
	ln -s /data/web_static/releases/test /data/web_static/current
else
	ln -sf /data/web_static/releases/test /data/web_static/current
fi

# Giving ownership of the /data/ folder to the ubuntu user and group
sudo chown -hR ubuntu:ubuntu /data/

# Update the Nginx configuration to server the content of /data/web_static/current/
sudo echo 
sudo echo "
server {
     listen    80 default_server;
     listen    localhost:80;
     listen    elizabettenuel.tech:80;
     root      /etc/nginx/html/;
     index     index.html index.htm;
     location  /hbnb_static/ {
          alias /data/web_static/current/;
     }
}
" | sudo tee /etc/nginx/sites-available/default
sudo service nginx restart
