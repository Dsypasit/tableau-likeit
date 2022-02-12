# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\test_table.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from asyncore import read
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDataStream, Qt
from PyQt5.QtWidgets import QListWidgetItem, QTableWidgetItem 
from matplotlib.pyplot import text
from Widgets.DataManipulate import data_manipulate
import copy as cp
import pandas
import re
from Widgets.DateItem import DateWidgetItem

########################################################################
## PLOTLIST CLASS
########################################################################
class PlotList(QtWidgets.QListWidget):
    def __init__(self, main, parent):
        super().__init__(parent)
        self.item_plot : list = []
        self.main : QtWidgets.QMainWindow = main
        self.dt : pandas.core.frame.DataFrame = main.dt
        self.dimension : dict = {}
        self.measure : dict = {}
        self.measure_filter : dict = {}
        self.setDefaultDropAction(QtCore.Qt.TargetMoveAction)
        self.itemDoubleClicked.connect(self.launchPopup)
        self.itemClicked.connect(self.allow_drag)
        self.allow = False
    
    ########################################################################
    ## FUNCTION
    ########################################################################
    def allow_drag(self) -> None:
        """ This method will allow drag"""
        self.allow = True

    def getFilter(self) -> dict:
        """ This method will return filter dimension dict """
        result = {}
        for col in self.dimension:  # column in list box
            if self.dt.check_date_col(col):
                result[col] = {}
                for method in ['day', 'month', 'year']:
                    result[col][method] = []
                    for fil in self.dimension[col][method]:
                        if self.dimension[col][method][fil]:
                            result[col][method].append(fil)
                result[col]['graph'] = self.dimension[col]['graph']
            else:
                result[col] = []
                for fil in self.dimension[col]:
                    if self.dimension[col][fil]: # selected item
                        result[col].append(fil)
        result = {**result, **self.measure_filter}
        return result

    def dragEnterEvent(self, e: QtGui.QDragEnterEvent) -> None:     # when mouse drag in this area
        item = self.readData(e.mimeData())[0]
        if item in self.dimension.keys() or item in self.measure.keys():
            self.allow = True
        else:
            self.allow = False
        return super().dragEnterEvent(e)

    def dragLeaveEvent(self, e: QtGui.QDragLeaveEvent) -> None:
        if self.item(self.currentRow())== None:
            return
        d = self.currentRow()
        if self.count() and self.allow:
            item = self.item(self.currentRow()).text()
            self.item_plot.remove(item)
            if self.dt.is_dimension(item) and item in self.dimension.keys():
                del self.dimension[self.item(self.currentRow()).text()]
            elif self.dt.is_measure(item) and item in self.measure.keys():
                del self.measure[self.item(self.currentRow()).text()]
                del self.measure_filter[self.item(self.currentRow()).text()]
            self.takeItem(d)
            self.clearSelection()
            super().dragLeaveEvent(e)
            self.main.app.Graph()
            self.allow = False
    
    def launchPopup(self, item: QtWidgets.QWidgetItem):
        if self.dt.is_dimension(item.text()): # if item is dimension
            if self.dt.check_date_col(item.text()):
                pop = Popup3(item.text(), self)
                pop.show()
            else:
                pop = Popup(item.text(), self)
                pop.show()

        else:
            pop2 = Popup2(item.text(), self)
            pop2.show()
        self.clearSelection()

    def readData(self, mime: QtCore.QMimeData) -> list:     # read event item
        stream = QDataStream(mime.data('application/x-qabstractitemmodeldatalist'))
        textList = []
        while not stream.atEnd():
            # we're not using row and columns, but we *must* read them
            row = stream.readInt()
            col = stream.readInt()
            for dataSize in range(stream.readInt()):
                role, value = stream.readInt(), stream.readQVariant()
                if role == Qt.DisplayRole:
                    textList.append(value)
        return textList
    
    def get_plot_item(self) -> tuple:
        """ This method will return important item to plot graph"""
        item_plot = []
        for i in range(self.count()):
            item_plot.append(self.item(i).text())   
        fil = self.getFilter()
        return item_plot, fil, self.measure

    def addFilter(self, name:str) -> None:
        """ This method will add filter to dict"""
        if(self.dt.is_dimension(name)):
            if name not in self.dimension.keys():
                if self.dt.check_date_col(name):
                    self.dimension[name] = {}
                    for method in ['day', 'month', 'year']:
                        self.dimension[name][method] = {}
                        fil = self.dt.get_unique_date(name, method)
                        for i in fil:
                            self.dimension[name][method][i] = True
                    self.dimension[name]['graph'] = 'year'
                else:
                    self.dimension[name] = {}
                    fil = self.dt.get_unique(name)
                    for i in fil:
                        self.dimension[name][i] = True
        else:
            if name not in self.measure.keys():
                self.measure[name] = 'sum'  # set sum as default
                self.measure_filter[name] = dict()
                self.measure_filter[name]['condition'] = '=='      # set sum method by default
                self.measure_filter[name]['value'] = 0      # set sum method by default
                self.measure_filter[name]['state'] = False      # set sum method by default
                
    def dropEvent(self, event: QtGui.QDropEvent) -> None:
        item = self.readData(event.mimeData())[0]
        self.addFilter(item)
        self.item_plot.append(item)
        super().dropEvent(event)
        self.clearSelection()
        self.main.app.Graph()
        self.allow = False



