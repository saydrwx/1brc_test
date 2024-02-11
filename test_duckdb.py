"""
https://rmoff.net/2024/01/03/1%EF%B8%8F%E2%83%A3%EF%B8%8F-1brc-in-sql-with-duckdb/
"""

import duckdb
import time

def create_duckdb_relation():
    return duckdb.sql("""
            SELECT 
                station_name,
                MIN(measurement) AS min_measurement,
                CAST(AVG(measurement) AS DECIMAL(8,1)) AS mean_measurement,
                MAX(measurement) AS max_measurement
            FROM READ_CSV('/app/data/measurements.txt', header=false, columns= {'station_name':'VARCHAR','measurement':'double'}, delim=';')
            GROUP BY station_name
            ORDER BY station_name
        """)

if __name__ == "__main__":
    start_time = time.time()
    rel = create_duckdb_relation()
    print(rel.show())
    took = time.time() - start_time
    print(f"DuckDB took: {took:.2f} sec")
