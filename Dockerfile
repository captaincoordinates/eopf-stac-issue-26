FROM python:3.13-slim

RUN pip install "pystac-client>=0.8.6,<1.0" "xarray==2025.6.1" "xarray-eopf==0.1.1"

COPY compare_dt_ds.py /compare_dt_ds.py

CMD ["python", "-m", "compare_dt_ds"]
