#! /usr/bin/env python3

import configparser
import logging
import sys
import PyQt5
import ORM
import UI

"""
Author: Winnie Wei Jeng
Assignment: Lab 10
Professor: Phil Tracton
Date: 12/05/2018

The lab demonstrates the use of Matplotlib, Numpy, and Pandas Libraries,
as well as the integration of Matplotlib and Qt
"""

if __name__ == "__main__":
    # Read in our configuration to find out log file name
    config_file = "movies.cfg"
    try:
        configuration = configparser.ConfigParser()
        configuration.read(config_file)
    except OSError:
        print("%s exists but we can not open or read it!" %
              (config_file))
        sys.exit(-1)

    # Parse log file for log file name and set up logging
    if configuration.has_section('LOGGING'):
        log_file_name = configuration['LOGGING']['LOG_FILE']
    else:
        log_file_name = "default.log"
    try:
        logging.basicConfig(filename=log_file_name,
                            level=logging.DEBUG,
                           format='%(asctime)s,%(levelname)s,%(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
    except:
        print("Failed to open log file %s" % (log_file_name))
        sys.exit(-1)

    logging.info("Program Starting")

    # These are the file unzipped from https://www.kaggle.com/tmdb/tmdb-movie-metadata/data
    moviesCSVFile = "../tmdb-5000-movie-dataset/tmdb_5000_movies.csv"
    creditsCSVFile = "../tmdb-5000-movie-dataset/tmdb_5000_credits.csv"

    # If the tables do not exist, create them
    if not ORM.tableExists(ORM.inspector, "Movies"):
        ORM.csvToTable(moviesCSVFile, tableName="Movies", db=ORM.db)

    if not ORM.tableExists(ORM.inspector, "Credits"):
        ORM.csvToTable(creditsCSVFile, tableName="Credits", db=ORM.db)

    # These are the file unzipped from https://www.kaggle.com/tmdb/tmdb-movie-metadata/data

    app = PyQt5.QtWidgets.QApplication(sys.argv)
    gui = UI.UI()
    gui.show()
    app.exec_()

    # All done, log it and exit
    logging.info("Program Terminated")
    sys.exit(0)
