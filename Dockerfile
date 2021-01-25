FROM mongo:latest

WORKDIR /usr/src/parsejson

COPY main.py .
COPY sample-data.json .
COPY README.md .
COPY run-parse-json.sh .

RUN apt-get update
RUN apt-get -y install python3
RUN apt-get -y install python3-pip
RUN pip3 install mongo

CMD ["/bin/sh","./run-parse-json.sh"]

