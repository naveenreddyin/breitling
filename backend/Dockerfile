FROM python:3.9.10

WORKDIR /app

RUN apt-get update \
    && apt-get install -y libpq-dev curl gdal-bin \
    && apt-get clean all \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . .
EXPOSE 8080
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8080", "--reload", "--log-level", "info"]

