FROM python:3.11.8-slim-bookworm

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r /app/requirements.txt

COPY test_polars.py test_duckdb.py run.sh /app/
CMD ["/bin/bash", "./run.sh"]
