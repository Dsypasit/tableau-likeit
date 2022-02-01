# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Widgets.DragDrop import DimensionList, MeasureList, TableGroupby


class Ui_App(object):
    def __init__(self, data):
        self.dt = data

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
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        
        self.tableDetail = TableGroupby(self, self.tab)
        self.tableDetail.setAcceptDrops(True)
        self.tableDetail.setObjectName("tableDetail")
        self.tableDetail.setColumnCount(0)
        self.tableDetail.setRowCount(0)
        self.gridLayout_4.addWidget(self.tableDetail, 2, 0, 1, 1)

        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.MeasureList = MeasureList(self, self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MeasureList.sizePolicy().hasHeightForWidth())
        self.MeasureList.setSizePolicy(sizePolicy)
        self.MeasureList.setMinimumSize(QtCore.QSize(0, 0))
        self.MeasureList.setAcceptDrops(True)
        self.MeasureList.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MeasureList.setDragEnabled(True)
        self.MeasureList.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.MeasureList.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.MeasureList.setFlow(QtWidgets.QListView.LeftToRight)
        self.MeasureList.setObjectName("MeasureList")
        self.gridLayout_2.addWidget(self.MeasureList, 2, 1, 1, 4)

        self.label_3 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.filterRow = QtWidgets.QLineEdit(self.frame)
        self.filterRow.setObjectName("filterRow")
        self.gridLayout_2.addWidget(self.filterRow, 3, 1, 1, 3)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 3, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.btnClearColumn = QtWidgets.QPushButton(self.frame)
        self.btnClearColumn.setObjectName("btnClearColumn")
        self.gridLayout_2.addWidget(self.btnClearColumn, 1, 4, 1, 1)

        self.DimensionList = DimensionList(self, self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DimensionList.sizePolicy().hasHeightForWidth())
        self.DimensionList.setSizePolicy(sizePolicy)
        self.DimensionList.setAcceptDrops(True)
        self.DimensionList.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DimensionList.setLineWidth(1)
        self.DimensionList.setDragEnabled(True)
        self.DimensionList.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.DimensionList.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.DimensionList.setFlow(QtWidgets.QListView.LeftToRight)
        self.DimensionList.setObjectName("DimensionList")
        self.gridLayout_2.addWidget(self.DimensionList, 0, 1, 1, 4)

        self.filterColumn = QtWidgets.QLineEdit(self.frame)
        self.filterColumn.setObjectName("filterColumn")
        self.gridLayout_2.addWidget(self.filterColumn, 1, 1, 1, 3)
        self.gridLayout_4.addWidget(self.frame, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_6 = QtWidgets.QFrame(self.tab_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.formLayout = QtWidgets.QFormLayout(self.frame_6)
        self.formLayout.setObjectName("formLayout")
        self.label_7 = QtWidgets.QLabel(self.frame_6)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.comboBox_3 = QtWidgets.QComboBox(self.frame_6)
        self.comboBox_3.setEditable(False)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_3)
        self.label_6 = QtWidgets.QLabel(self.frame_6)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        
        self.DimensionList_2 = DimensionList(self, self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DimensionList_2.sizePolicy().hasHeightForWidth())
        self.DimensionList_2.setSizePolicy(sizePolicy)
        self.DimensionList_2.setAcceptDrops(True)
        self.DimensionList_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DimensionList_2.setLineWidth(1)
        self.DimensionList_2.setDragEnabled(True)
        self.DimensionList_2.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.DimensionList_2.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.DimensionList_2.setFlow(QtWidgets.QListView.LeftToRight)
        self.DimensionList_2.setObjectName("DimensionList_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.DimensionList_2)

        self.label_5 = QtWidgets.QLabel(self.frame_6)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)

        self.MeasureList_2 = MeasureList(self, self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MeasureList_2.sizePolicy().hasHeightForWidth())
        self.MeasureList_2.setSizePolicy(sizePolicy)
        self.MeasureList_2.setMinimumSize(QtCore.QSize(0, 0))
        self.MeasureList_2.setAcceptDrops(True)
        self.MeasureList_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MeasureList_2.setDragEnabled(True)
        self.MeasureList_2.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.MeasureList_2.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.MeasureList_2.setFlow(QtWidgets.QListView.LeftToRight)
        self.MeasureList_2.setObjectName("MeasureList_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.MeasureList_2)

        self.verticalLayout.addWidget(self.frame_6)
        self.stackedWidget = QtWidgets.QStackedWidget(self.tab_2)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_3 = QtWidgets.QFrame(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_5.addWidget(self.frame_3, 1, 0, 1, 1)
        self.frame_9 = QtWidgets.QFrame(self.page)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.formLayout_6 = QtWidgets.QFormLayout(self.frame_9)
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_12 = QtWidgets.QLabel(self.frame_9)
        self.label_12.setObjectName("label_12")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.gridLayout_5.addWidget(self.frame_9, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame_5 = QtWidgets.QFrame(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_6.addWidget(self.frame_5, 1, 0, 1, 1)
        self.frame_8 = QtWidgets.QFrame(self.page_2)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.formLayout_5 = QtWidgets.QFormLayout(self.frame_8)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_9 = QtWidgets.QLabel(self.frame_8)
        self.label_9.setObjectName("label_9")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.gridLayout_6.addWidget(self.frame_8, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_10 = QtWidgets.QFrame(self.page_3)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.formLayout_7 = QtWidgets.QFormLayout(self.frame_10)
        self.formLayout_7.setObjectName("formLayout_7")
        self.label_13 = QtWidgets.QLabel(self.frame_10)
        self.label_13.setObjectName("label_13")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.verticalLayout_2.addWidget(self.frame_10, 0, QtCore.Qt.AlignTop)
        self.frame_7 = QtWidgets.QFrame(self.page_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_2.addWidget(self.frame_7)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_11 = QtWidgets.QFrame(self.page_4)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.formLayout_8 = QtWidgets.QFormLayout(self.frame_11)
        self.formLayout_8.setObjectName("formLayout_8")
        self.label_14 = QtWidgets.QLabel(self.frame_11)
        self.label_14.setObjectName("label_14")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.verticalLayout_3.addWidget(self.frame_11, 0, QtCore.Qt.AlignTop)
        self.frame_12 = QtWidgets.QFrame(self.page_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_3.addWidget(self.frame_12)
        self.stackedWidget.addWidget(self.page_4)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 1, 1, 1)
        App.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(App)
        self.statusbar.setObjectName("statusbar")
        App.setStatusBar(self.statusbar)
        self.dataWidget = QtWidgets.QDockWidget(App)
        self.dataWidget.setObjectName("dataWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.label_10 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)
        self.filterData = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.filterData.setObjectName("filterData")
        self.gridLayout.addWidget(self.filterData, 1, 1, 1, 1)
        self.btnClearFilterData = QtWidgets.QPushButton(self.dockWidgetContents)
        self.btnClearFilterData.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/icons8-close-384.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnClearFilterData.setIcon(icon1)
        self.btnClearFilterData.setIconSize(QtCore.QSize(10, 10))
        self.btnClearFilterData.setObjectName("btnClearFilterData")
        self.gridLayout.addWidget(self.btnClearFilterData, 1, 2, 1, 1)
        self.dataCombo = QtWidgets.QComboBox(self.dockWidgetContents)
        self.dataCombo.setObjectName("dataCombo")
        self.dataCombo.addItem("")
        self.gridLayout.addWidget(self.dataCombo, 0, 0, 1, 3)
        self.DimensionWidget = QtWidgets.QListWidget(self.dockWidgetContents)
        self.DimensionWidget.setAcceptDrops(False)
        self.DimensionWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.DimensionWidget.setDragEnabled(True)
        self.DimensionWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.DimensionWidget.setObjectName("DimensionWidget")
        self.gridLayout.addWidget(self.DimensionWidget, 2, 0, 1, 3)
        self.line = QtWidgets.QFrame(self.dockWidgetContents)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 0, 1, 3)
        self.MeasureWidget = QtWidgets.QListWidget(self.dockWidgetContents)
        self.MeasureWidget.setAcceptDrops(False)
        self.MeasureWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.MeasureWidget.setDragEnabled(True)
        self.MeasureWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.MeasureWidget.setObjectName("MeasureWidget")
        self.gridLayout.addWidget(self.MeasureWidget, 4, 0, 1, 3)
        self.dataWidget.setWidget(self.dockWidgetContents)
        App.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dataWidget)
        self.menubar = QtWidgets.QMenuBar(App)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuData = QtWidgets.QMenu(self.menubar)
        self.menuData.setObjectName("menuData")
        App.setMenuBar(self.menubar)
        self.menuOpen = QtWidgets.QAction(App)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/images/icons8-opened-folder-384.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuOpen.setIcon(icon2)
        self.menuOpen.setObjectName("menuOpen")
        self.menuSave = QtWidgets.QAction(App)
        self.menuSave.setObjectName("menuSave")
        self.menuExit = QtWidgets.QAction(App)
        self.menuExit.setObjectName("menuExit")
        self.menuImport = QtWidgets.QAction(App)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/images/icons8-document-384.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuImport.setIcon(icon3)
        self.menuImport.setObjectName("menuImport")
        self.actionUnion = QtWidgets.QAction(App)
        self.actionUnion.setObjectName("actionUnion")
        self.menuFile.addAction(self.menuOpen)
        self.menuFile.addAction(self.menuSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuExit)
        self.menuData.addAction(self.menuImport)
        self.menuData.addAction(self.actionUnion)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuData.menuAction())

        self.retranslateUi(App)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.comboBox_3.currentIndexChanged['int'].connect(self.stackedWidget.setCurrentIndex) # type: ignore
        self.stackedWidget.currentChanged['int'].connect(self.comboBox_3.setCurrentIndex) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(App)

    def retranslateUi(self, App):
        _translate = QtCore.QCoreApplication.translate
        App.setWindowTitle(_translate("App", "Tableauu"))
        self.label_3.setText(_translate("App", "filter"))
        self.label_2.setText(_translate("App", "Measure"))
        self.pushButton_2.setText(_translate("App", "Clear Row"))
        self.label_4.setText(_translate("App", "filter"))
        self.label.setText(_translate("App", "Dimension"))
        self.btnClearColumn.setText(_translate("App", "Clear Column"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("App", "Table Detail"))
        self.label_7.setText(_translate("App", "Selection Chart"))
        self.comboBox_3.setItemText(0, _translate("App", "Percentage Bar Chart"))
        self.comboBox_3.setItemText(1, _translate("App", "Nested Donut Chart"))
        self.comboBox_3.setItemText(2, _translate("App", "Line Charts"))
        self.comboBox_3.setItemText(3, _translate("App", "Bar Chart"))
        self.label_6.setText(_translate("App", "Dimension"))
        self.label_5.setText(_translate("App", "Measure"))
        self.label_12.setText(_translate("App", "Percentage Bar Chart"))
        self.label_9.setText(_translate("App", "Nested Donut Chart"))
        self.label_13.setText(_translate("App", "Line Charts"))
        self.label_14.setText(_translate("App", "Bar Chart"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("App", "Chart"))
        self.dataWidget.setWindowTitle(_translate("App", "Data Source"))
        self.label_10.setText(_translate("App", "filter"))
        self.dataCombo.setItemText(0, _translate("App", "Data Source"))
        self.menuFile.setTitle(_translate("App", "File"))
        self.menuData.setTitle(_translate("App", "Data"))
        self.menuOpen.setText(_translate("App", "Open"))
        self.menuSave.setText(_translate("App", "Save"))
        self.menuExit.setText(_translate("App", "Exit"))
        self.menuImport.setText(_translate("App", "Import"))
        self.actionUnion.setText(_translate("App", "Union"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    App = QtWidgets.QMainWindow()
    ui = Ui_App()
    ui.setupUi(App)
    App.show()
    sys.exit(app.exec_())
