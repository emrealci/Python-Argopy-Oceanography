import numpy as np
import xarray as xr
import netCDF4
xr.set_options(display_style="html", display_expand_attrs=False);
from matplotlib import pyplot as plt
from argopy import DataFetcher as ArgoDataFetcher
argo_loader = ArgoDataFetcher(src='erddap', cache=True, cachedir='tmp')
argo_loader = argo_loader.profile(3902004,1).load()
apDS2 = argo_loader.data
data = apDS2.argo.point2profile()
fig, ax = plt.subplots(1,2,figsize=(8,10))

#Temperature
ax[0].plot(data.TEMP[0],-data.PRES[0],'b-',label='N_PROF=0')
ax[0].set_title(data.TEMP.long_name)
ax[0].set_ylabel(data.PRES.long_name)
ax[0].grid()
ax[0].legend()

#Salinity
ax[1].plot(data.PSAL[0],-data.PRES[0],'b-',label='N_PROF=0')
ax[1].set_title(data.PSAL.long_name)
ax[1].grid()
plt.show()
