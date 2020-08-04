import numpy as np
import matplotlib.pyplot as plt
t = np.arange(0., 2., 0.1)
line, = plt.plot(t,t,'g^', picker=6)

def click(event):
    artist = event.artist
    ind = event.ind[0]
    xd = artist.get_xdata()[:ind]
    yd = artist.get_ydata()[:ind]
    print( tuple(zip(xd, yd)) )

cid = plt.gcf().canvas.mpl_connect("pick_event", click)

plt.show()