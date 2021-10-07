FROM python:3.8

ADD /app.py

RUN pip install selenium
RUN pip install flask

CMD["python3","./app.py"]
