FROM python:3

WORKDIR /db_server

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# add files into working directory
COPY . .

EXPOSE 8001
ENV PORT "8001"

ENTRYPOINT ["python", "/db_server/db_server.py"]