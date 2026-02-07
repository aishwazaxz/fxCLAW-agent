FROM python:3.10-slim

WORKDIR /app

COPY main.py .

CMD ["python", "main.py"]
