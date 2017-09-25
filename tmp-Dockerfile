FROM python:3.6.2
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
ADD . /pylytics
WORKDIR /pylytics/tests
EXPOSE 5000
ENV PYTHONPATH /pylytics/src/
#CMD ["python", "-m","unittest","test_inputFileProcessor.py"]
CMD ["python", "app.py"]
