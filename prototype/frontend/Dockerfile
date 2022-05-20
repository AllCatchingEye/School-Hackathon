FROM node:lts-alpine

WORKDIR /frontend

ENV PATH /frontend/node_modules/.bin:$PATH

COPY package.json ./
COPY package-lock.json ./

RUN npm install --silent

RUN npm install -g @vue/cli@next

COPY . ./
RUN chown -R node:node /frontend  
# ENTRYPOINT [ "vue", "serve", "--","--port", "5000"]