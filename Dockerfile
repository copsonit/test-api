#
# test-API Dockerfile
#
#

# Pull base image.
FROM python

# make a local directory
RUN mkdir /opt/test-api

# set "test-api" as the working directory from which CMD, RUN, ADD references
WORKDIR /opt/test-api

# now copy all the files in this directory to ./
COPY requirements.txt ./

# pip install the local requirements.txt
RUN pip install -r requirements.txt

# Add all files
ADD . .

# Listen to port 5000 at runtime
EXPOSE 5000

# Add the startup file to be able to start server with run flask run
ENV FLASK_APP=application.py

# start the app server on all available addresses (0.0.0.0)
CMD "flask" "run" "--host=0.0.0.0"