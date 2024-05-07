# Parquet ファイル

## S3 からロードする

[s3fs](https://s3fs.readthedocs.io/en/latest/api.html)

```py
import pyarrow.parquet as pq
import s3fs

path = "s3://lafoglia-devel-dms/main/lafogliadb/purchases_purchase/2024/04/18/20240418-042945603.parquet"

s3 = s3fs.S3FileSystem()

pandas_dataframe = pq.ParquetDataset(
    path,
    filesystem=s3
).read_pandas().to_pandas()
```
