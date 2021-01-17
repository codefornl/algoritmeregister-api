# algorithmregister-api
An API to get remote data, cached in a database, for algorithmregister

## How to start

### Development:

- Create a Python 3 virtual env named `venv` and activate it.
- Install requirements inside your virtual env with `python -m pip install -r requirements.txt`
- Set up and customize the environment variabels, see below
- Start application with `./algorithmregister.sh`

### Production:

- Build Docker image (see Dockerfile)
- Create container with the required environments variabels (see below, customize them)
- Start container, the application will be exported under port 8000


## Handy endpoints
[API homepage](http://localhost:8000/)
[OpenApi docs](http://localhost:8000/docs)
[Import data](http://localhost:8000/api/jobs)

## Environment variables
Set the following environment variabels before starting the application.

    USERS={"demo": "test12345"}
    BACKEND_CORS_ORIGINS_CSV=http://localhost,http://localhost:4200,http://localhost:3000

### About USERS variabel

The `USERS` variabel defines the list of users with password. This should be a secret value. The list is a JSON object, property is the username, value is a plain password string (we need to change this to hashed values in the near feature).

Example:

    {
      "tim": "insecure-password",
      "tom": "another-insecure-password"
    }
