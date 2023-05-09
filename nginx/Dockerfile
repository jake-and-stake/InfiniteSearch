FROM nginx:latest
RUN rm /etc/nginx/conf.d/default.conf

COPY cert.pem /etc/nginx/cert.pem
COPY key.pem /etc/nginx/key.pem
COPY nginx.conf /etc/nginx/nginx.conf
