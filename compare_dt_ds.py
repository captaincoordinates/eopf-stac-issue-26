import xarray as xr
from pystac_client import Client

print("fetching item")
client = Client.open("https://stac.core.eopf.eodc.eu/")
collection = client.get_collection(collection_id="sentinel-2-l2a")
item = collection.get_item(
    id="S2B_MSIL2A_20250522T125039_N0511_R095_T26TML_20250522T133252"
)
assert item is not None, "failed to fetch item"
dt_asset = item.assets["product"]
ds_sr10m_asset = item.assets["SR_10m"]

print("opening datatree")
dt = xr.open_datatree(
    dt_asset.href,
    **dt_asset.extra_fields[
        "xarray:open_datatree_kwargs"
    ],  # "xarray:open_datatree_kwargs": {"chunks": {}, "engine": "eopf-zarr", "op_mode": "native"}
)
print("opening dataset")
ds_sr10m = xr.open_dataset(
    ds_sr10m_asset.href,
    **ds_sr10m_asset.extra_fields[
        "xarray:open_dataset_kwargs"
    ],  # "xarray:open_dataset_kwargs": {"chunks": {}, "engine": "eopf-zarr", "op_mode": "native"}
)
print("gathering stats")
print("-----")
print(
    "from datatree, nbytes: {}".format(
        dt["/measurements/reflectance/r10m"].to_dataset().nbytes
    )
)  # 3858108480
print(
    "from datatree, dims: {}".format(
        len(dt["/measurements/reflectance/r10m"].to_dataset().dims)
    )
)  # 2
print("from dataset, nbytes: {}".format(ds_sr10m.nbytes))  # 0
print("from dataset, dims: {}".format(len(ds_sr10m.dims)))  # 0
