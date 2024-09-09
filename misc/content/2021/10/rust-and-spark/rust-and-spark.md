Status: published
Date: 2021-10-10 23:58:37
Modified: 2021-12-05 12:59:56
Author: Benjamin Du
Slug: rust-and-spark
Title: Rust and Spark
Category: Computer Science
Tags: Computer Science, programming, Rust, Spark, big data, distributed, PySpark, pandas_udf, Shell, subprocess

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


The simplest and best way is to leverage `pandas_udf` in PySpark.
In the pandas UDF, 
you can call `subprocess.run` to run any shell command 
and capture its output.

    :::python
    from pathlib import Path
    import subprocess as sp
    import pandas as pd

    CMD = "./pineapple test --id1-path {} --htype1 3 --n0 2 --n2 5 --ratio2 0.001"


    def run_cmd(cmd: str) -> str:
        try:
            proc = sp.run(cmd, shell=True, check=True, capture_output=True)
        except sp.CalledProcessError as err:
            print(f"Here: {err}\nOutput: {err.stdout}\nError: {err.stderr}")
            print("Content of Directory:")
            for p in Path(".").glob("*"):
                print(f"    {p}")
            raise err
        return proc.stdout.strip().decode()


    @pandas_udf("string", PandasUDFType.SCALAR)
    def test_score_r4(id1):
        path = Path(tempfile.mkdtemp()) / "id1.txt"
        path.write_text("\n".join(str(id_) for id_ in id1))
        output = run_cmd(CMD.format(path))
        return pd.Series(output.split())

## References

- [Spark and Rust - How to Build Fast, Distributed and Flexible Analytics Pipelines with Side Effects](https://blog.phylum.io/spark-and-rust-how-to-build-fast-distributed-and-flexible-analytics-pipelines)
