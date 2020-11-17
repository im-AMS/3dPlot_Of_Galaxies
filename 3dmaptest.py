from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import numpy as np

app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.opts["distance"] = 20
w.show()
w.setWindowTitle("pyqtgraph example: GLScatterPlotItem")

g = gl.GLGridItem()
w.addItem(g)

end = 5
# x,y,z=np.meshgrid(np.arange(0,end),np.arange(0,end),np.arange(0,end))
# z=np.zeros(5)
# pos=np.zeros((end,3))
# pos=(*x,*y,*z)
# x = np.arange(0, end)
# y = z = x
# pos=np.zeros((end,3))
# for u,i,j,k in range(end),x,y,z:
# pos[u]=(i,j,k)

# pos=
# print(pos)
# pos=np.empty((end*3,3))
# for i in range(end*3):
# pos[i]=(x[i],y[i],z[i])

pos = np.empty((10, 3))
pos[0] = (1, 0, 0)
pos[1] = (0, 1, 0)
pos[2] = (0, 0, 1)

# pos = np.array([
#     x,y,0
# ]for n,x in enumerate(range(3)) for m,y in enumerate(range(3))
# )
size = 1.5 * np.ones((2))

print(pos)

sp1 = gl.GLScatterPlotItem(pos=pos, size=size, color=(1.0, 0.0, 0.0, 0.5), pxMode=False)
sp1.translate(5, 5, 0)
w.addItem(sp1)

if __name__ == "__main__":
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, "PYQT_VERSION"):
        QtGui.QApplication.instance().exec_()