########################################################################
## POPUP MEASURE WINDOW CLASS
########################################################################
class Popup3(QtWidgets.QDialog):
    def __init__(self, name, parent):
        super().__init__(parent)
        self.name = name
        self.parent = parent
        self.dimension = cp.deepcopy(self.parent.dimension)
        self.method : str = self.dimension[self.name]['graph']
        self.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.setWindowTitle("Filter "+name)
        self.selectButton = QtWidgets.QPushButton(self)
        self.selectButton.setGeometry(20, 20, 75, 23)
        self.selectButton.setText('Select')
        self.selectButton.clicked.connect(self.selectFilter)
        self.clearButton = QtWidgets.QPushButton(self)
        self.clearButton.setGeometry(280, 20, 75, 23)
        self.clearButton.setText('Clear')
        self.clearButton.clicked.connect(self.clearFilter)

        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(160, 20, 70, 23)
        self.comboBox.addItem("Year")
        self.comboBox.addItem("Month")
        self.comboBox.addItem("Day")
        self.comboBox.setCurrentText(self.method.capitalize())
        self.comboBox.currentIndexChanged.connect(self.changeMethod)

        self.listWidget = QtWidgets.QListWidget(self)
        self.listWidget.setGeometry(70, 50, 256, 192)
        self.listWidget.itemChanged.connect(self.testCheck)

        self.doneButton = QtWidgets.QPushButton(self)
        self.doneButton.setGeometry(80, 250, 75, 23)
        self.doneButton.setText('Done')
        self.doneButton.clicked.connect(self.changeFilter)
        self.cancelButton = QtWidgets.QPushButton(self)
        self.cancelButton.setGeometry(250, 250, 75, 23)
        self.cancelButton.setText('Cancel')
        self.cancelButton.clicked.connect(self.close)

        self.createFilter()
    
    def changeMethod(self, index):
        self.method = self.comboBox.currentText().lower()
        self.dimension[self.name]['graph'] = self.method
        self.createFilter()

    def changeFilter(self, event):
        self.parent.dimension = self.dimension
        if(isinstance(self.parent, PlotList)):
            self.parent.main.app.Graph()
        else:
            self.parent.main.tableWidget.make_table()
        self.close()

    def testCheck(self, item):
        fil = int(item.text())
        self.dimension[self.name][self.method][fil] = not self.dimension[self.name][self.method][fil]     # change item filter of column dimension
    
    def selectFilter(self): # select all item
        # print('hello')
        data = self.dimension[self.name]
        for fil in data[self.method]:
            self.dimension[self.name][self.method][fil] = True
        self.createFilter()

    def clearFilter(self):  # deselect all item
        data = self.dimension[self.name]
        for fil in data[self.method]:
            self.dimension[self.name][self.method][fil] = False
        self.createFilter()
    
    def createFilter(self):
        for i in range(self.listWidget.count()):    # clear all item
            self.listWidget.takeItem(0)

        data = self.dimension[self.name]
        for i in data[self.method]:
            item = QtWidgets.QListWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled) # can check/uncheck
            if data[self.method][i]:
                item.setCheckState(QtCore.Qt.Checked)
            else:
                item.setCheckState(QtCore.Qt.Unchecked)
            item.setData(QtCore.Qt.DisplayRole, i)
            self.listWidget.addItem(item)


