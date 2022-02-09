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

########################################################################
## PLOTLIST CLASS
########################################################################
class PlotList(QtWidgets.QListWidget):
    def __init__(self, main, parent):
        super().__init__(parent)
        self.item_plot = []
        self.main = main
        self.dt = main.dt
        self.dimension = {}
        self.measure = {}
        self.setDefaultDropAction(QtCore.Qt.TargetMoveAction)
        self.itemDoubleClicked.connect(self.launchPopup)
  
    ########################################################################
    ## FUNCTION
    ########################################################################
    def getFilter(self):
        result = {}
        for col in self.dimension:
            result[col] = []
            for fil in self.dimension[col]:
                if self.dimension[col][fil]:
                    result[col].append(fil)
        return result


    def dragLeaveEvent(self, e: QtGui.QDragLeaveEvent) -> None:
        if self.item(self.currentRow())== None:
            return
        # if self.item(self.currentRow()) != name:
        #     return
        if self.count():
            item = self.item(self.currentRow()).text()
            self.clearSelection()
            self.item_plot.remove(item)
            if self.dt.is_dimension(item) and item in self.dimension.keys():
                del self.dimension[self.item(self.currentRow()).text()]
            elif self.dt.is_measure(item) and item in self.measure.keys():
                del self.measure[self.item(self.currentRow()).text()]
            self.takeItem(self.currentRow())
            self.removeItemWidget(self.currentItem())
            super().dragLeaveEvent(e)
            self.main.app.Graph()
    
    def launchPopup(self, item):
        if self.dt.is_dimension(item.text()):
            pop = Popup(item.text(), self)
            pop.show()
        else:
            pop2 = Popup2(item.text(), self)
            pop2.show()
        self.clearSelection()

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
    
    def get_plot_item(self):
        item_plot = []
        for i in range(self.count()):
            # if self.item(i).text != a:
            item_plot.append(self.item(i).text())
        fil = self.getFilter()
        return item_plot, fil, self.measure

    def addFilter(self, name:str) -> None:
        if(self.dt.is_dimension(name)):
            if name not in self.dimension.keys():
                self.dimension[name] = {}
                fil = self.dt.get_unique(name)
                for i in fil:
                    self.dimension[name][i] = True
        else:
            if name not in self.measure.keys():
                self.measure[name] = 'sum'
                
    def dropEvent(self, event: QtGui.QDropEvent) -> None:
        item = self.readData(event.mimeData())[0]
        self.addFilter(item)
        self.item_plot.append(item)
        super().dropEvent(event)
        c = 0
        for i in range(self.count()):
            if self.item(i).text() == item:
                c+= 1
        if c>1:
            for i in range(self.count()-1, -1, -1):
                if self.item(i).text() == item:
                    self.takeItem(i)
                    break
        self.main.app.Graph()

    def test(self):
        item1, col1, measure = self.main.MeasureList_2.get_plot_item()
        item2, col2, _ = self.main.DimensionList_2.get_plot_item()
        # if(len(item1)>0 and len(item2)>0):
            # test = self.dt.data_filter(item1, item2, col1, col2)
            # print(test)


########################################################################
## POPUP MEASURE WINDOW CLASS
########################################################################
class Popup2(QtWidgets.QDialog):
    def __init__(self, name, parent):
        super().__init__(parent)
        self.resize(300, 100)
        self.name = name
        self.parent = parent

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

        self.cancelButton = QtWidgets.QPushButton(self)
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayout.addWidget(self.cancelButton, 2, 2, 1, 2)
        # self.cancelButton.clicked.connect(self.clearFilter)
        self.cancelButton.setText("Cancel")

        self.doneButton = QtWidgets.QPushButton(self)
        self.doneButton.setObjectName("doneButton")
        self.gridLayout.addWidget(self.doneButton, 2, 0, 1, 2)
        # self.doneButton.clicked.connect(self.clearFilter)
        self.doneButton.setText("Done")
    
    ########################################################################
    ## FUNCTION
    ########################################################################    
    def selectionchange(self,i):
      self.parent.measure[self.name] = self.comboBox.currentText()

    def closeEvent(self, event):
        if(isinstance(self.parent, PlotList)):
            self.parent.main.app.Graph()
        else:
            self.parent.main.tableDetail.make_table()


