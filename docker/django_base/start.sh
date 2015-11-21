#!/bin/bash

cat << EOF > /etc/supervisor/conf.d/supervisor-app.conf
[program:django]
directory = /opt/web/
command = gunicorn web.wsgi

[program:nginx]
command = /usr/sbin/nginx -g "daemon off;"
EOF

cd /opt/web/

pip install -r /opt/web/requirements.txt

python3 ./manage.py collectstatic --noinput
python3 ./manage.py migrate

