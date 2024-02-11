# 1brc Python test

Benchmarking simple solutions of the One Billion Row Challenge in Python using duckDB and Polars

## Data generation
```bash
python ./data/create_measurements.py 1_000_000_000
```

## Running test
```bash
docker build --tag test-image .
docker run -v ./data:/app/data test-image
```

## Results
On Dell Latitude 7490 with Intel Core i5 8250U, 16GB of RAM and SATA6GB SSD
```bash
Polars took: 53.69 sec
DuckDB took: 131.25 sec
```
