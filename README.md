# Parse JSON Test Project

This script reads a JSON file with network traffic data and extracts the following values:

* Name
* CPU Time
* Memory Usage
* IP address
* Status
* Creation time


The values are then inserted as documents to a MongoDB and the application also retreives
the records from the dabatabse and prints it to the output. The application should retreive 
17 documents.

# System Requirements

* Python 3
* Mongo Python module
* Mongo database

# Prerequisites:

* JSON file : sample-json.json

* Mongodb to be up and runing. Failing to do this will cause the application to fail and
  display message 'Connection to the database failed'
  
# Docker image
A Dockerfile is available to create a docker image using the following command:

~~~~
docker build -t parsejson .
~~~~

The image is based on mongodb image
To run the dockerized solution, enter the following command:

~~~~
docker run parsejson
~~~~