########################################################################
## POPUP DIMENSION WINDOW CLASS
########################################################################
class Popup(QtWidgets.QDialog):
    def __init__(self, name, parent):
        super().__init__(parent)
        self.resize(442, 370)
        self.name = name
        self.parent = parent

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

    ########################################################################
    ## FUNCTION
    ########################################################################
    def closeEvent(self, event):
        if(isinstance(self.parent, PlotList)):
            self.parent.main.app.Graph()
        else:
            self.parent.main.tableDetail.make_table()

    def testCheck(self, item):
        fil = item.text()
        self.parent.dimension[self.name][fil] = not self.parent.dimension[self.name][fil]
        
    def search(self, e): 
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
    
    def selectFilter(self):
        data = self.parent.dimension[self.name]
        for fil in data:
            self.parent.dimension[self.name][fil] = True
        self.createFilter()

    def clearFilter(self):
        data = self.parent.dimension[self.name]
        for fil in data:
            self.parent.dimension[self.name][fil] = False
        self.createFilter()
    
    def createFilter(self):
        for i in range(self.listWidget.count()):
            self.listWidget.takeItem(0)
            # self.listWidget.

        data = self.parent.dimension[self.name]
        for i in data:
            item = QtWidgets.QListWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
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
        pop = Popup(item.text(), self)
        pop.show()

    def dragLeaveEvent(self, e: QtGui.QDragLeaveEvent) -> None:
        if self.count():
            del self.dimension[self.item(self.currentRow()).text()]
            self.takeItem(self.currentRow())
            self.main.tableDetail.make_table()

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
    
    def dragEnterEvent(self, e: QtGui.QDragEnterEvent) -> None:
        col = self.readData(e.mimeData())[0]
        if self.dt.is_dimension(col):
            e.accept()
        else:
            e.ignore()
    
    def getFilter(self):
        result = {}
        for col in self.dimension:
            result[col] = []
            for fil in self.dimension[col]:
                if self.dimension[col][fil]:
                    result[col].append(fil)
        return result
    
    def addFilter(self, name:str) -> None:
        if name not in self.dimension.keys():
            self.dimension[name] = {}
            fil = self.dt.get_unique(name)
            for i in fil:
                self.dimension[name][i] = True

    def dropEvent(self, event: QtGui.QDropEvent) -> None:
        col = self.readData(event.mimeData())[0]
        self.addFilter(col)
        super().dropEvent(event)
        self.main.tableDetail.make_table()

class MeasureList(QtWidgets.QListWidget):
    def __init__(self, main, parent):
        super(MeasureList, self).__init__(parent)
        self.dt = main.dt
        self.main = main
        self.measure = {}
        self.itemDoubleClicked.connect(self.launchFilter)
    
    def launchFilter(self, item):
        pop = Popup2(item.text(), self)
        pop.show()

    def dragLeaveEvent(self, e: QtGui.QDragLeaveEvent) -> None:
        if self.count():
            del self.measure[self.item(self.currentRow()).text()]
            self.takeItem(self.currentRow())
            self.main.tableDetail.make_table()
            self.main.tableDetail.make_table()

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
        # val = col.split('.')[0]
        if self.dt.is_measure(col):
            e.accept()
        else:
            e.ignore()
    
    def addFilter(self, item):
        if item not in self.measure.keys():
            self.measure[item] = 'sum'

    
    def dropEvent(self, event: QtGui.QDropEvent) -> None:
        # super().dropEvent(event)
        col = self.readData(event.mimeData())[0]
        if self.isExist(col):
            return
        self.addFilter(col)
        item = QListWidgetItem()
        item.setText(col)
        self.addItem(item)
        self.main.tableDetail.make_table()

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
        self.setColumnCount(0)
        self.setRowCount(0)
        self.dimension = self.get_widget_item(self.main.DimensionList)
        self.dimension_filter = self.main.DimensionList.getFilter()
        self.measure_raw = self.get_widget_item(self.main.MeasureList)
        self.measure = self.main.MeasureList.measure
        # print(self.dimension_filter)
        if not(len(self.dimension) > 0 ):
            self.main.MeasureList.clear()
            return
        self.data_groupby = self.dt.get_groupby(self.dimension, self.measure, self.dimension_filter)
        self.header = self.data_groupby['col']
        self.data = self.data_groupby['data']
        self.setColumnCount(len(self.header))
        self.setRowCount(len(self.data))
        self.setHorizontalHeaderLabels(self.header)
        for row in range(len(self.data)):
            for col, item in enumerate(self.data[row]):
                if type(item) in (int, float):
                    newItem = QTableWidgetItem()
                    newItem.setData(QtCore.Qt.DisplayRole, item)
                else:
                    newItem = QTableWidgetItem(str(item))
                self.setItem(row, col, newItem)
    
    def get_widget_item(self, widget:QtWidgets.QListWidget) -> list :
        return [widget.item(i).text() for i in range(widget.count())]
    
    def to_measure_dict(self, measure: list):
        result = {}
        for i in measure:
            col = i.split('.')
            result[col[0]] = col[1]
        return result

    def add_listbox(self, e):
        col = self.readData(e.mimeData())[0]
        if self.dt.is_measure(col) and len(self.dimension) > 0:
            # self.measure[col] = 'sum'
            # col = col+'.sum'
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
        self.add_listbox(event)
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