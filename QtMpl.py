
import PyQt5
import matplotlib
import matplotlib.pyplot
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg


class QtMpl(FigureCanvasQTAgg):
    """This class is in charge of the Matplotlib plotting!!!"""


    def __init__(self, parent):

        """
        Constructor
        """

        self.fig = matplotlib.figure.Figure()
        self.axes = self.fig.add_subplot(111)

        FigureCanvasQTAgg.__init__(self, self.fig)

        self.setParent(parent)

        self.axes.set_ylabel("Money")
        self.axes.set_xlabel("Dates")
        self.axes.set_title("Movie Revenue by Month")

        # define the widget as expandable
        FigureCanvasQTAgg.setSizePolicy(self,
                                        PyQt5.QtWidgets.QSizePolicy.Expanding,
                                        PyQt5.QtWidgets.QSizePolicy.Expanding)

        # notify the system of updated policy
        FigureCanvasQTAgg.updateGeometry(self)


    def addBars(self, x=None, revenue=None, budget=None, year=None):
        # clear the plot
        self.axes.cla()

        self.axes.set_title("Movie Revenue by Month for {}".format(year))

        self.axes.set_ylabel("Billions")  # need to reset it so it appears on screen

        revenue_bar = self.axes.bar(x=x, height=revenue, color='#67b6ea', label="Revenue")
        budget_bar = self.axes.bar(x=x, height=budget, color='#eedb71', label="Budget")

        self.axes.legend()
        self.fig.canvas.draw()
