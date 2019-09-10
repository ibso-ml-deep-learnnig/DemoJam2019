FROM node:12

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY . .

ENV PORT = 50065

EXPOSE 50065

CMD [ "node", "./src/tokenService.js" ]