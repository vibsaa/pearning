import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor, Button
from numpy import random
i=0
x, y = random.rand(2, 100)
fig, ax = plt.subplots()
p, = plt.plot(x, y, 'o')

cursor = Cursor(ax,
				horizOn=True, # Controls the visibility of the horizontal line
				vertOn=True, # Controls the visibility of the vertical line
				color='green',
				linewidth=2.0
				)
def onclick1(event):
	#for i in range (0,2):
	x[1] = event.xdata
	y[1]= event.ydata
	print(f'x1={x[1]}, y1={y[1]}')
def onclick2(event):
	#for i in range (0,2):
	x[2] = event.xdata
	y[2] = event.ydata
	print(f'x2={x[2]}, y2={y[2]}')
def slopept1():  
	cid1 = fig.canvas.mpl_connect('button_press_event', onclick1)
	fig.canvas.mpl_disconnect(cid1)
	#cid2 = fig.canvas.mpl_connect('button_press_event', onclick2)
	#ig.canvas.mpl_disconnect(cid2)
def slopept2():  
	#cid1 = fig.canvas.mpl_connect('button_press_event', onclick1)
	#fig.canvas.mpl_disconnect(cid1)
	cid2 = fig.canvas.mpl_connect('button_press_event', onclick2)
	fig.canvas.mpl_disconnect(cid2)	
	#fig.canvas.mpl_connect('button_press_event', onclick2)
slopept1()
slopept2()
plt.show()


