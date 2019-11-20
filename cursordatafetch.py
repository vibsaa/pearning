import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor, Button
from numpy import random

x, y = random.rand(2, 100)
fig, ax = plt.subplots()
p, = plt.plot(x, y, 'o')

cursor = Cursor(ax,
				horizOn=True, # Controls the visibility of the horizontal line
				vertOn=True, # Controls the visibility of the vertical line
				color='green',
				linewidth=2.0
				)
def onclick(event):
	x1, y1 = event.xdata, event.ydata
    print(x1, y1)
    
fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()