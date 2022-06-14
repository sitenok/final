FROM ubuntu:22.04

RUN apt update && apt -y upgrade
RUN apt install -y git python3 python3-pip curl

RUN pip3 install fastapi
RUN pip3 install uvicorn

WORKDIR /root
RUN git init
RUN git clone https://github.com/sitenok/RESTapis

WORKDIR /root/nicole-oss-assignment3
EXPOSE 8080
CMD ["uvicorn", "main:app1", "--reload", "port=8080"]