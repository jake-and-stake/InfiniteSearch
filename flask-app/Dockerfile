FROM python:3.11.1
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
ENV FLASK_APP=app.py

# Add SSL certs
# CMD ["gunicorn", "--certfile", "certs/cert.pem", "--keyfile", "certs/key.pem", "-b", "0.0.0.0:5000", "--workers", "4", "--threads", "2", "wsgi:app"]

# No SSL certs
CMD ["gunicorn", "-b", "0.0.0.0:5000", "--workers", "4", "--threads", "2", "wsgi:app"]