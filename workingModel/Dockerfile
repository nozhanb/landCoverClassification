# Using ubunut:18.04 image

FROM ubuntu:18.04

RUN apt update && apt install python3 -y && apt install python3-pip -y && apt install nano

WORKDIR /app

# To install ping command and their ip related commands

#RUN apt-get install iputils-ping

# Install any needed packages specified in requirements.txt

COPY requirements.txt /app

RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

# Copy the current directory's contents into the /app directory
COPY . /app

# The following is the error message you will get when you do "flask run":
#"This system supports the C.UTF-8 locale which is recommended. You might be able to resolve your issue by exporting the following environment variables:"

#RUN export LC_ALL=C.UTF-8
#RUN export LANG=C.UTF-8

# The following line was added at Dec 2, 2019. I believe the image Ukba made did not include this line!!
ENV LANG C.UTF-8

# To run the flask run export flask variables:

RUN export FLASK_APP=api.py
RUN export FLASK_ENV=development

# We create a log file to keep the container alive

RUN touch /var/log/zookeeper.log

RUN echo "hey AI " > zookeeper.log

# Run app.py when the container launches

#ENTRYPOINT python3 app.py
#CMD /bin/bash 
EXPOSE 5000

CMD flask run --host=0.0.0.0
