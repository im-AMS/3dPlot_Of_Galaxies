from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import numpy as np
from astropy import units as u
from astropy.coordinates import SkyCoord
import pandas as pd
from scipy.constants import c
import pyqtgraph as pg

from scipy.interpolate import interp1d

pg.setConfigOptions(antialias=True)

app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.opts["distance"] = 1e6
w.show()
# g = gl.GLGridItem()
# w.addItem(g)


# df = pd.read_csv("MyResult_2020108.csv")
df = pd.read_csv("sorted.csv")
# df = pd.read_csv("merged.csv")
# df = pd.read_csv("MyTable_7_snigdha.csv")

ra = df.loc[:, "ra"].to_numpy()
dec = df.loc[:, "dec"].to_numpy()
redshift = df.loc[:, "redshift"].to_numpy()

# distance in kpc
dis = np.absolute(redshift * (c / 73))

data = SkyCoord(ra=ra * u.degree, dec=dec * u.degree, distance=dis * u.kpc)
# print(dec)
x = data.cartesian.x
y = data.cartesian.y
z = data.cartesian.z

x = np.array(x)
y = np.array(y)
z = np.array(z)
pos = np.dstack([x, y, z])


size = 0.5 * np.ones(pos.shape[1])

color = np.empty((pos.shape[1], 4))


def grad(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


max_dis = np.max(dis)
min_dis = np.min(dis)

# grad = interp1d([min_dis, max_dis], [0, 255])

for i, val in enumerate(dis):
    _grad = grad(x=val, in_max=max_dis, in_min=min_dis, out_max=255, out_min=0)
    # _grad = grad(val)
    color[i] = [255, _grad, 0, 0.9]


# sp = gl.GLScatterPlotItem(pos=pos, size=size, color=color, pxMode=False)
sp = gl.GLScatterPlotItem(pos=pos, size=size, pxMode=False)
w.addItem(sp)


# Start Qt event loop unless running in interactive mode.
if __name__ == "__main__":
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, "PYQT_VERSION"):
        QtGui.QApplication.instance().exec_()
