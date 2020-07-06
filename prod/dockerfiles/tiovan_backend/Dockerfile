FROM tiangolo/uwsgi-nginx:python3.8

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY ./prod/tiovan_backend/ /code/
COPY ./prod/dockerfiles/tiovan_backend/nginx.conf /etc/nginx/conf.d/app.conf
# COPY ./prod/letsencrypt/ /etc/letsencrypt
RUN apt-get update && apt-get install -y libpq-dev gcc 
# certbot python-certbot-nginx
RUN pip install -r requirements.txt
RUN pip install psycopg2 pillow
# RUN certbot --nginx -d tiovan-backend.ml ; certbot renew --dry-run
RUN apt-get autoremove -y gcc

# ENV STATIC_PATH /app/static
ENV STATIC_URL /code/static
ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
# ENV LISTEN_PORT=8000
# EXPOSE 443 8000 80

ENV UWSGI_INI /code/uwsgi.ini


# URL under which static (not modified by Python) files will be requested
# They will be served by Nginx directly, without being handled by uWSGI
# Absolute path in where the static files wil be