class Popup2(QtWidgets.QDialog):    # popup for measure
    def __init__(self, name, parent):
        super().__init__(parent)
        self.resize(300, 100)
        self.name = name
        self.parent = parent
        self.measure = cp.deepcopy(self.parent.measure)
        self.measure_filter = cp.deepcopy(self.parent.measure_filter)

        self.setWindowTitle("Filter "+name)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")

        self.label = QtWidgets.QLabel(self)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)
        self.label.setText(name)

        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.addItem("sum")
        self.comboBox.addItem("mean")
        self.comboBox.addItem("median")
        self.comboBox.addItem("min")
        self.comboBox.addItem("max")
        self.comboBox.addItem("count")
        self.comboBox.setCurrentText(self.parent.measure[name])
        self.comboBox.currentIndexChanged.connect(self.selectionchange)
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 4)

        self.state = QtWidgets.QCheckBox(self)
        self.state.setText("Filter")
        self.state.setChecked(self.measure_filter[self.name]['state'])
        self.state.stateChanged.connect(self.stateChange)
        self.gridLayout.addWidget(self.state, 2, 0)

        self.filterBox = QtWidgets.QComboBox(self)
        self.filterBox.addItem("==")
        self.filterBox.addItem("!=")
        self.filterBox.addItem(">")
        self.filterBox.addItem(">=")
        self.filterBox.addItem("<")
        self.filterBox.addItem("<=")
        self.filterBox.setCurrentText(self.measure_filter[self.name]['condition'])
        self.filterBox.currentIndexChanged.connect(self.selectionchange)
        self.gridLayout.addWidget(self.filterBox, 3, 1, 1, 2)

        self.labelData = QtWidgets.QLabel(self)
        self.labelData.setText("data")
        self.gridLayout.addWidget(self.labelData, 3,0)

        self.valueEdit = QtWidgets.QLineEdit(self)
        self.valueEdit.setObjectName("cancelButton")
        self.gridLayout.addWidget(self.valueEdit, 3, 3)
        self.valueEdit.setText(str(self.measure_filter[self.name]['value']))
        self.valueEdit.textEdited.connect(self.valueChange)
        # self.cancelButton.clicked.connect(self.clearFilter)

        self.cancelButton = QtWidgets.QPushButton(self)
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayout.addWidget(self.cancelButton, 4, 2, 1, 2)
        # self.cancelButton.clicked.connect(self.clearFilter)
        self.cancelButton.setText("Cancel")

        self.doneButton = QtWidgets.QPushButton(self)
        self.doneButton.setObjectName("doneButton")
        self.gridLayout.addWidget(self.doneButton, 4, 0, 1, 2)
        # self.doneButton.clicked.connect(self.clearFilter)
        self.doneButton.setText("Done")

        self.doneButton.clicked.connect(self.changeFilter)
        self.cancelButton.clicked.connect(self.close)
    
    ########################################################################
    ## FUNCTION
    ########################################################################    
    def stateChange(self, e):
        if e:
            self.measure_filter[self.name]['state'] = True
        else:
            self.measure_filter[self.name]['state'] = False
    
    def is_float(self, element: str) -> bool:
        try:
            float(element)
            return True
        except ValueError:
            return False

    def valueChange(self, e:str):
        if self.is_float(e):
            self.measure_filter[self.name]['value'] = float(e)
    
    def changeFilter(self, e):
        self.parent.measure = self.measure
        self.parent.measure_filter = self.measure_filter
        self.close()
    
    def selectionchange(self,i):
      self.measure[self.name] = self.comboBox.currentText()     # change method of measure column
      self.measure_filter[self.name]['condition'] = self.filterBox.currentText()     # change method of measure column

    def closeEvent(self, event):
        if(isinstance(self.parent, PlotList)):  # check parent class
            self.parent.main.app.Graph()
        else:
            self.parent.main.tableWidget.make_table()


