FROM python:3.8.2-buster

# creating the directory so it's owned by the right user
RUN mkdir /simon/

# setting workdir so yarn can build in the right directory
WORKDIR /simon/

# copy all source in as we need everything to build the assets
COPY . /simon/
