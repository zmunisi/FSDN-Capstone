# FSDN-Capstone
 This is the final Capstone Project for my Udacity Full Stack Nanodegree and the goal is to create an API for The Casting Agency which models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

## Models:
1. Movies with attributes title and release date
2. Actors with attributes name, age and gender

## Endpoints:
- GET /actors and /movies
- DELETE /actors/ and /movies/
- POST /actors and /movies and
- PATCH /actors/ and /movies/

## Roles:
### Casting Assistant
- Can view actors and movies
### Casting Director
- All permissions a Casting Assistant has and…
- Add or delete an actor from the database
- Modify actors or movies
### Executive Producer
- All permissions a Casting Director has and…
- Add or delete a movie from the database

## Getting Started
### Virtual Environment
We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### Create a environment folder env
```bash
python -m venv env
```
#### Activate the encironment (macOS)
```bash
source env/bin/activate
```
#### Activate the encironment (windows)
```bash
source env/Scripts/activate
```

#### Export all the required variables
```bash
# Health Check
export EXCITED=true

# Flask App config
export FLASK_APP=app
export FLASK_ENV=development

# Pagination
export RESULTS_PER_PAGE=10

# Auth0
export AUTH0_DOMAIN=''
export ALGORITHMS=''
export API_AUDIENCE=''
# Bearer Tokens
export CASTING_ASSISTANT='' 
export CASTING_DIRECTOR=''
export EXECUTIVE_PRODUCER=''
```

#### Install all project requirements
```bash
pip install -r requirements.txt
```

#### Upgrade pip
```bash
pip install --upgrade pip
```