########################################################################
## POPUP DIMENSION WINDOW CLASS
########################################################################
class Popup(QtWidgets.QDialog):     # popup for dimension
    def __init__(self, name, parent):
        super().__init__(parent)
        self.resize(442, 370)
        self.name = name
        self.parent = parent
        self.dimension = cp.deepcopy(self.parent.dimension)

        self.setWindowTitle("Filter "+name)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget = QtWidgets.QListWidget(self)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 2, 0, 1, 4)
        # function listwidget
        self.listWidget.itemChanged.connect(self.testCheck)
        self.listWidget.setSortingEnabled(True)

        self.label = QtWidgets.QLabel(self)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)
        self.label.setText(name)

        self.selectButton = QtWidgets.QPushButton(self)
        self.selectButton.setObjectName("selectButton")
        self.gridLayout.addWidget(self.selectButton, 1, 0, 1, 1)
        self.selectButton.clicked.connect(self.selectFilter)
        self.selectButton.setText("All Select")

        self.clearButton = QtWidgets.QPushButton(self)
        self.clearButton.setObjectName("clearButton")
        self.gridLayout.addWidget(self.clearButton, 1, 3, 1, 1)
        self.clearButton.clicked.connect(self.clearFilter)
        self.clearButton.setText("All Clear")

        self.searchEdit = QtWidgets.QLineEdit(self)
        self.searchEdit.setObjectName("searchEdit")
        self.gridLayout.addWidget(self.searchEdit, 1, 1, 1, 2)
        self.searchEdit.textEdited.connect(self.search)

        self.cancelButton = QtWidgets.QPushButton(self)
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayout.addWidget(self.cancelButton, 3, 2, 1, 2)
        # self.cancelButton.clicked.connect(self.clearFilter)
        self.cancelButton.setText("Cancel")

        self.doneButton = QtWidgets.QPushButton(self)
        self.doneButton.setObjectName("doneButton")
        self.gridLayout.addWidget(self.doneButton, 3, 0, 1, 2)
        # self.doneButton.clicked.connect(self.clearFilter)
        self.doneButton.setText("Done")

        self.createFilter()
        self.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))

        # self.cancelButton.clicked.connect(self.resetDimension)
        self.cancelButton.clicked.connect(self.close)
        self.doneButton.clicked.connect(self.changeFilter)

    ########################################################################
    ## FUNCTION
    ########################################################################
    def changeFilter(self, event):
        self.parent.dimension = self.dimension
        if(isinstance(self.parent, PlotList)):
            self.parent.main.app.Graph()
        else:
            self.parent.main.tableWidget.make_table()
        self.close()

    def testCheck(self, item):
        fil = item.text()
        self.dimension[self.name][fil] = not self.dimension[self.name][fil]     # change item filter of column dimension
        
    def search(self, e):
        """ This method will search item in listbox """
        if e == "":
            self.createFilter()
            return 
        for i in range(self.listWidget.count()):
            self.listWidget.takeItem(0)
        data = self.parent.dimension[self.name]
        for fil in data:
            if e in fil:
                item = QtWidgets.QListWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                if data[fil]:
                    item.setCheckState(QtCore.Qt.Checked)
                else:
                    item.setCheckState(QtCore.Qt.Unchecked)
                item.setData(QtCore.Qt.DisplayRole, fil)
                self.listWidget.addItem(item)
    
    def selectFilter(self): # select all item
        data = self.dimension[self.name]
        for fil in data:
            self.dimension[self.name][fil] = True
        self.createFilter()

    def clearFilter(self):  # deselect all item
        data = self.dimension[self.name]
        for fil in data:
            self.dimension[self.name][fil] = False
        self.createFilter()
    
    def createFilter(self):
        for i in range(self.listWidget.count()):    # clear all item
            self.listWidget.takeItem(0)

        data = self.dimension[self.name]
        for i in data:
            item = QtWidgets.QListWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled) # can check/uncheck
            if data[i]:
                item.setCheckState(QtCore.Qt.Checked)
            else:
                item.setCheckState(QtCore.Qt.Unchecked)
            item.setData(QtCore.Qt.DisplayRole, i)
            self.listWidget.addItem(item)


