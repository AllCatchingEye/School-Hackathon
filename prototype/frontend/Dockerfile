FROM node:lts-alpine

RUN npm install -g npm@8.7.0

WORKDIR /frontend

COPY package*.json ./
RUN npm install -g @vue/cli@next
RUN npm install @vue/cli-service-global
RUN npm install -g --unsafe-perm=true 
RUN vue upgrade --next
COPY . .
RUN chown -R node:985 node_modules
ENTRYPOINT [ "vue", "serve", "--","--port", "5000"]