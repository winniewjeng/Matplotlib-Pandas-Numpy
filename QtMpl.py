
import PyQt5
import matplotlib
import matplotlib.pyplot
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg


class QtMpl(FigureCanvasQTAgg):

    '''
    '''

    def __init__(self, parent):
        self.fig = matplotlib.figure.Figure()
        self.setParent(parent)
        FigureCanvasQTAgg.__init__(self, self.fig)

