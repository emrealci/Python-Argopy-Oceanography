from argopy import IndexFetcher as ArgoIndexFetcher
from matplotlib import pyplot as plt

#functions
def trajectory():
    figure = idx.plot('trajectory')
    return figure

def dac():
    figure = idx.plot('dac')
    return figure

def profiler():
    figure = idx.plot('profiler')
    return figure
#main
index_loader = ArgoIndexFetcher()
index_loader = ArgoIndexFetcher(backend='erddap')
idx = index_loader.region([25, 43, 36., 47.])
idx = index_loader.region([25, 43, 36., 47., '2022-03-10', '2022-03-17'])
str=input("")
if str=="trajectory":
    plt.show(block=trajectory())
if str=="dac":
    plt.show(block=dac())
if str=="profiler":
    plt.show(block=profiler())
