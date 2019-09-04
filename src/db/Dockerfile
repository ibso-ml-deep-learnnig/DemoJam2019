# Derived from official mysql image (our base image)

FROM mysql

# Add a database
ENV MYSQL_DATABASE grpc
ENV MYSQL_ROOT_PASSWORD helloworld01
EXPOSE 8000
# Add the content of the ./sql/ directory to your image
# All scripts in docker-entrypoint-initdb.d/ are automatically

# executed during container startup
COPY ./sql/ /docker-entrypoint-initdb.d/