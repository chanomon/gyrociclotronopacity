import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from math import exp
import matplotlib as mpl
from time import gmtime, strftime

hora = strftime("%H:%M:%S", gmtime())

mpl.rcParams["savefig.directory"] = './'

def func(nu,a,A,b,B):
    return (A * nu**a)*(1.0-np.exp(-B* (nu**(-b))))

xdata = [2.6,3.21,3.41,4.01,1.8,1.4,1.6,2.01,2.21,3.02,4.33,2.4,4.62,4.9,5.2,5.51,5.81,6.23,6.63,7.01,7.53,8.04,8.53,8.97,9.56,10.,10.6,11.2,12.,13.1,14.1,15.,16.,17.]#utilizando digitizeit#,
ydata= [0.341,0.51,0.599,0.651,.0444,.583,.704,1.08,1.014,.859,1.31,1.83,3.17,3.41,4.96,7.76,10.1,10.5,15.6,16.9,17.1,19.3,19.6,16.6,14.1,12.8,10.4,9.86,8.63,6.27,5.19,3.51,3.99,2.58]


#np.random.seed(1729)

#y_noise = 0.2 * np.random.normal(size=xdata.size)

#ydata = y + y_noise
fig = plt.figure()
ax1 = plt.subplot(111)
plt.plot(xdata, ydata, 'bs',label='data')


popt, pcov = curve_fit(func, xdata, ydata,bounds=([6.,0.,8.,1e3],[6.5,25.,20.0,1.5e7]))

print(popt,pcov)

plt.plot(xdata, func(xdata, *popt), 'r-', label='fit: a=%5.4f, A=%0.6f, b=%5.3f,B=%5.3f' % tuple(popt))

ax1.set_yscale('log')
ax1.set_xscale('log')
plt.xlabel('frec [GHz]')
plt.ylabel('Flux density [SFU]')
plt.title('bounds=([6.,0.,8.,1e3],[6.5,25.,20.0,1.5e7]')
plt.legend()
plt.show()
