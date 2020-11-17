from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import numpy as np

app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.show()
g = gl.GLGridItem()
w.addItem(g)


num = 100
# x, y, z = np.meshgrid(np.arange(0, num), np.arange(0, num), np.arange(0, num))
# x=x.reshape(-1)
# y=y.reshape(-1)
# z=z.reshape(-1)
# pos = np.array([[i, j, k] for i in x for j in y for k in z], dtype=np.float32)
# x, y = np.meshgrid(np.arange(0, num), np.arange(0, num))
# pos = np.dstack([x,x,x])
# print(pos)
pos = np.array([[x, y, z] for x in range(num) for y in range(num) for z in range(num)])
color = np.ones((len(pos), 4), dtype=np.float32)
size = np.ones(len(pos))
sp = gl.GLScatterPlotItem(pos=pos, color=color, size=size)
w.addItem(sp)


## Start Qt event loop unless running in interactive mode.
if __name__ == "__main__":
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, "PYQT_VERSION"):
        QtGui.QApplication.instance().exec_()
