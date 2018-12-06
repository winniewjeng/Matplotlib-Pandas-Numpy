"""
This is the top level UI for the Python Movies Project
At this level we instantiate the Central Window which has the
GUI elements.  This is also the level of handling signal/slot connections.
"""
import datetime
import logging
import traceback

import PyQt5
import PyQt5.QtWidgets
import sqlalchemy

import OpenMovie
import UI_CentralWindow


class UI(PyQt5.QtWidgets.QMainWindow):
    """
    Top level UI class
    """

    def __init__(self, parent=None):
        print("Entering UI CTOR")
        super(UI, self).__init__(parent)

        # Create Main Window Elements
        self.statusBar().showMessage('Status Bar')
        self.setWindowTitle('Python Movie Project')

        # Create our central widget
        self.centralWidget = UI_CentralWindow.UI_CentralWindow()
        self.setCentralWidget(self.centralWidget)

        # Connect signals and slots
        self.centralWidget.enterMoviePushButton.clicked.connect(
            self.enterMoviePushButtonClicked)
        # Display
        self.show()
        print("Exiting UI CTOR")

    def enterMoviePushButtonClicked(self):
        """
        Callback function for the enterMoviePushButton button object is clicked
        """
        print("Entering UI enterMoviePushButtonClicked method")
        # Read the movie title from the GUI.  This is UNSAFE data.  Never trust a USER!
        movieTitle = self.centralWidget.enterMovieLineEdit.text()

        # Instantiate an openMovie object from the class
        openMovie = OpenMovie.OpenMovie(title=movieTitle, posterURL=None)

        movieTitleQuery = openMovie.getMovieTitleData()
        if movieTitleQuery is False:
            return

        # Get our data
        cast = openMovie.getCast()
        director, crew = openMovie.getCrew()

        awardDict = openMovie.getAwards()

        # Update UI_CentralWindow with awardDict
        self.statusBar().showMessage("Start Getting Award")
        if awardDict is False or awardDict is None:
            self.centralWidget.awardsDisplay.setText("No Award")
            return
        else:
            self.centralWidget.updateAwards(awardDict)

        # Update UI_CentralWindow with posterFileName
        self.statusBar().showMessage("Start Getting Poster")

        if openMovie.getPoster() is False:
            self.centralWidget.posterLabel.setText("No Poster")
            return
        else:
            self.centralWidget.updatePoster(openMovie.posterFileName)

        self.statusBar().showMessage("Done Getting Poster")

        # Update the GUI
        self.centralWidget.directorInformation.infoLabel.setText(director)
        self.centralWidget.actorInformation.infoLabel.setText(cast[0]['name'])
        self.centralWidget.releaseDateInformation.infoLabel.setText(
            movieTitleQuery.release_date)
        self.centralWidget.budgetInformation.infoLabel.setText(
            "{:,.2f}".format(movieTitleQuery.budget))
        self.centralWidget.revenueInformation.infoLabel.setText(
            "{:,.2f}".format(movieTitleQuery.revenue))
        self.centralWidget.runTimeInformation.infoLabel.setNum(
            movieTitleQuery.runtime)
        self.centralWidget.voteCountInformation.infoLabel.setText(
            "{:,.2f}".format(movieTitleQuery.vote_count))
        self.centralWidget.voteAverageInformation.infoLabel.setText(
            "{:,.2f}".format(movieTitleQuery.vote_average))
        self.centralWidget.statusInformation.infoLabel.setText(
            movieTitleQuery.status)

        # Call openMovie’s analyzeMovie method
        year, month, day = movieTitleQuery.release_date.split('-')
        print("{}  {}  {}".format(year, month, day))
        year = int(year)
        month = int(month)
        openMovie.analyzeMovie(year=year, month=month)

        print("Exiting UI enterMoviePushButtonClicked method")
        return
