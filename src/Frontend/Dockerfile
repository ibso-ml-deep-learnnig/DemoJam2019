FROM python:3

# get packages
WORKDIR /app_frontend
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# add files into working directory
COPY . .

# set listen port
ENV PORT "5000"
EXPOSE 5000

ENTRYPOINT ["python", "/Frontend/frontend_server.py"]