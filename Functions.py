
from math import pi
import numpy as np


def Sph(x):
       
    x = np.asarray_chkfinite(x)  
    return sum(x*np.transpose(x))

def Ack(x, a=20, b=0.2, c=2*pi):
        
    x = np.asarray_chkfinite(x)  
    n = len(x)
    s1 = sum( x**2 )
    s2 = sum( np.cos( c * x ))
    return -a * np.exp(-b*np.sqrt( s1 / n )) - np.exp( s2 / n ) + a + np.exp(1)

def SS(x):
    x = np.asarray_chkfinite(x)  
    for i in range(0,3):
        SUM=sum(x*np.transpose(x)+i**2)
    return SUM
