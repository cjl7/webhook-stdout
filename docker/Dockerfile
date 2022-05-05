FROM python:alpine3.15

WORKDIR .
COPY requirements.txt /
COPY app.py /
RUN pip install -r requirements.txt
CMD python app.py

