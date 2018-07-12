# Flask-API-Middleware-V1

Simple API made with Flask intended to be scalable to suit the needs of a particular application. The API is integrated with MySQL to store/request any data needed and keeping a username and password hash pair used with the `/login` route. For now, the API is used through CURL, with the ability to create parameters needed. The framework as is includes Login feature that implements `flask_jwt_extended` to request data through CURL secure by using a token and `Bcrypt` in the user registration to store passwords in hash form.
