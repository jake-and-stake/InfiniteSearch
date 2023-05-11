Run on Ubuntu

    Amazon Linux 2 (CentOS) 7 has an unsupported OpenSSL version. 
    Pip will fail to fetch from pypi. [link](https://bugs.python.org/issue47201)

## Description
Runs the website InfiniteSearch.
- Creates a website using Flask Backend
- The website uses the WSGI software Gunicorn to host the application
    - Given the command `gunicorn --certfile cert.pem --keyfile key.pem -b 0.0.0.0:5000 --workers 4 --threads 2 wsgi:app`,
    Gunicorn binds the app to the port 5000 and makes the port public to other machines on the network (since the command is running in a docker container, this network is the Docker network)
- Running this line `docker run -p 8000:5000 infinitesearch` allows access to the docker container's `5000` port by binding the local machine's `8000` port to it

## Instructions
-  $ `source .venv/bin/activate`

## Database
 - 

## Local Testing Instructions
1. Run `flask run` for http. For https run `flask run --cert=cert.pem --key=key.pem --host "0.0.0.0"`
2. Visit `http://127.0.0.1:5000` in your browser
3. 

### Using Docker
1. Install docker
2. `docker build -t infinitesearch .`
3. `docker run -p 8000:5000 infinitesearch`
`gunicorn --certfile cert.pem --keyfile key.pem -b 0.0.0.0:5000 --workers 4 threads 2 wsgi:app`

### Docker compose
1. Navigate to folder containing `docker-compose.yml`
2. Build images using `docker compose build`
3. Run images using `docker-compose up -d` or `docker-compose up --build`
2. Shut it down using `docker-compose down`

## Create your own local certificate
1. `openssl genrsa -out key.pem 2048`
2. `openssl req -new -x509 -key key.pem -out cert.pem -days 365`

## Troubleshooting
- Check that your IP address is added to cloud.mongodb.com. Go to The Network Access section

Local Machine Installs
docker
docker-compose

## AWS EC2 install/run instructions
- `sudo yum install python3-pip`
- `sudo systemctl enable docker.service`
- `sudo systemctl start docker.service`
- `pip3 install docker-compose`
- `docker-compose up --build-d`
