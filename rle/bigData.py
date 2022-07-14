import xclim 
import xarray as xr
import numpy as np
import xclim.indices as xci

def get_task_n(da):
    return len(da.__dask_graph__().keys())


file = "/tank/smith/espo-r5_temp/day_CCCma_CanESM2_CCCma_CanRCM4_rcp45_1950-2100.zarr"
ds = xr.open_zarr(file)

print(ds)

# res = xclim.indices.run_length.rle(da, index = "last")
# print(get_task_n(res))

