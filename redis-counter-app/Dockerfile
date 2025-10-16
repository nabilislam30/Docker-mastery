FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN apt-get update && apt-get install -y curl
RUN pip install -r requirements.txt
EXPOSE 5050
CMD ["python", "count.py"]