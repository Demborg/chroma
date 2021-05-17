# Chroma

## Setup
### Install
```
python3 -m venv venv
source venv/bin/activate
pip intall -p requirements.txt
```
### Create database
```
docker run --name postgres -e POSTGRES_PASSWORD=secret -d -p 5432:5432 postgres
```

## Start application (dev mode)
```
FLASK_ENV=development flask run
```