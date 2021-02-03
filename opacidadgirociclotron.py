import numpy as np
import matplotlib.pyplot as plt
from math import exp,sin,pi,cos,log
import matplotlib as mpl
from time import gmtime, strftime

hora = strftime("%H:%M:%S", gmtime())

mpl.rcParams["savefig.directory"] = './'

def eta(armnum,delta,teta):
    return log(3.3e-24 * 10**(-0.52*delta) *(sin(teta)**(-0.43-0.65*delta))*(armnum**(1.22-0.9*delta)))

def kappa(armnum,delta,teta):
    return log(1.4e-9 * 10**(-0.22*delta) *(sin(teta)**(-0.09+0.72*delta))*(armnum**(-1.3-0.98*delta)))


def Teff(armnum,delta,teta):
    return log(2.2e9 * 10**(-0.31*delta) *(sin(teta)**(-0.36-0.06*delta))*(armnum**(0.5+0.085*delta)))


def rc(armnum,delta,teta):
    return 0.20*10**(0.05*delta)*10**(1.93*cos(teta)-1.16*cos(teta)**2)*armnum**(-0.21-0.37*sin(teta))

def fpeak(delta,teta,NL,B):
    return 2.72*10e3 * 10**(0.27*delta)*sin(teta)**(0.41+0.03*delta)*(NL)**(0.32-0.03*delta) * B**(0.68+0.03*delta)

armnum = np.linspace(4,100,num=200)

etad3t40 =[eta(i,3,(2./9.)*pi) for i in armnum]
etad5t40 =[eta(i,5,(2./9.)*pi) for i in armnum]
etad7t40 =[eta(i,7,(2./9.)*pi) for i in armnum]

kappad3t40 = [kappa(i,3,(2./9.)*pi) for i in armnum]
kappad5t40 = [kappa(i,5,(2./9.)*pi) for i in armnum]
kappad7t40 = [kappa(i,7,(2./9.)*pi) for i in armnum]

Teffd3t40=[Teff(i,3,(2./9.)*pi) for i in armnum]  
Teffd5t40=[Teff(i,5,(2./9.)*pi) for i in armnum]
Teffd7t40=[Teff(i,7,(2./9.)*pi) for i in armnum]

rcd3t40= [rc(i,3,(2./9.)*pi) for i in armnum]
rcd5t40= [rc(i,5,(2./9.)*pi) for i in armnum]
rcd7t40= [rc(i,7,(2./9.)*pi) for i in armnum]

etad3t80 =[eta(i,3,(4./9.)*pi) for i in armnum]
etad5t80 =[eta(i,5,(4./9.)*pi) for i in armnum]
etad7t80 =[eta(i,7,(4./9.)*pi) for i in armnum]

kappad3t80 = [kappa(i,3,(4./9.)*pi) for i in armnum]
kappad5t80 = [kappa(i,5,(4./9.)*pi) for i in armnum]
kappad7t80 = [kappa(i,7,(4./9.)*pi) for i in armnum]

Teffd3t80=[Teff(i,3,(4./9.)*pi) for i in armnum]
Teffd5t80=[Teff(i,5,(4./9.)*pi) for i in armnum]
Teffd7t80=[Teff(i,7,(4./9.)*pi) for i in armnum]

rcd3t80=[rc(i,3,(4./9.)*pi) for i in armnum]
rcd5t80=[rc(i,5,(4./9.)*pi) for i in armnum]
rcd7t80=[rc(i,7,(4./9.)*pi) for i in armnum]

fig1 = plt.figure()
ax1 =  plt.subplot(111)
plt.plot(armnum,etad3t40,color='b',label='delta=3,teta=40')
plt.plot(armnum,etad5t40,color='r',label='delta=5,teta=40')
plt.plot(armnum,etad7t40,color='g',label='delta=7,teta=40')
plt.plot(armnum,etad3t80,linestyle='--',color='b',label='delta=3,teta=80')
plt.plot(armnum,etad5t80,color='r',linestyle='--',label='delta=5,teta=80')
plt.plot(armnum,etad7t80,color='g',linestyle='--',label='delta=7,teta=80')
plt.legend()
ax1.set_xscale('log')
plt.xlabel('numero armonico')
plt.ylabel('log(eta/BN)')

fig2 = plt.figure()
ax2 =  plt.subplot(111)
plt.plot(armnum,Teffd3t40,color='b',label='delta=3,teta=40')
plt.plot(armnum,Teffd5t40,color='r',label='delta=5,teta=40')
plt.plot(armnum,Teffd7t40,color='g',label='delta=7,teta=40')
plt.plot(armnum,Teffd3t80,linestyle='--',color='b',label='delta=3,teta=80')
plt.plot(armnum,Teffd5t80,color='r',linestyle='--',label='delta=5,teta=80')
plt.plot(armnum,Teffd7t80,color='g',linestyle='--',label='delta=7,teta=80')
plt.legend()
ax2.set_xscale('log')
plt.xlabel('numero armonico')
plt.ylabel('log(Teff)')

fig3= plt.figure()
ax3 =  plt.subplot(111)
plt.plot(armnum,kappad3t40,color='b',label='delta=3,teta=40')
plt.plot(armnum,kappad5t40,color='r',label='delta=5,teta=40')
plt.plot(armnum,kappad7t40,color='g',label='delta=7,teta=40')
plt.plot(armnum,kappad3t80,linestyle='--',color='b',label='delta=3,teta=80')
plt.plot(armnum,kappad5t80,color='r',linestyle='--',label='delta=5,teta=80')
plt.plot(armnum,kappad7t80,color='g',linestyle='--',label='delta=7,teta=80')
plt.legend()
ax3.set_xscale('log')
plt.xlabel('numero armonico')
plt.ylabel('log(kappaB/N)')

fig4 = plt.figure()
ax4=  plt.subplot(111)
plt.plot(armnum,rcd3t40,color='b',label='delta=3,teta=40')
plt.plot(armnum,rcd5t40,color='r',label='delta=5,teta=40')
plt.plot(armnum,rcd7t40,color='g',label='delta=7,teta=40')
plt.plot(armnum,rcd3t80,linestyle='--',color='b',label='delta=3,teta=80')
plt.plot(armnum,rcd5t80,color='r',linestyle='--',label='delta=5,teta=80')
plt.plot(armnum,rcd7t80,color='g',linestyle='--',label='delta=7,teta=80')
plt.legend()
ax4.set_xscale('log')
plt.xlabel('numero armonico')
plt.ylabel('rc')


print(rcd3t40[0])






plt.show()
