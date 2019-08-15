FROM ubuntu:latest

RUN apt-get update && apt-get install python3-pip -y

COPY plugin1.py .

COPY plugin.csv .

RUN pip3 install jenkinsapi

ENTRYPOINT ["/usr/bin/python3","plugin1.py"]
