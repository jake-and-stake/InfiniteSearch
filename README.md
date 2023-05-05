Run on Ubuntu

    Amazon Linux 2 (CentOS) 7 has an unsupported OpenSSL version. 
    Pip will fail to fetch from pypi. [link](https://bugs.python.org/issue47201)


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
3. `docker run -p 5000:5000 infinitesearch`

## Create your own local certificate
1. `openssl genrsa -out key.pem 2048`
2. `openssl req -new -x509 -key key.pem -out cert.pem -days 365`

## Troubleshooting
- Check that your IP address is added to cloud.mongodb.com. Go to The Network Access section