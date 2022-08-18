# Notebook setup
import xarray as xr
import matplotlib.pyplot as plt
import netCDF4
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from argopy import DataFetcher as ArgoDataFetcher
# Load the dataset using xarray
argo_loader = ArgoDataFetcher(src='erddap', cache=True, cachedir='tmp')
apDS = argo_loader.float(3902004).load().data

ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([25, 42, 36, 47]) #this one will be changed

# Basemaps
ax.coastlines('10m', linewidth=1)

ax.plot(apDS.LONGITUDE, apDS.LATITUDE, linewidth=3, color='royalblue');
plt.show()
