
from PySide import QtGui, QtCore
import pyqtgraph as pg
import pyaudio
import sys
import numpy as np


chunk = 2048
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS, 
                rate=RATE, 
                input=True,
                output=True,
                frames_per_buffer=chunk)

  
    

# declare the GUI
app = QtGui.QApplication([])
win = pg.GraphicsWindow(title="ThinkRF FFT Plot Example")
win.resize(1000,600)
win.setWindowTitle("PYRF FFT Plot Example")

# initialize time domain plot
audio_plot = win.addPlot(title="Power Vs. Frequency")

# initialize frequency plot
fft_plot = win.addPlot(title="Power Vs. Frequency")

curve = audio_plot.plot(pen='g')

fft_curve = fft_plot.plot(pen='g')
def update():
    global stream, curve, fft_curve 
    
    # read data

    raw_data = stream.read(chunk)
    data = np.frombuffer(raw_data, dtype = np.int32)
    windowed_data = data * np.hanning(len(data))
    p = 20*np.log10(np.abs(np.fft.rfft(windowed_data)))
    
    curve.setData(data, pen = 'g')
    fft_curve.setData(p, pen = 'g')
timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(0)



## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
    stream.stop_stream()
    stream.close()
    p.terminate()
