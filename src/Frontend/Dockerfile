FROM python:3.7

# get packages
WORKDIR /Frontend
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# add files into working directory
COPY . .

# set listen port
ENV PORT "5000"
ENV ACCOUNT_SERVICE_ADDR "account:50050"
ENV ASSET_SERVICE_ADDR "asset:50051"
ENV DB_SERVER_SERVICE_ADDR "db-server:8001"

EXPOSE 5000

ENTRYPOINT ["python", "/Frontend/frontend_server.py"]