"""to plot data from a csv file"""
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np


style.use('ggplot')

x,y = np.loadtxt('data123.txt',
                 unpack=True,
                 delimiter = ',')

plt.scatter(x,y)

plt.title('CHARACTERSTIC CURVE')
plt.ylabel('Id(Amperes)')
plt.xlabel('Vd(volts)')



plt.show()
