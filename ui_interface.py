# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_App(object):
    def setupUi(self, App):
        App.setObjectName("App")
        App.resize(1080, 800)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/icons8-bookmark-384.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        App.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(App)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableDetail = QtWidgets.QTableWidget(self.tab)
        self.tableDetail.setObjectName("tableDetail")
        self.tableDetail.setColumnCount(3)
        self.tableDetail.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableDetail.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableDetail.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableDetail.setHorizontalHeaderItem(2, item)
        self.gridLayout_2.addWidget(self.tableDetail, 2, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_4.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_4.addWidget(self.lineEdit_2, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.stackedWidget = QtWidgets.QStackedWidget(self.tab_2)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout_9.addWidget(self.stackedWidget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        App.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(App)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuData = QtWidgets.QMenu(self.menubar)
        self.menuData.setObjectName("menuData")
        App.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(App)
        self.statusbar.setObjectName("statusbar")
        App.setStatusBar(self.statusbar)
        self.dataWidget = QtWidgets.QDockWidget(App)
        self.dataWidget.setObjectName("dataWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.dataCombo = QtWidgets.QComboBox(self.dockWidgetContents)
        self.dataCombo.setObjectName("dataCombo")
        self.dataCombo.addItem("")
        self.gridLayout.addWidget(self.dataCombo, 0, 0, 1, 2)
        self.label_10 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)
        self.searchEntry = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.searchEntry.setObjectName("searchEntry")
        self.gridLayout.addWidget(self.searchEntry, 1, 1, 1, 1)
        self.objectList = QtWidgets.QListWidget(self.dockWidgetContents)
        self.objectList.setObjectName("objectList")
        self.gridLayout.addWidget(self.objectList, 2, 0, 1, 2)
        self.line = QtWidgets.QFrame(self.dockWidgetContents)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 0, 1, 2)
        self.valueList = QtWidgets.QListWidget(self.dockWidgetContents)
        self.valueList.setObjectName("valueList")
        self.gridLayout.addWidget(self.valueList, 4, 0, 1, 2)
        self.dataWidget.setWidget(self.dockWidgetContents)
        App.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dataWidget)
        self.menuOpen = QtWidgets.QAction(App)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/icons8-opened-folder-384.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuOpen.setIcon(icon1)
        self.menuOpen.setObjectName("menuOpen")
        self.menuSave = QtWidgets.QAction(App)
        self.menuSave.setObjectName("menuSave")
        self.menuExit = QtWidgets.QAction(App)
        self.menuExit.setObjectName("menuExit")
        self.menuImport = QtWidgets.QAction(App)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/images/icons8-document-384.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuImport.setIcon(icon2)
        self.menuImport.setObjectName("menuImport")
        self.menuFile.addAction(self.menuOpen)
        self.menuFile.addAction(self.menuSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuExit)
        self.menuData.addAction(self.menuImport)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuData.menuAction())

        self.retranslateUi(App)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(App)

    def retranslateUi(self, App):
        _translate = QtCore.QCoreApplication.translate
        App.setWindowTitle(_translate("App", "Tableauu"))
        item = self.tableDetail.horizontalHeaderItem(0)
        item.setText(_translate("App", "New Column"))
        item = self.tableDetail.horizontalHeaderItem(1)
        item.setText(_translate("App", "New Column"))
        item = self.tableDetail.horizontalHeaderItem(2)
        item.setText(_translate("App", "New Column"))
        self.label.setText(_translate("App", "Column"))
        self.label_2.setText(_translate("App", "Row"))
        self.label_3.setText(_translate("App", "filter"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("App", "Table Detail"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("App", "Chart"))
        self.menuFile.setTitle(_translate("App", "File"))
        self.menuData.setTitle(_translate("App", "Data"))
        self.dataWidget.setWindowTitle(_translate("App", "Data Source"))
        self.dataCombo.setItemText(0, _translate("App", "Data Source"))
        self.label_10.setText(_translate("App", "filter"))
        self.menuOpen.setText(_translate("App", "Open"))
        self.menuSave.setText(_translate("App", "Save"))
        self.menuExit.setText(_translate("App", "Exit"))
        self.menuImport.setText(_translate("App", "Import"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    App = QtWidgets.QMainWindow()
    ui = Ui_App()
    ui.setupUi(App)
    App.show()
    sys.exit(app.exec_())
