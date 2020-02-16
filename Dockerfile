FROM python:3
ENV PYTHONUNBUFFERED 1
ADD . /application
WORKDIR /application
COPY requirements.txt /application/
RUN pip install -r requirements.txt