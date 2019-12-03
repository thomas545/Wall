
# wall
### Documentation:

1. [Django](https://docs.djangoproject.com/en/2.0/releases/2.0/)
2. [Django Rest Framework](https://www.django-rest-framework.org/)


### Installation:
1. pip install -r requirements.txt
2. python manage.py runserver

##### Steps for install Celery and work it.
1. pip install -r requirements.txt
2. sudo apt-get install -y erlang
3. sudo apt-get install rabbitmq-server
4. sudo systemctl enable rabbitmq-server
5. sudo systemctl start rabbitmq-server to check if rabbitmq is working run: systemctl status rabbitmq-server
6. run local server for backend
7. run this command in new terminal in project path with activating virtual env: celery -A wall worker -l info

### API Endpoints
##### Register
Method: `POST`  
Endpoint: `/registration/`  
Payload:  
`{  
    "username": "USERNAME",  
    "password1": "PASSWORD",  
    "password2": "PASSWORD",  
    "email": "OPTIONAL_EMAIL"  
}`
##### Login
Method: `POST`  
Endpoint: `/login/`  
Payload:  
`{  
    "username": "USERNAME",  
    "password": "PASSWORD"  
}`


### Admin Credentials
### Username: `admin`  
### Password: `123` 