#### Key Dependencies
- [Python 3](https://www.python.org/downloads/) server language the project is based on

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the database

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

### Run the environment locally
To run the API locally you need [postgres](https://www.postgresql.org/download/) running and configured on your local machine

#### export the SQLALCHEMY_DATABASE_URI
```bash
export SQLALCHEMY_DATABASE_URI='postgresql://{{username}}:@localhost:5432/{{database_name}}'
export SQLALCHEMY_TRACK_MODIFICATIONS=False
```

#### Run database migrations
```bash
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```
#### Print out all variables to check everything is set up
```bash
printenv
```

## Run Flask
```bash
flask run
```
or

```bash
flask run --reload
```
The `--reload` flag will detect file changes and restart the server automatically.

## Verify on the Browser
Navigate to project homepage [http://127.0.0.1:5000/](http://127.0.0.1:5000/) or [http://localhost:5000](http://localhost:5000) 

## Setup Auth0
All endpoints are decorated with Auth0](https://manage.auth0.com/) permissions so you need to:
1. Create a new [Auth0](https://manage.auth0.com/) Account
2. Select a unique tenant domain
3. Create a new, single page web application
4. Create a new API
   - in API Settings:
     - Enable RBAC
     - Enable Add Permissions in the Access Token
5. Create new API permissions:
   - `get:movies`
   - `get:actors`
   - `post:movies`
   - `post:actors`
   - `patch:movies`
   - `patch:actors`
   - `delete:movies`
   - `delete:actors`
6. Create new roles for:
   - Casting Assistant
     - can `get:actors`
     - can `get:movies`
   - Casting Director
     - can `get:movies`
     - can `get:actors`
     - can `post:movies`
     - can `post:actors`
     - can `patch:movies`
     - can `patch:actors`
     - can `delete:actors`
   - Executive Producer
     - can perform all actions
7. Test your endpoints with [Postman](https://getpostman.com).
   - Register 3 users - assign them to the particular roles with the included permissions
   - Sign into each account and make note of the JWT.
   - Test your endpoints with [Postman](https://getpostman.com).
   - Import the postman collection `./Capstone.postman_collection.json`
   - Right-clicking the collection folder for Casting Assistant, Casting Director and Executive Producer, navigate to the authorization tab, and including the JWT in the token field (you should have noted these JWTs).
   - Run the collection and correct any errors.
   - Export the collection overwriting the one we've included so that we have the proper JWTs!

## Testing
Besides the postman manual testing you can optionally run the unit tests with
```bash
python test_capstone.py
```

## API
Here is a list of all existing endpoints

### Actors
GET '/actors'
- fetches all actors
- requested adguments: None
- response example:
```
{
    "actors": [
        {
            "age": 56,
            "gender": "male",
            "id": 24,
            "name": "Keanu Charles",
            "surname": "Reeves"
        }
    ],
    "success": true
}
```

- curl example:
```
url -H 'authorization: Bearer {YOUR_ACCESS_TOKEN}' \
       -X GET \
       http://127.0.0.1:5000/actors
```

POST '/actors'
- Creates a new actor
- Required JSON header example:
```
{
    "name": "Keanu Charles",
    "surname": "Reeves Neo",
    "age": 56,
    "gender": "Male"
}
```
- Returns: An object of successfuly created actor state and it's corresponding actor_id
- Response example:
```
{
  "created": 75, 
  "success": true
}
```

- curl example:
```
curl -X POST    -H "Content-Type: application/json" -H 'Authorization: Bearer {YOUR_ACCESS_TOKEN}' \
        -d '{
                "name": "Keanu Charles",
                "surname": "Reeves",
                "age": 56,
                "gender": "Male"
            }'  http://127.0.0.1:5000/actors
```

PATCH '/actors/<int:actor_id>'
- Edit's an actor
- Request Arguments: actor_id (integer)
- Returns: An object of successfuly edited actor state and it's corresponding actor_id
- Response example:
```
{
  "success": true, 
  "updated": 25
}
```
- curl example:
```
curl -X PATCH    -H "Content-Type: application/json" -H 'Authorization: Bearer {YOUR_ACCESS_TOKEN}' \
        -d '{
                "name": "Patrick",
                "surname": "Swayze",
                "age": 57,
                "gender": "Male"
            }'  http://127.0.0.1:5000/actors/1
```

DELETE '/actors/<int:actor_id>'
- Deletes an actor
- Request Arguments: actor_id (integer)
- Returns: An object of successfuly deleted actor state and it's corresponding actor_id
- Response example:
```
{
  "deleted": 25, 
  "success": true
}
```
- curl example:
```
curl -X DELETE    -H "Content-Type: application/json" -H 'Authorization: Bearer {YOUR_ACCESS_TOKEN}' http://127.0.0.1:5000/actors/1
```

### Movies
GET '/movies'
- Fetches all movies
- Requested arguments: None
- Response example:
```
{
    "movies": [
        {
            "description": "An F.B.I. Agent goes undercover to catch a gang of surfers who may be bank robbers.",
            "director": "Kathryn Bigelow",
            "id": 20,
            "release_date": "1991",
            "title": "Point Break"
        }
    ],
    "success": true
}
```

- curl example:
```
curl -H 'Authorization: Bearer {YOUR_ACCESS_TOKEN}' \
       -X GET http://127.0.0.1:5000/movies
```

POST '/movies'
- Creates a new movie
- Required JSON header example:
```
{
    "desc": "An F.B.I. Agent goes undercover to catch a gang of surfers who may be bank robbers.",
    "director": "Kathryn Bigelow",
    "release_date": "1991",
    "title": "Point Break"
}
```
- Returns: An object of successfuly created movie state and it's corresponding movie_id
- Response example:
```
{
    "created": 42,
    "success": true
}
```

- curl example:
```
curl -X POST    -H "Content-Type: application/json" -H 'Authorization: Bearer {YOUR_ACCESS_TOKEN}' \
        -d '{
                "desc": "An F.B.I. Agent goes undercover to catch a gang of surfers who may be bank robbers.",
                "director": "John Woo",
                "release_date": "1991",
                "title": "Point Break"
            }'  http://127.0.0.1:5000/movies
```

PATCH '/movies/<int:movie_id>'
- Edit's an movie
- Request Arguments: movie_id (integer)
- Returns: An object of successfuly edited movie state and it's corresponding movie_id
- Response example:
```
{
  "success": true, 
  "updated": 45
}
```
- curl example:
```
curl -X PATCH    -H "Content-Type: application/json" -H 'Authorization: Bearer {YOUR_ACCESS_TOKEN}' \
        -d '{
                "desc": "When a beautiful stranger leads computer hacker Neo to a forbidding underworld",
                "director": "Lana and Lilly Wachowski",
                "release_date": "1999",
                "title": "Matrix"
            }'  http://127.0.0.1:5000/movie/1
```

DELETE '/movies/<int:movie_id>'
- Deletes an movie
- Request Arguments: movie_id (integer)
- Returns: An object of successfuly deleted movie state and it's corresponding movie_id
- Response example:
```
{
  "deleted": 45, 
  "success": true
}
```
- curl example:
```
curl -X DELETE    -H "Content-Type: application/json" -H 'Authorization: Bearer {YOUR_ACCESS_TOKEN}' http://127.0.0.1:5000/movies/1
```

## Heroku Link
```
https://fsnd-capstone-zmunisi.herokuapp.com/
```