# webchallenge_me
Task for webchallenge.me

## backend

For backend you need to have: 
* Redis
* Rabbitmq
* Postgresql
* libmagic
* python


Actions to run backend 

* Create virtual env `mkvirtualenv webchallenge`
* Setup requirements `pip isntall -r backend/backend/requirements.txt`
* copy `backend/backend/local_settings.py.sample` to `backend/backend/local_settings.py`
* edit `backend/backend/local_settings.py` to use your redit, rabbitmq, postgres
* go to backend `cd backend`
* start one or several celery processes `celery -A backend worker --loglevel=INFO --concurrency=10 -n worker1.%h`
  where `-n` - name of the worker
* start django-server `./manage.py rusnerver 0.0.0.0:8000`
 
 
## client 

For frontend you need to have: 
* nodejs


Actions to run cliento

* go to client `cd client`
* setup project `npm install`
* start project `gulp watch`
