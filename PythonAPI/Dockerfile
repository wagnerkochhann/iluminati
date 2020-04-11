FROM python:3.8-rc-slim

COPY PythonAPI/app.py /app.py
COPY PythonAPI/routes /routes

COPY PythonAPI/requirements.txt /app/requirements.txt

RUN pip3 install -r /app/requirements.txt

EXPOSE 5000
