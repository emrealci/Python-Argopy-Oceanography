"""
we can plot specific cycle graphs of any float we want
first we got all the properties of a float we wanted and we learned its cycle number
then plot this float  with cycle number
ax[0] --> first column
ax[1] --> second column
ax[2] --> third column

...
wualfabre
...

"""
import numpy as np
import xarray as xr
import netCDF4
xr.set_options(display_style="html", display_expand_attrs=False);
from matplotlib import pyplot as plt
from argopy import DataFetcher as ArgoDataFetcher

def cycle_number():
    argo_loader = ArgoDataFetcher(src='erddap', cache=True, cachedir='tmp')
    apDS = argo_loader.float(6904222).load().data
    data = apDS.argo.point2profile()
    cycle = []
    cycle = data.CYCLE_NUMBER
    c = int(cycle[len(cycle) - 1])  # c miz artık cycle sayısı
    return c

number=cycle_number()
print(number)

argo_loader = ArgoDataFetcher(src='erddap', cache=True, cachedir='tmp')
fig, ax = plt.subplots(1,2*number,figsize=(8,10))
k=0
j=1

while(number>0):
    argo_loader = argo_loader.profile(6904222,j).load()
    apDS2 = argo_loader.data
    data = apDS2.argo.point2profile()

    # Temperature
    ax[k].plot(data.TEMP[0], -data.PRES[0], 'b-', label='N_PROF=0')
    ax[k].set_title(data.TEMP.long_name)
    ax[k].set_ylabel(data.PRES.long_name)
    ax[k].grid()
    ax[k].legend()

    # Salinity
    ax[k + 1].plot(data.PSAL[0], -data.PRES[0], 'b-', label='N_PROF=0')
    ax[k + 1].set_title(data.PSAL.long_name)
    ax[k + 1].grid()
    number = number - 1
    k=k+2
    j=j+1
plt.show()
