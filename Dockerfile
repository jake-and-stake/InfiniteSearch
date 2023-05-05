FROM python:3.11.1
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
ENV FLASK_APP=app.py
CMD ["flask", "run", "--cert=cert.pem", "--key=key.pem", "--host", "0.0.0.0"]