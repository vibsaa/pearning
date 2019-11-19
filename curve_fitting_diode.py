
from numpy import *
from scipy.optimize import leastsq
 
def diode_res(args, T, V, I):
    '''
    Shockley diode equation with series resistor residual
 
    @param n emission coefficient [unitless]
    @param Rs series resistance [ohms]
    @param Is saturation current [A]
    @param T reference temperature [K]
    @param V voltage across diode [V]
    @param I current through diode [A]
     
    @return I*Rs+log(I/Is+1)*n*k*T-V
    '''
    n, Rs, Is = args
    kb = 8.617332478e-5
    return I*Rs+log(I/Is+1)*n*kb*T-V
 