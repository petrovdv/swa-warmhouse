FROM python:3.11-alpine

WORKDIR /app

COPY . /app

RUN apk add --no-cache gcc musl-dev linux-headers && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del gcc musl-dev linux-headers

EXPOSE 8083

CMD ["gunicorn", "--bind", "0.0.0.0:8083", "app:app"]
