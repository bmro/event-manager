FROM node:16.17.0-bullseye-slim
RUN apt-get update && apt-get install -y --no-install-recommends dumb-init
ENV NODE_ENV production
WORKDIR /usr/src/app

COPY --chown=node:node . .
RUN npm install -g http-server

USER node

CMD ["dumb-init", "http-server", ".", "-p 8000"]