FROM node:12

# create app directory
WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY  . .

ENV PORT = 50051

EXPOSE 50051

CMD [ "node", "./src/front2asset-server.js" ]