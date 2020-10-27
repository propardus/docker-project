FROM python:3.9

WORKDIR /home/docker_project

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . ./

EXPOSE 5000
ENTRYPOINT python3 app.py
