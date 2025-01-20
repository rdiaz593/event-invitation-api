FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev gcc && \
    apt-get clean

COPY . /app
RUN pip install flask flask-sqlalchemy psycopg2-binary

CMD ["python", "app.py"]
