FROM node:12

# create app directory
WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY  . .

EXPOSE 50051

CMD [ "node", "./src/front2asset-server.js" ]