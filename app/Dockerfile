FROM python:3.11-slim

WORKDIR /opt/app

ENV PYTHONPATH="/opt/app"  

COPY ./requirements.txt /opt/app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /opt/app/

CMD ["sh", "-c", "sleep 3600"]