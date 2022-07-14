import xclim 
import xarray as xr
import numpy as np
import xclim.indices as xci

def get_task_n(da):
    return len(da.__dask_graph__().keys())
# da = xr.DataArray(
#     [False, True, True, True, False, False], dims=("time")
# )
n_l = 10
n_t = 100
da = xr.DataArray([[np.sin(i+j)>0 for i in range(n_l)] for j in range(n_t)], dims=["time","lat"])
da = da.chunk({'lat': -1})

res = xclim.indices.run_length.rle(da, index = "last")
print(get_task_n(res))
