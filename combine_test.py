from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import numpy as np
from astropy import units as u
from astropy.coordinates import SkyCoord

app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.show()
g = gl.GLGridItem()
w.addItem(g)

points = 800000
ra = np.random.randint(360, size=(points))
dec = np.random.randint(-90, 90, size=(points))
distance = np.random.randint( 500,1200, size=(points))

data = SkyCoord(ra=ra * u.degree, dec=dec * u.degree, distance=distance * u.kpc)
# print(dec)
x = data.cartesian.x
y = data.cartesian.y
z = data.cartesian.z

x = np.array(x)
y = np.array(y)
z = np.array(z)
# pos = np.array([[i, j, k] for i in x for j in y for k in z])
pos = np.dstack([x, y, z])
# print(pos)

size =  np.ones(len(pos))
color = np.ones((points, 4), dtype=np.float32)
sp = gl.GLScatterPlotItem(pos=pos, color=color, size=size)
w.addItem(sp)


## Start Qt event loop unless running in interactive mode.
if __name__ == "__main__":
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, "PYQT_VERSION"):
        QtGui.QApplication.instance().exec_()
