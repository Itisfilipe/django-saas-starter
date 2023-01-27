FROM node:18.13.0-slim

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Install application into container
COPY . /usr/src/app

# set work directory
WORKDIR /usr/src/app/assets

RUN npm install
