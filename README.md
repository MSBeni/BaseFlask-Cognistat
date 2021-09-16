# Working with SqlAlchemy

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