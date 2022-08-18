#we choose the spesific date what we want. Also we selected spesific location (E-W-N-S)
#since this time interval is less than the time in the previous code, the floats in the figure are sparse.

from argopy import DataFetcher as ArgoDataFetcher
from argopy import IndexFetcher as ArgoIndexFetcher
from matplotlib import pyplot as plt
argo_loader = ArgoDataFetcher()

#request data for a specific space/time domain:

ds = argo_loader.region([25,43,36.,47.,0,10.]).to_xarray()
ds = argo_loader.region([25,43,36.,47,0,1000.,'2022-03-10','2022-12-17']).to_xarray()


#for one or a collection of floats:
ds = argo_loader.float(6902746).to_xarray()
ds = argo_loader.float([6902746, 6902747, 6902757, 6902766]).to_xarray()

#By default fetched data are returned in memory as xarray.DataSet. From there, it is easy to convert it to other formats like a Pandas dataframe:
ds = ArgoDataFetcher().profile(6902746, 34).to_xarray()
df = ds.to_dataframe()

#ERDDAP is a data server that gives you a simple, consistent way to download subsets of scientific datasets in common file formats and make graphs and maps.
#This particular ERDDAP installation has oceanographic data
index_loader = ArgoIndexFetcher()
index_loader = ArgoIndexFetcher(backend='erddap')
# Local ftp backend
# index_loader = ArgoIndexFetcher(backend='localftp',path_ftp='/path/to/your/argo/ftp/',index_file='ar_index_global_prof.txt')
#set the index request index for a domain:
idx=index_loader.region([25,43,36.,47.])
idx=index_loader.region([25,43,36.,47.,'2022-03-10','2022-03-17'])

idx.to_dataframe()
idx.to_xarray()
idx.plot('trajectory')
idx.plot('dac')
idx.plot('profiler')
plt.show()
