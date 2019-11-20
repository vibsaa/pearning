'''import matplotlib.pyplot as plt
import numpy as np
import mplcursors

data = np.outer(range(10), range(1, 5))

fig, ax = plt.subplots()
lines = ax.plot(data)
ax.set_title("Click somewhere on a line.\nRight-click to deselect.\n"
             "Annotations can be dragged.")

mplcursors.cursor(lines) # or just mplcursors.cursor()

plt.show()

import string
import matplotlib.pyplot as plt
import mplcursors

fig, ax = plt.subplots()
ax.bar(range(9), range(1, 10), align="center")
labels = string.ascii_uppercase[:9]
ax.set(xticks=range(9), xticklabels=labels, title="Hover over a bar")

cursor = mplcursors.cursor(hover=True)
@cursor.connect("add")
def on_add(sel):
    x, y, width, height = sel.artist[sel.target.index].get_bbox().bounds
    sel.annotation.set(text=f"{x+width/2}: {height}", position=(0, 20))
    sel.annotation.xy = (x + width / 2, y + height)

plt.show()


import matplotlib.pyplot as plt
import numpy as np
import mplcursors

fig, axes = plt.subplots(ncols=2)

left_artist = axes[0].plot(range(11))
axes[0].set(title="No box, different position", aspect=1)

right_artist = axes[1].imshow(np.arange(100).reshape(10, 10))
axes[1].set(title="Fancy white background")

# Make the text pop up "underneath" the line and remove the box...
c1 = mplcursors.cursor(left_artist)
@c1.connect("add")
def _(sel):
    sel.annotation.set(position=(15, -15))
    # Note: Needs to be set separately due to matplotlib/matplotlib#8956.
    sel.annotation.set_bbox(None)

# Make the box have a white background with a fancier connecting arrow
c2 = mplcursors.cursor(right_artist)
@c2.connect("add")
def _(sel):
    sel.annotation.get_bbox_patch().set(fc="white")
    sel.annotation.arrow_patch.set(arrowstyle="simple", fc="white", alpha=.5)

plt.show()'''

import matplotlib.pyplot as plt
import numpy as np
import mplcursors

data = np.outer(range(10), range(1, 5))

fig, ax = plt.subplots()
ax.set_title("Multiple non-draggable annotations")
ax.plot(data)

mplcursors.cursor(multiple=True).connect(
    "add", lambda sel: sel.annotation.draggable(False))

plt.show()
