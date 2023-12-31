FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install Flask

EXPOSE 80

CMD ["python", "calculator.py"]
