FROM python:3.10

WORKDIR /data

COPY . /data/

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80" ]