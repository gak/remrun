FROM ubuntu:14.04

RUN apt-get update

RUN apt-get install -y \
    rsync \
    wget \
    git-core \
    git \
    ca-certificates \
    build-essential \
    git \
    python2.7 \
    python-dev \
    python3.4 \
    python3-dev \
    python3-setuptools \
    supervisor \
    python-software-properties \
    software-properties-common

RUN easy_install3 pip

# Upgrade to latest pip
RUN pip3 install --upgrade pip

# Install nginx
RUN apt-get update
RUN add-apt-repository -y ppa:nginx/stable

# Packages needed by Django
RUN apt-get install -y sqlite3
RUN apt-get install -y libpq-dev
RUN apt-get install -y postgresql
RUN apt-get install -y postgresql-contrib
RUN apt-get install -y nginx

# Python libs needed by Django
RUN pip3 install uwsgi
RUN pip3 install gunicorn

# Remove default nginx config
RUN rm /etc/nginx/sites-enabled/default

# nginx config
ADD django /etc/nginx/sites-enabled/

# preparation script
ADD start.sh /

EXPOSE 80

CMD ./start.sh && supervisord -n

