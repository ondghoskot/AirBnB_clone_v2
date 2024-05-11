#!/usr/bin/env bash
# sets up web servers for deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw --force enable
sudo ufw allow 22/tcp
sudo ufw allow 'Nginx HTTP'
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo tee /etc/nginx/sites-available/default > /dev/null <<EOF
server {
    listen 80;
    listen [::]:80;
    server_name anassch.tech;

    location /hbnb_static/ {
        alias /data/web_static/current/;
    }

    error_page 404 /404.html;
    location = /404.html {
        internal;
        alias /var/www/html/404.html;
    }
}
EOF
sudo service nginx restart
