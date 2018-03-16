# Bucketlist Service 

> First of all , big shoutout to Jee Gikera!. This is an extension of his write up on 
[RESTful API with Flask](https://scotch.io/tutorials/build-a-restful-api-with-flask-the-tdd-way)
> The directory structure differs a bit from that in [RESTful API with Flask](https://scotch.io/tutorials/build-a-restful-api-with-flask-the-tdd-way)

## Objective This Repository

Flask is a simple to use python framework. You only add what you need. However , this project makes use of a Flask API Scafold which is basically a bundle of libaries needed to build a RESTful API using Flask . Functionalities include 

* Flask-SQLAlchemy for creating POCOs
* Flask-Migrate for running migrations 
* CRUD Mixin for Models 
* Flask-Security for API security 

## How to Launch

1. Clone this repo ( of course !) and cd to working directory
2. Create virtual environment(please name it venv) using [virtualenv](http://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv)
3. Run $ source .env ( this activates the virtual environment and creates enviromental variables)
4. Install dependencies ( $ pip install -r requirements.txt)
5. Run $ docker-compose up ( this creates a PostgreSQL container for the database of this application ) 
Useful links: [Docker](https://docs.docker.com/get-started/) ,[Docker-compose](https://docs.docker.com/compose/install/)
6. Run $ flask run

## Testing 
Recommended client : Postman 

### Get a token
So, the first time a GET request is made to http://localhost:5000 a test user is created with 
Username: test@example.com
password: test123

To get a token send a POST request to http://127.0.0.1:5000/login with
{'email':'test@example.com', 'password':'test123'} 

### Make a request with a Token 
Make a GET request to localhost:5000/bucketlists
Add the  header paramater 
Authentication-Token : add-your-token-here