class DimensionList(QtWidgets.QListWidget):
    def __init__(self, main, parent):
        super(DimensionList, self).__init__(parent)
        self.dt = main.dt
        self.main = main
        self.dimension = {}

        self.itemDoubleClicked.connect(self.launchFilter)
    
    def launchFilter(self, item):
        if self.dt.check_date_col(item.text()):
            pop = Popup3(item.text(), self)
            pop.show()
        else:
            pop = Popup(item.text(), self)
            pop.show()

    def dragLeaveEvent(self, e: QtGui.QDragLeaveEvent) -> None:     # action when drag item out of area
        if self.count():
            del self.dimension[self.item(self.currentRow()).text()]
            self.takeItem(self.currentRow())
            self.main.tableWidget.make_table()

    def readData(self, mime: QtCore.QMimeData) -> list:     # read event item
        stream = QDataStream(mime.data('application/x-qabstractitemmodeldatalist'))
        textList = []
        while not stream.atEnd():
            # we're not using row and columns, but we *must* read them
            row = stream.readInt()
            col = stream.readInt()
            for dataSize in range(stream.readInt()):
                role, value = stream.readInt(), stream.readQVariant()
                if role == Qt.DisplayRole:
                    textList.append(value)
        return textList
    
    def dragEnterEvent(self, e: QtGui.QDragEnterEvent) -> None:
        col = self.readData(e.mimeData())[0]
        if self.dt.is_dimension(col):
            e.accept()
        else:
            e.ignore()
    
    def getFilter(self) -> dict:
        """ This method will return filter dimension dict """
        result = {}
        for col in self.dimension:  # column in list box
            if self.dt.check_date_col(col):
                result[col] = {}
                for method in ['day', 'month', 'year']:
                    result[col][method] = []
                    for fil in self.dimension[col][method]:
                        if self.dimension[col][method][fil]:
                            result[col][method].append(fil)
                result[col]['graph'] = self.dimension[col]['graph']
            else:
                result[col] = []
                for fil in self.dimension[col]:
                    if self.dimension[col][fil]: # selected item
                        result[col].append(fil)
        return result
    
    def addFilter(self, name:str) -> None:
        """ This method will create new dimension col and add unique item """
        if name not in self.dimension.keys():
            if self.dt.check_date_col(name):
                self.dimension[name] = {}
                for method in ['day', 'month', 'year']:
                    self.dimension[name][method] = {}
                    fil = self.dt.get_unique_date(name, method)
                    for i in fil:
                        self.dimension[name][method][i] = True
                self.dimension[name]['graph'] = 'year'
            else:
                self.dimension[name] = {}
                fil = self.dt.get_unique(name)
                for i in fil:
                    self.dimension[name][i] = True

    def dropEvent(self, event: QtGui.QDropEvent) -> None:
        col = self.readData(event.mimeData())[0]
        self.addFilter(col)
        super().dropEvent(event)
        self.main.tableWidget.make_table()

class MeasureList(QtWidgets.QListWidget):
    def __init__(self, main, parent):
        super(MeasureList, self).__init__(parent)
        self.dt = main.dt
        self.main = main
        self.measure = {}
        self.measure_filter = {}
        self.itemDoubleClicked.connect(self.launchFilter)
        self.allow = False
    
    def allow_drag(self):
        self.allow = True
    
    def launchFilter(self, item):
        pop = Popup2(item.text(), self)
        pop.show()

    def dragLeaveEvent(self, e: QtGui.QDragLeaveEvent) -> None:
        if self.count():
            del self.measure[self.item(self.currentRow()).text()]
            del self.measure_filter[self.item(self.currentRow()).text()]
            self.takeItem(self.currentRow())
            self.main.tableWidget.make_table()

    def readData(self, mime: QtCore.QMimeData) -> list:
        stream = QDataStream(mime.data('application/x-qabstractitemmodeldatalist'))
        textList = []
        while not stream.atEnd():
            # we're not using row and columns, but we *must* read them
            row = stream.readInt()
            col = stream.readInt()
            for dataSize in range(stream.readInt()):
                role, value = stream.readInt(), stream.readQVariant()
                if role == Qt.DisplayRole:
                    textList.append(value)
        return textList
    
    def isExist(self, s):
        for i in range(self.count()):
            if s.split('.')[0] == self.item(i).text().split('.')[0]:
                return True
        return False
    
    def dragEnterEvent(self, e: QtGui.QDragEnterEvent) -> None:
        col = self.readData(e.mimeData())[0]
        if self.dt.is_measure(col):
            e.accept()
        else:
            e.ignore()
    
    def getFilter(self):
        return self.measure_filter
    
    def addFilter(self, item):
        if item not in self.measure.keys():
            self.measure[item] = 'sum'      # set sum method by default
            self.measure_filter[item] = dict()
            self.measure_filter[item]['condition'] = '=='      # set sum method by default
            self.measure_filter[item]['value'] = 0      # set sum method by default
            self.measure_filter[item]['state'] = False      # set sum method by default

    
    def dropEvent(self, event: QtGui.QDropEvent) -> None:
        col = self.readData(event.mimeData())[0]
        if self.isExist(col):
            return
        self.addFilter(col)
        item = QListWidgetItem()
        item.setText(col)
        self.addItem(item)
        self.main.tableWidget.make_table()

