FROM python:3.6.2
ADD requirements.txt /tmp/requirements.txt
RUN pip install uwsgi
RUN pip install -r /tmp/requirements.txt
ADD . /pylytics
WORKDIR /pylytics/tests

ENV PYTHONPATH /pylytics/src/
CMD ["python", "app.py"]

ENV HOME /pylytics/tests
WORKDIR /pylytics/tests

EXPOSE 5000
