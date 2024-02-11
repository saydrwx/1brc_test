"""
https://github.com/Butch78/1BillionRowChallenge/blob/main/python_1brc/main.py
"""

import polars as pl
import time

def create_polars_df():
    pl.Config.set_streaming_chunk_size(4000000)
    return (
        pl.scan_csv(
            "/app/data/measurements.txt",
            separator=";",
            has_header=False,
            new_columns=["station", "measure"],
            schema={"station": pl.String, "measure": pl.Float64}
        )
        .group_by("station")
        .agg(
            max = pl.col("measure").max(),
            min = pl.col("measure").min(),
            mean = pl.col("measure").mean()
        )
        .sort("station")
        .collect(streaming=True)
    )

if __name__ == "__main__":
    start_time = time.time()
    df = create_polars_df()
    took = time.time() - start_time
    print(df.head())
    print(f"Polars took: {took:.2f} sec")
