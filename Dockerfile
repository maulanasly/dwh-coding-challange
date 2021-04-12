FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /solution

WORKDIR /solution

ADD requirements.txt /solution/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

ADD . /solution/

RUN chmod +x /solution/runner.py

CMD [runner.py]