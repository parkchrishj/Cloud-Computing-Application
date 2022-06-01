FROM python:3.7-slim-buster

RUN apt-get update

RUN apt-get install -y build-essential

WORKDIR /app
Copy requirements.txt .
RUN python3 -m pip install -r requirements.txt
CMD ["python3", "classify.py"]
