#!/usr/bin/env bash
# Not finished nor tested

# This is used when deploying the application on production server
exec &> log.txt

PROJECT_DIR="/home/mjovanc/tv/venv/project_files"

# Git deploying
git -C $PROJECT_DIR fetch production
git -C $PROJECT_DIR checkout -b master production/master

# Update static files and DB
#source /home/mjovanc/tv/bin/activate # activating the virtualenv

#requirements.txt install -r $PROJECT_DIR/requirements.txt
#python $PROJECT_DIR/manage.py collectstatic
#python $PROJECT_DIR/manage.py makemigrations
#python $PROJECT_DIR/manage.py migrate

#deactivate # deactivates the virtualenv

# Restarting servers
#systemctl restart gunicorn.service
#/etc/init.d/nginx restart