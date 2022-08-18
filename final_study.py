"""
change the WMO of floats , see all the cyclies easily on different figures that makes it more understandable

attributes:

-find out how many cycles there are
-analyzing a graph of temperature and salinity for each cycle
-learning the cycle date on top of each cycle graph
-learning latitude and longitude
-if there is an error, find out which cycle is the problem

...
wualfabre
...

"""
import numpy as np
import xarray as xr
import netCDF4
import datetime
xr.set_options(display_style="html", display_expand_attrs=False);
from matplotlib import pyplot as plt
from argopy import DataFetcher as ArgoDataFetcher
o=5906516

def cycle_number():
    argo_loader = ArgoDataFetcher(src='erddap', cache=True, cachedir='tmp')
    apDS = argo_loader.float(o).load().data
    data = apDS.argo.point2profile()
    cycle = []
    cycle = data.CYCLE_NUMBER
    c = int(cycle[len(cycle) - 1])  # c miz artık cycle sayısı
    return c

def find_date():
    argo_loader = ArgoDataFetcher(src='erddap', cache=True, cachedir='tmp')
    apDS = argo_loader.float(o).load().data
    data = apDS.argo.point2profile()
    date1=[]
    date1=data.TIME
    return date1

def find_latitude():
    argo_loader = ArgoDataFetcher(src='erddap', cache=True, cachedir='tmp')
    apDS = argo_loader.float(o).load().data
    data = apDS.argo.point2profile()
    latitude=[]
    latitude=data.LATITUDE
    return latitude

def find_longitude():
    argo_loader = ArgoDataFetcher(src='erddap', cache=True, cachedir='tmp')
    apDS = argo_loader.float(o).load().data
    data = apDS.argo.point2profile()
    longitude=[]
    longitude=data.LONGITUDE
    return longitude

number=cycle_number()

number1=find_date()
number2=find_latitude()
number3=find_longitude()


print(number)


check_point=0
j=1
if number%4==0:
    while(True):
        print(check_point,int(number/4))


        if check_point==number/4:
            break

        argo_loader = ArgoDataFetcher(src='erddap', cache=True, cachedir='tmp')
        fig, ax = plt.subplots(nrows=2, ncols=4)
        z = 4  # 4 cycle on one figure
        k = 0  # temperature
        l = 1  # salinity
        m = 0  # buffer of temperature and salinity

        while(z>0):
            argo_loader = ArgoDataFetcher(src='erddap', cache=True, cachedir='tmp')
            argo_loader = argo_loader.profile(o,j).load()
            apDS2 = argo_loader.data
            data = apDS2.argo.point2profile()

            # Temperature
            ax[k,m].plot(data.TEMP[0], -data.PRES[0], 'b-', label='N_PROF=0')
            ax[k,m].set_title("SEA TEMPERATURE IN SITU\n{}. cycle\n{}\n latitude:{}\nlongitude{}".format(j,number1[j-1],number2[j-1],number3[j-1]))
            ax[k,m].set_ylabel(data.PRES.long_name)
            ax[k,m].grid()
            ax[k,m].legend()
            ax[k, m].set_ylim([-300, 0])

            # Salinity
            ax[l,m].plot(data.PSAL[0], -data.PRES[0], 'b-', label='N_PROF=0')
            ax[l,m].set_title(data.PSAL.long_name)
            ax[l,m].grid()
            ax[l, m].set_ylim([-300, 0])
            z=z-1
            j=j+1
            m=m+1

        check_point=check_point+1
elif number%4!=0:
    buffer=number
    while(True):

        argo_loader = ArgoDataFetcher(src='erddap', cache=True, cachedir='tmp')
        if buffer>4:
            fig, ax = plt.subplots(nrows=2, ncols=4)
            z = 4  # 4 cycle on one figure
            k = 0  # temperature
            l = 1  # salinity
            m = 0  # buffer of temperature and salinity

            while(z>0):
                argo_loader = ArgoDataFetcher(src='erddap', cache=True, cachedir='tmp')
                argo_loader = argo_loader.profile(o,j).load()
                apDS2 = argo_loader.data
                data = apDS2.argo.point2profile()

                # Temperature
                ax[k,m].plot(data.TEMP[0], -data.PRES[0], 'b-', label='N_PROF=0')
                ax[k,m].set_title("SEA TEMPERATURE IN SITU SCALE\n{}. cycle\n{}\n latitude:{}\nlongitude{}".format(j,number1[j-1],number2[j-1],number3[j-1]))
                ax[k,m].set_ylabel(data.PRES.long_name)
                ax[k,m].grid()
                ax[k,m].legend()
                ax[k, m].set_ylim([-300, 0])

                # Salinity
                ax[l,m].plot(data.PSAL[0], -data.PRES[0], 'b-', label='N_PROF=0')
                ax[l,m].set_title(data.PSAL.long_name)
                ax[l,m].grid()
                ax[l, m].set_ylim([-300, 0])
                z=z-1
                j=j+1
                m=m+1
            buffer = buffer - 4
        elif 0<buffer<4:
            fig, ax = plt.subplots(nrows=2, ncols=buffer)
            z = buffer   # 4 cycle on one figure
            k = 0  # temperature
            l = 1  # salinity
            m = 0  # buffer of temperature and salinity

            while (z > 0):

                argo_loader = ArgoDataFetcher(src='erddap', cache=True, cachedir='tmp')
                argo_loader = argo_loader.profile(o, j).load()
                apDS2 = argo_loader.data
                data = apDS2.argo.point2profile()

                # Temperature
                ax[k, m].plot(data.TEMP[0], -data.PRES[0], 'b-', label='N_PROF=0')
                ax[k, m].set_title("SEA TEMPERATURE IN SITU\n{}. cycle\n{}\n latitude:{}\nlongitude:{}".format(j,number1[j-1],number2[j-1],number3[j-1]))
                ax[k, m].set_ylabel(data.PRES.long_name)
                ax[k, m].grid()
                ax[k, m].legend()
                ax[k,m].set_ylim([-300,0])

                # Salinity
                ax[l, m].plot(data.PSAL[0], -data.PRES[0], 'b-', label='N_PROF=0')
                ax[l, m].set_title(data.PSAL.long_name)
                ax[l, m].grid()
                ax[l, m].set_ylim([-300, 0])
                z = z - 1
                j = j + 1
                m = m + 1
            buffer = buffer - 4

        else:
            break
        check_point=check_point+1

plt.show()
