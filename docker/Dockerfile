#FROM quay.io/devfile/python:slim
#FROM alpine:3.7
#FROM python:3-alpine
FROM python:3.8-slim-buster
# By default, listen on port 8081
EXPOSE 8081/tcp
ENV FLASK_PORT=8081

# Set the working directory in the container
WORKDIR /projects


# Copy the dependencies file to the working directory
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

#RUN apk add --update --no-cache-dir python3 py3-pip

#RUN apt-get update && apt-get install -y python-pip
# Install any dependencies
#RUN pip install -r requirements.txt


# Copy the content of the local src directory to the working directory
COPY . .

# Specify the command to run on container start
CMD [ "python", "./app.py" ]