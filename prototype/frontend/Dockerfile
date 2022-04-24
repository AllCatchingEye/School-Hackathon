FROM node:lts-alpine

# install project dependencies
RUN npm install -g @vue/cli

# copy project files and folders to the current working directory (i.e. 'app' folder)
# ADD . /frontend

WORKDIR ./frontend/frontend
# vue ui --headless --port 8000 --host 0.0.0.0
ENTRYPOINT [ "vue", "serve", "--","--port", "5000"]
