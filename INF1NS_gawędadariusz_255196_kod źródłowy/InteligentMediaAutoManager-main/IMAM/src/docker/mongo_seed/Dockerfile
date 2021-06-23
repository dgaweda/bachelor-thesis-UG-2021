# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /mongo_seed

# install dependencies
RUN pip install pymongo

# copy the content of the local src directory to the working directory
COPY . .

# command to run on container start
CMD [ "python", "database.py" ]