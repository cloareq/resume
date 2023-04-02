FROM python:3.10-slim-buster

RUN apt-get update \
    && apt-get install -y \
        libpq-dev \
        libxml2-dev \
        libxslt-dev \
        libjpeg-dev \
        libopenjp2-7-dev \
        wkhtmltopdf \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "python", "app.py" ]
