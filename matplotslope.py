import numpy as np
import matplotlib.pyplot as plt

from mpltools import annotation




ax4.loglog(x, x**0.5)
annotation.slope_marker((10, 2), 0.5, ax=ax4)
ax4.set_title('loglog, float slope')

plt.tight_layout()
plt.show()