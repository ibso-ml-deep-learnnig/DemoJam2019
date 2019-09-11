FROM python:3

# download the grpc health probe
RUN GRPC_HEALTH_PROBE_VERSION=v0.3.0 && \
    wget -qO/bin/grpc_health_probe https://github.com/grpc-ecosystem/grpc-health-probe/releases/download/${GRPC_HEALTH_PROBE_VERSION}/grpc_health_probe-linux-amd64 && \
    chmod +x /bin/grpc_health_probe

WORKDIR /db_server

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# add files into working directory
COPY . .

EXPOSE 8001
ENV PORT "8001"
ENV DB_ADDR "db"
ENV DB_PORT "3306"

ENTRYPOINT ["python", "/db_server/db_server.py"]