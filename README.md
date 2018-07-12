# Flask-API-V1

Simple API made with Flask intended to be scalable to suit the needs of a particular application. The API is integrated with MySQL to store/request any data needed and keeping a username and password hash pair used with the `/login` route. For now, the API is used through CURL, with the ability to create parameters needed. The framework as is includes a Login feature that implements `flask_jwt_extended` to request data through CURL securely by using a token and `Bcrypt` in the user registration to store passwords in hash form.

### Prerequisites

Install `requirements.txt` with `pip install -r requirements.txt`. I recommend doing this within a `virtualenv`. 

### Deployment

Once all the required libraries are installed, the Flask app can run on its own development server for testing and development purposes, however in Production you should always serve the Flask app with a self hosting option (i.e. Gunicorn) or a hosted option (i.e. AWS, Heroku). To deploy the development server: in the `Flask-Api-Framework` directory start the Flask app with `python authenticate.py`. This will start the development server in localhost `127.0.0.1:5000/`.

## Usage

With a development server or production server running, there are three basic routes in this Flask app:

### /login

To log in and create a `JWT` token needed to use any other route:

`curl -H "Content-Type: application/json" -X POST   -d '{"username":"Mensk","password":"AHSNBF78"}' http://localhost:5000/login`

### /register

To register a user, you must use the `/login` route that needs a valid registered user in the MySQL database. A user can be registered in the database beforehand and those credential are use to create any new user. With a valid user available, the following can be used to register a new user:

`curl -H "Content-Type: application/json" -X POST   -d '{"username":"Mensk","password":"AHSNBF78","Username":"JimBob","Password":"BBvag67"}' http://localhost:5000/login`

and then

`curl -X GET http://localhost:5000/password -H "Authorization: Bearer JWT TOKEN GOES HERE"`

### /protected

This route can be modified to request any data, execute a MySQL stored procedure, etc. As an example, I included a function that will add client names to a MySQL table.

`curl -H "Content-Type: application/json" -X POST   -d '{"username":"Mensk","password":"AHSNBF78","Client First Name":"Saul","Client Last Name":"Lasko"}' http://localhost:5000/login`

and then

`curl -X GET http://localhost:5000/protected -H "Authorization: Bearer JWT TOKEN GOES HERE"`
