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
from Widgets.DataManipulate import data_manipulate
from Widgets.DateItem import DateWidgetItem
########################################################################
# IMPORT GUI FILE
# from ui_interface import *
from ui_interfaceDemo import *
from PyQt5.QtWidgets import QFileDialog, QListWidget, QTableWidgetItem, QApplication, QMainWindow, qApp, QListWidgetItem
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
        self.ui.actionUnion.triggered.connect(self.union_file)

        self.ui.DimensionWidget.itemDoubleClicked.connect(self.to_measure)
        self.ui.MeasureWidget.itemDoubleClicked.connect(self.to_dimension)

        #######################################################################
        # SHOW WINDOW
        #######################################################################
        self.show()
        #######################################################################

    ########################################################################
    ## FUNCTION
    ########################################################################
    def to_dimension(self, item):
        self.dt.change_to_dimension(item.text())
        self.dimension()

    def to_measure(self, item):
        self.dt.change_to_measure(item.text())
        self.dimension()

    def union_file(self):
        filename, _ = QFileDialog.getOpenFileName(None, "open File", "", "CSV file (*.csv)")
        if filename:
            self.path = filename
            self.dt.unioun_data(filename)

            self.dataCombo.append(filename)
            self.ui.dataCombo.clear()
            self.ui.dataCombo.addItems(self.dataCombo)

            self.make_table()
            #self.ui.dataCombo.setText(filename)
            self.dimension()

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(None, "open File", "", "CSV file (*.csv)")
        if filename:
            self.path = filename
            self.dt.load_data(filename)

            self.dataCombo.append(filename)
            self.ui.dataCombo.clear()
            self.ui.dataCombo.addItems(self.dataCombo)

            self.make_table()
            #self.ui.dataCombo.setText(filename)
            self.dt.separated_dimension_measure()
            self.dimension()

    def make_table(self):
        self.header = self.dt.get_column()
        self.data = self.dt.get_data()
        self.ui.tableWidget.setColumnCount(len(self.header))
        self.ui.tableWidget.setRowCount(len(self.data))
        self.ui.tableWidget.setHorizontalHeaderLabels(self.header)
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
                self.ui.tableWidget.setItem(row, col, newItem)

    def dimension(self):
        for i in range(self.ui.DimensionWidget.count()):
            self.ui.DimensionWidget.takeItem(0)
        for i in range(self.ui.MeasureWidget.count()):
            self.ui.MeasureWidget.takeItem(0)
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

    def changeDataCombo(self):
        pass
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