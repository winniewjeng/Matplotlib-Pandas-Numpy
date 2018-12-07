"""
This file handles holding the main GUI elements
"""

import PyQt5
import PyQt5.QtWidgets
import UI_MovieInfo
import QtMpl


class UI_CentralWindow(PyQt5.QtWidgets.QDialog):
    """
    This class holds the GUI elements
    """

    def __init__(self, parent=None):
        super(UI_CentralWindow, self).__init__(parent)

        # Create GUI Elements
        enterMovieLabel = PyQt5.QtWidgets.QLabel("Movie to Look up")
        self.enterMovieLineEdit = PyQt5.QtWidgets.QLineEdit()
        self.enterMoviePushButton = PyQt5.QtWidgets.QPushButton(
            "Look Up Movie")

        """
                # Create a mpl instance
                # self.mpl = QtMpl.QtMpl(parent)
                """
        self.mpl = QtMpl.QtMpl(parent=parent)

        """
        # add mpl to the bottom of the display
        # vbox.addLayout(self.mpl)  # ? 7-C

        """

        # Put into layout to view
        # vbox.addWidget(self.mpl)

        # Set up the various HBOX and VBOX
        hboxSearch = PyQt5.QtWidgets.QHBoxLayout()
        hboxInfo1 = PyQt5.QtWidgets.QHBoxLayout()
        hboxInfo2 = PyQt5.QtWidgets.QHBoxLayout()
        hboxInfo3 = PyQt5.QtWidgets.QHBoxLayout()
        hboxInfo4 = PyQt5.QtWidgets.QHBoxLayout()
        hboxInfo5 = PyQt5.QtWidgets.QHBoxLayout()

        hboxInfoAndPoster = PyQt5.QtWidgets.QHBoxLayout()
        vboxInfo = PyQt5.QtWidgets.QVBoxLayout()
        vbox = PyQt5.QtWidgets.QVBoxLayout()

        # hboxSearch is the layer for entering movie information
        # and running the search
        hboxSearch.addWidget(enterMovieLabel)
        hboxSearch.addWidget(self.enterMovieLineEdit)
        hboxSearch.addWidget(self.enterMoviePushButton)

        # hboxInfo is the layer for presenting the results from the search
        self.directorInformation = UI_MovieInfo.UI_MovieInfo(title="Director:")
        self.actorInformation = UI_MovieInfo.UI_MovieInfo(title="Lead Actor:")
        self.releaseDateInformation = UI_MovieInfo.UI_MovieInfo(
            title="Release Date:")

        self.budgetInformation = UI_MovieInfo.UI_MovieInfo(title="Budget:")
        self.revenueInformation = UI_MovieInfo.UI_MovieInfo(title="Revenue:")
        self.runTimeInformation = UI_MovieInfo.UI_MovieInfo(title="Run Time:")

        self.voteCountInformation = UI_MovieInfo.UI_MovieInfo(
            title="Vote Count:")
        self.voteAverageInformation = UI_MovieInfo.UI_MovieInfo(
            title="Vote Average:")
        self.statusInformation = UI_MovieInfo.UI_MovieInfo(title="Status:")

        self.monthlyRevenueMean = UI_MovieInfo.UI_MovieInfo(title="Monthly Revenue Mean:")
        self.monthlyRevenueMedian = UI_MovieInfo.UI_MovieInfo(title="Monthly Revenue Median:")
        self.monthlyRevenueStd = UI_MovieInfo.UI_MovieInfo(title="Monthly Revenue Std:")

        self.annualRevenueMean = UI_MovieInfo.UI_MovieInfo(title="Annual Revenue Mean:")
        self.annualRevenueMedian = UI_MovieInfo.UI_MovieInfo(title="Annual Revenue Median:")
        self.annualRevenueStd = UI_MovieInfo.UI_MovieInfo(title="Annual Revenue Std:")

        hboxInfo1.addLayout(self.directorInformation.getLayout())
        hboxInfo1.addLayout(self.actorInformation.getLayout())
        hboxInfo1.addLayout(self.releaseDateInformation.getLayout())

        hboxInfo2.addLayout(self.budgetInformation.getLayout())
        hboxInfo2.addLayout(self.revenueInformation.getLayout())
        hboxInfo2.addLayout(self.runTimeInformation.getLayout())

        hboxInfo3.addLayout(self.voteCountInformation.getLayout())
        hboxInfo3.addLayout(self.voteAverageInformation.getLayout())
        hboxInfo3.addLayout(self.statusInformation.getLayout())

        hboxInfo4.addLayout(self.monthlyRevenueMean.getLayout())
        hboxInfo4.addLayout(self.monthlyRevenueMedian.getLayout())
        hboxInfo4.addLayout(self.monthlyRevenueStd.getLayout())

        hboxInfo5.addLayout(self.annualRevenueMean.getLayout())
        hboxInfo5.addLayout(self.annualRevenueMedian.getLayout())
        hboxInfo5.addLayout(self.annualRevenueStd.getLayout())

        self.posterLabel = PyQt5.QtWidgets.QLabel("Poster Goes Here")
        self.pixmap = PyQt5.QtGui.QPixmap()

        self.awardsDisplay = PyQt5.QtWidgets.QTextEdit()
        self.awardsDisplay.setReadOnly(True)

        hboxInfoAndPoster.addWidget(self.posterLabel)
        hboxInfoAndPoster.addWidget(self.awardsDisplay)
        vboxInfo.addLayout(hboxInfo1)
        vboxInfo.addLayout(hboxInfo2)
        vboxInfo.addLayout(hboxInfo3)
        vboxInfo.addLayout(hboxInfo4)
        vboxInfo.addLayout(hboxInfo5)
        hboxInfoAndPoster.addLayout(vboxInfo)

        vbox.addLayout(hboxSearch)
        vbox.addLayout(hboxInfoAndPoster)
        vbox.addWidget(self.mpl)

        # Put into layout to view
        self.setLayout(vbox)
        return

    def updatePoster(self, posterFileName=None):
        """
        Display the poster in the GUI
        """
        self.pixmap.load(posterFileName)
        scaledPixmap = self.pixmap.scaled(self.posterLabel.size(),
                                          PyQt5.QtCore.Qt.KeepAspectRatio)
        self.posterLabel.setPixmap(self.pixmap)
        self.posterLabel.setScaledContents(False)
        return

    def updateAwards(self, awardsDict=None):
        """
        Display the awards in the GUI
        """
        self.awardsDisplay.setText("")  # always reset the display box for every new movie

        award = True  # flag the first item in dict bc it's the name of the award, not category/winner
        if awardsDict is not None:
            for category, winners in awardsDict.items():
                if award is True:
                    str = "{} {}".format(category, winners)
                    self.awardsDisplay.append(str)
                    award = False
                else:
                    str = "Category: {} Winner(s): {}".format(category, winners)
                    # print(str)
                    self.awardsDisplay.append(str)
        return

    def updatePlot(self, x=None, revenue=None, budget=None, year=None):

        self.mpl.addBars(x, revenue, budget, year)

        return
