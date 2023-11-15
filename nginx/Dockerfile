FROM nginx:1.25

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

RUN mkdir -p /etc/letsencrypt /var/www/certbot

EXPOSE 80
EXPOSE 443
