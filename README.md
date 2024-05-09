# test-api
Test API using Python and Flask



Run locally:

* Set up venv using your default Python
* pip install flask
* export FLASK_APP=application.py
* flask run

Run in container:

Tested using WSL (22.04), Docker Desktop with integration

* docker-compose build
* docker-compose up web

Easiest to run in Windows 11 with .wslconfig set to networkingMode=mirrored
Access the service at 127.0.0.1 (note NOT 5000 here) on local machine



