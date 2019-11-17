from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

x,y = np.loadtxt('datapoints.txt',
                 unpack=True,
                 delimiter = ',')

plt.plot(x,y)

plt.title('CHARACTERSTIC CURVE')
plt.ylabel('Id(Amperes)')
plt.xlabel('Vd(volts)')

plt.show()
