import sys
sys.path.insert(0,'/VideoCapture')

from VideoCapture import Device
import numpy as np

from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg

cam = Device()
im = cam.getImage()


app = QtGui.QApplication([])

## Create window with ImageView widget
win = QtGui.QMainWindow()
win.resize(480,640)
imv = pg.RawImageWidget()
win.setCentralWidget(imv)
win.show()
win.setWindowTitle('pyqtgraph example: ImageView')

def update():
    global imv, cam
    im = cam.getImage()
    pix = np.asarray(im)
    r = pix[:,:,2]

    imv.setImage(r)
timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(0)




## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()


