# Working with SqlAlchemy and Deploying on Heroku

## Installation
Please install the necessary libraries as before:

```shell
pip install Flask
pip install Flask-RESTful
```
### Authentication and logging with Flask and JWT
JWT stands for JSON Web Token and can be used to encode some data.

### installation
Please install the Flask-JWT library using this command:
```shell
pip install Flask-JWT
```

### SqlAlchemy Installation
```shell
pip install Flask-SQLAlchemy
```


## Configuration of :
Please follow this [link](https://computingforgeeks.com/how-to-install-ms-sql-on-ubuntu/) to Install Microsoft SQL 
Server 2019 on Ubuntu.

Simply type this command to create run the sqlcmd on your command line and be able to create database.
```shell
sqlcmd -S 127.0.0.1 -U SA
```
```shell
1> create database testDB;
1> select name from sys.databases;
2> go
name                                                                                                                            
--------------------------------------------------------------------------------------------------------------------------------
master                                                                                                                          
tempdb                                                                                                                          
model                                                                                                                           
msdb                                                                                                                            
testDB                                                                                                                          

(5 rows affected)
```

# Heroku Deployment
For deploying the project on heroku you need to create these files with these goals:

* **runtime.txt** file: To tell heroku what language (python) and what version you are using 
* **requirements.txt** file: Telling heroku what libraries we are using in this project nad how to install them.
    - Note: The uwsgi library added for this project is responsible for multi-process support, restarting processes 
      if they hang up and so on. It is not needed to be installed locally (need a c compiler). 
* **uwsgi.ini** file: Contains some configuration parameters for uwsgi processes to run our app.
    - [uwsgi] is the section tag and then we should define the port. 
      
    - The heroku has its own port this part "http-socket = :$(PORT)" can run the port from heroku configuration.
      
    - The "master = true" is going to tell heroku about master process when running wsgi and controlling slave 
      processes. 
      
    - "die-on-term = true" kill an uwsgi process  when it is terminated to free up resources. 
      
    - "module = run:app" shows the module we are running which is inside run.py in the variable called app.
    
* **Procfile** file: Explain what dyno we are going to use in Heroku which run the uwsgi process and when we deploy
the python app will be handled and listen to python app and start flask app.
  
# Other Cloud-based Service Providers:


```editorconfig
server{
listen 80;
real_ip_header X-Forwarded-For;
set_real_ip_from 127.0.0.1;
server_name localhost;

location / {
include uwsgi_params;
uwsgi_pass unix:/var/www/html/items-rest/socket.sock;
uwsgi_modifier1 30;
}

error_page 404 /404.html;
location = /404.html{
root /usr/share/nginx/html;
}

error_page 500 502 503 504 /50x.html
location = /50x.html {
root /usr/share/nginx/html;
}
}
```

- Ubuntu service creation:
```editorconfig
[Unit]
Description=uWSGI items rest

[Service]
Environemnt=DATABASE_URL=postgres://jose:1234@localhost:5432/msbeni
ExecStart=/var/www/html/items-rest/venv/bin/uwsgi --master --emperor /var/www/html/items-rest/uwsgi.ini --die-on-term --uid msbeni --gid msbeni --logto /var/www/html/items-rest/log/emperor.l
og
Restart=always
KillSignal=SIGQUIT
Type=notify
NotifyAccess=all

[Install]
WantedBy=multi-user.target
```


- uwsgi.ini file edit on cloud
```editorconfig
[uwsgi]
base = /var/www/html/items-rest
app = run
module = %(app)

home = %(base)/venv
pythonpath = %(base)

socket = %(base)/socket.sock

chmod-socket = 777

processes = 8

threads = 8

harakiri = 15

callable = app

logto = /var/www/html/items-rest/log/%n.log

```


__________________________________________________________________________
[uwsgi]
base = /var/www/html/items-rest
app = run
module = %(app)

home = %(base)/venv
pythonpath = %(base)

socket = %(base)/socket.sock

chmod-socket = 777

processes = 8

threads = 8

harakiri = 15

callable = app

logto = /var/www/html/items-rest/log/%n.log