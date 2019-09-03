FROM python:3

# get packages
WORKDIR /app_frontend
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# add files into working directory
COPY . .

# set listen port
ENV PORT "5000"
ENV ACCOUNT_SERVICE_ADDR "account:50050"
ENV ASSET_CREATION_SERVICE_ADDR "assetcreation:50051"
ENV ASSET_DISPLAY)SERVICE_ADDR "assetdisplay:50053"

EXPOSE 5000

ENTRYPOINT ["python", "/Frontend/frontend_server.py"]