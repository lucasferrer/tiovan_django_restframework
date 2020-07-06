FROM nginx
COPY ./prod/dockerfiles/tiovan_backend/nginx.conf /etc/nginx/conf.d/nginx.conf


# ENV STATIC_PATH /app/static
ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
# ENV LISTEN_PORT=8000
# EXPOSE 443 8000 80