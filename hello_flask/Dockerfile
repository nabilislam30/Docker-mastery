FROM python:3.13-slim

WORKDIR /app
COPY . /app

# Install Flask and MySQL connector
RUN pip install --no-cache-dir Flask==3.0.3 mysql-connector-python==9.0.0

EXPOSE 5002
CMD ["python", "app.py"]