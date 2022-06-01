FROM python:3.6

RUN apt-get update

RUN apt-get install -y python3 python3-pip

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["python3", "classify.py"]

