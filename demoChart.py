########################################################################
## CONVERT .UI & .QRC
# pyrcc5 resources.qrc -o resource_rc.py
# pyuic5 -x ui_interface.ui -o ui_interface.py 
########################################################################

########################################################################
## IMPORTS
########################################################################
import os
import sys
import re

from DataManipulate import data_manipulate
from Widgets.DateItem import DateWidgetItem
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
########################################################################
# IMPORT GUI FILE
from ui_interfaceDemo import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
########################################################################

########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.dt = data_manipulate()
        self.ui = Ui_App(self.dt)
        self.ui.setupUi(self)
        self.path = "Path"
        self.dataCombo = []

        #######################################################################
        # ADD FUNCTION ELEMENT
        #######################################################################
        self.ui.menuImport.triggered.connect(self.open_file)
        self.ui.menuExit.triggered.connect(qApp.quit)

        #######################################################################
        # SHOW WINDOW
        #######################################################################
        self.show()
        #######################################################################

    ########################################################################
    ## FUNCTION
    ########################################################################
    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(None, "open File", "", "CSV file (*.csv)")
        if filename:
            self.path = filename
            self.dt.load_data(filename)

            self.dataCombo.append(filename)
            self.ui.dataCombo.clear()
            self.ui.dataCombo.addItems(self.dataCombo)

            self.make_table()
            self.dimension()
            self.Graph()

    def make_table(self):
        self.header = self.dt.get_column()
        self.data = self.dt.get_data()
        self.ui.tableDetail.setColumnCount(len(self.header))
        self.ui.tableDetail.setRowCount(len(self.data))
        self.ui.tableDetail.setHorizontalHeaderLabels(self.header)
        print([type(i) for i in self.data[0]])
        for row in range(len(self.data)):
            for col, item in enumerate(self.data[row]):
                if type(item) in (int, float):
                    newItem = QTableWidgetItem()
                    newItem.setData(QtCore.Qt.DisplayRole, item)
                elif re.match('^(0[1-9]|[12][0-9]|3[01]|[1-9])/(0[1-9]|1[0-2]|[1-9])/\d{4}$', item):
                    newItem = DateWidgetItem(str(item))
                else:
                    newItem = QTableWidgetItem(str(item))
                self.ui.tableDetail.setItem(row, col, newItem)

    def dimension(self):
        self.dt.separated_dimension_measure()
        dimension = self.dt.get_dimension()
        measure = self.dt.get_measure()
        for i in dimension:
            # item = QListWidgetItem("Aa {}".format(i))
            item = QListWidgetItem("{}".format(i))
            self.ui.DimensionWidget.addItem(item)
        for i in measure:
            item = QListWidgetItem("{}".format(i))
            # item = QListWidgetItem("# {}".format(i))
            self.ui.MeasureWidget.addItem(item)

    def Graph(self):
        # create list for y-axis
        y1 = [5, 5, 7, 10, 3, 8, 9, 1, 6, 2]
        # create horizontal list i.e x-axis
        x = ["bleo", 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # create pyqt5graph bar graph item
        # with width = 0.6
        # with bar colors = green
        bargraph = pg.BarGraphItem(x = x, height = y1, width = 0.6, brush ='g')
 
        # add item to plot window
        # adding bargraph item to the plot window
        self.ui.BarChartWidget.addItem(bargraph)
    
        
    ########################################################################

########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ########################################################################
    ##
    ########################################################################
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################
