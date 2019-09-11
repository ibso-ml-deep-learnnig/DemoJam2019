FROM node:12

RUN GRPC_HEALTH_PROBE_VERSION=v0.2.0 && \
    wget -qO/bin/grpc_health_probe https://github.com/grpc-ecosystem/grpc-health-probe/releases/download/${GRPC_HEALTH_PROBE_VERSION}/grpc_health_probe-linux-amd64 && \
    chmod +x /bin/grpc_health_probe

# create app directory
WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY  . .

ENV PORT "50051"

EXPOSE 50051

CMD [ "node", "./src/front2asset-server.js" ]