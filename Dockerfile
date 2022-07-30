FROM library/python:3.7-slim

COPY . /app/

WORKDIR /app

RUN pip3.7 install -r requirements.txt

CMD ["python3", "-u", "main.py"]