class TableGroupby(QtWidgets.QTableWidget):
    def __init__(self, main, parent):
        super(TableGroupby, self).__init__(parent)
        self.main = main
        self.dt = main.dt
        self.dimension = []
        self.measure = {}
        self.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.setSortingEnabled(True)

    def make_table(self):
        """ This method will make table"""
        self.setColumnCount(0)  # clear column and row count
        self.setRowCount(0) 
        self.dimension = self.get_widget_item(self.main.DimensionList)  # get dimension list
        self.dimension_filter = self.main.DimensionList.getFilter()     # get dimensino filter
        self.measure = self.main.MeasureList.measure
        self.measure_filter = self.main.MeasureList.measure_filter
        if not(len(self.dimension) > 0 ):   # if dimension has no item
            self.main.MeasureList.clear()
            self.main.MeasureList.measure = {}
            return
        fil = {**self.dimension_filter, **self.measure_filter}
        self.data_groupby = self.dt.get_groupby(self.dimension, self.measure, fil)    # use groupby and get dataframe data
        self.header = self.data_groupby['col']
        self.data = self.data_groupby['data']
        self.setColumnCount(len(self.header))
        self.setRowCount(len(self.data))
        self.setHorizontalHeaderLabels(self.header)
        for row in range(len(self.data)):
            for col, item in enumerate(self.data[row]):
                if type(item) in (int, float):  # check type of item when add to table
                    newItem = QTableWidgetItem()
                    newItem.setData(QtCore.Qt.DisplayRole, item)
                elif re.match('^(0[1-9]|[12][0-9]|3[01]|[1-9])/(0[1-9]|1[0-2]|[1-9])/\d{4}$', str(item)): # check date column
                    newItem = DateWidgetItem(str(item))
                else:
                    newItem = QTableWidgetItem(str(item))
                self.setItem(row, col, newItem)     # add item to table
    
    def get_widget_item(self, widget:QtWidgets.QListWidget) -> list :
        return [widget.item(i).text() for i in range(widget.count())]

    def add_listbox(self, e) -> None: # add item to measurelist or dimensin list
        col = self.readData(e.mimeData())[0]
        if self.dt.is_measure(col) and len(self.dimension) > 0:     # if col is measure
            item = QListWidgetItem()
            item.setText(col)
            item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            self.main.MeasureList.addItem(item)
            self.main.MeasureList.addFilter(col)
            e.accept()
        elif self.dt.is_dimension(col):
            self.dimension.append(col)
            self.main.DimensionList.addFilter(col)
            self.main.DimensionList.addItem(col)
            e.accept()
    
    def dropEvent(self, event: QtGui.QDropEvent) -> None:
        self.add_listbox(event)     # add item to measurelist or dimensin list
        if len(self.dimension) >0:
            self.make_table()

    def readData(self, mime: QtCore.QMimeData) -> list:
        stream = QDataStream(mime.data('application/x-qabstractitemmodeldatalist'))
        textList = []
        while not stream.atEnd():
            # we're not using row and columns, but we *must* read them
            row = stream.readInt()
            col = stream.readInt()
            for dataSize in range(stream.readInt()):
                role, value = stream.readInt(), stream.readQVariant()
                if role == Qt.DisplayRole:
                    textList.append(value)
        return textList