########################################################################
## CONVERT .UI & .QRC
# pyrcc5 resources.qrc -o resource_rc.py
# pyuic5 -x ui_interface.ui -o ui_interface.py 
########################################################################

########################################################################
## IMPORTS
########################################################################
import sys
from DataManipulate import data_manipulate
from Widgets.DateItem import DateWidgetItem
import re
########################################################################
# IMPORT GUI FILE
from ui_interface import *
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QApplication, QMainWindow, qApp, QListWidgetItem
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt
########################################################################

########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_App()
        self.ui.setupUi(self)
        self.dt = data_manipulate()
        self.path = "Path"
        dataCombo = [
            self.tr('First Item'),
            self.tr('Second Item'),
            self.tr('Third Item'),
        ]
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
                self.make_table()
                self.dimensions()
                #self.ui.dataCombo.setText(filename)

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

    def dimensions(self):
        for colname, coltype in self.dt.data.dtypes.iteritems():
            if coltype == 'object': 
                item = QListWidgetItem("Aa {}".format(colname))
                self.ui.objectList.addItem(item)
            else : 
                item = QListWidgetItem("# {}".format(colname))
                self.ui.valueList.addItem(item)
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
