# syntax=docker/dockerfile:1

FROM ubuntu:20.04

WORKDIR /user/src/app

# install necesasary tools for flask
RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip install flask[async]

# ai tools
RUN apt install git -y
RUN pip install git+https://github.com/huggingface/transformers.git 
RUN pip install torch 
RUN pip install transformers 

COPY . .

EXPOSE 5000

CMD ["python3", "app.py"]