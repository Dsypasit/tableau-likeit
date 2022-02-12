# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Widgets.DragDrop import DimensionList, MeasureList, TableGroupby, PlotList
from Widgets.Chart import WebEngineView


class Ui_App(object):
    def __init__(self, data):
        self.dt = data

    def setupUi(self, App):
        self.app = App
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
        
        self.tableWidget = TableGroupby(self, self.tab)
        self.tableWidget.setAcceptDrops(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_4.addWidget(self.tableWidget, 2, 0, 1, 1)
       
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btnClearColumn_2 = QtWidgets.QPushButton(self.frame)
        self.btnClearColumn_2.setObjectName("btnClearColumn_2")
        self.gridLayout_2.addWidget(self.btnClearColumn_2, 1, 2, 1, 1)
       
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
        self.gridLayout_2.addWidget(self.DimensionList, 1, 1, 1, 1)
      
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)
        self.btnClearRow_2 = QtWidgets.QPushButton(self.frame)
        self.btnClearRow_2.setObjectName("btnClearRow_2")
        self.gridLayout_2.addWidget(self.btnClearRow_2, 3, 2, 1, 1)
        
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
        self.gridLayout_2.addWidget(self.MeasureList, 3, 1, 1, 1)
      
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
        self.gridLayout_17 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame_6)
        self.comboBox_3.setEditable(False)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout_17.addWidget(self.comboBox_3, 0, 1, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.frame_6)
        self.label_7.setObjectName("label_7")
        self.gridLayout_17.addWidget(self.label_7, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_6)
        self.stackedWidget = QtWidgets.QStackedWidget(self.tab_2)
        self.stackedWidget.setMidLineWidth(0)
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
        self.frame_2 = QtWidgets.QFrame(self.page)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_7.addWidget(self.label_6, 0, 0, 1, 1)
       
        self.ColumnList_bar = PlotList(self, self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ColumnList_bar.sizePolicy().hasHeightForWidth())
        self.ColumnList_bar.setSizePolicy(sizePolicy)
        self.ColumnList_bar.setAcceptDrops(True)
        self.ColumnList_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ColumnList_bar.setLineWidth(1)
        self.ColumnList_bar.setDragEnabled(True)
        self.ColumnList_bar.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.ColumnList_bar.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.ColumnList_bar.setFlow(QtWidgets.QListView.LeftToRight)
        self.ColumnList_bar.setObjectName("ColumnList_bar")
        self.gridLayout_7.addWidget(self.ColumnList_bar, 0, 1, 1, 1)
       
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_7.addWidget(self.label_5, 2, 0, 1, 1)
   
        self.RowList_bar = PlotList(self, self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RowList_bar.sizePolicy().hasHeightForWidth())
        self.RowList_bar.setSizePolicy(sizePolicy)
        self.RowList_bar.setMinimumSize(QtCore.QSize(0, 0))
        self.RowList_bar.setAcceptDrops(True)
        self.RowList_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.RowList_bar.setDragEnabled(True)
        self.RowList_bar.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.RowList_bar.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.RowList_bar.setFlow(QtWidgets.QListView.LeftToRight)
        self.RowList_bar.setObjectName("RowList_bar")
        self.gridLayout_7.addWidget(self.RowList_bar, 2, 1, 1, 1)

        #BarChart 
        self.barChart = WebEngineView()
        self.gridLayout_5.addWidget(self.barChart, 1, 0, 1, 1)
      
        self.btnClearRow_bar = QtWidgets.QPushButton(self.frame_2)
        self.btnClearRow_bar.setObjectName("btnClearRow_bar")
        self.gridLayout_7.addWidget(self.btnClearRow_bar, 2, 2, 1, 1)
        self.btnClearColumn_bar = QtWidgets.QPushButton(self.frame_2)
        self.btnClearColumn_bar.setObjectName("btnClearColumn_bar")
        self.gridLayout_7.addWidget(self.btnClearColumn_bar, 0, 2, 1, 1)
        self.gridLayout_5.addWidget(self.frame_2, 0, 0, 1, 1)
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
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_11 = QtWidgets.QLabel(self.frame_8)
        self.label_11.setObjectName("label_11")
        self.gridLayout_10.addWidget(self.label_11, 0, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame_8)
        self.label_12.setObjectName("label_12")
        self.gridLayout_10.addWidget(self.label_12, 2, 0, 1, 1)
     
        self.ThetaList = PlotList(self, self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ThetaList.sizePolicy().hasHeightForWidth())
        self.ThetaList.setSizePolicy(sizePolicy)
        self.ThetaList.setAcceptDrops(True)
        self.ThetaList.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ThetaList.setLineWidth(1)
        self.ThetaList.setDragEnabled(True)
        self.ThetaList.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.ThetaList.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.ThetaList.setFlow(QtWidgets.QListView.LeftToRight)
        self.ThetaList.setObjectName("ThetaList")
        self.gridLayout_10.addWidget(self.ThetaList, 0, 1, 1, 1)
      
        self.ColorList = PlotList(self, self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ColorList.sizePolicy().hasHeightForWidth())
        self.ColorList.setSizePolicy(sizePolicy)
        self.ColorList.setMinimumSize(QtCore.QSize(0, 0))
        self.ColorList.setAcceptDrops(True)
        self.ColorList.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ColorList.setDragEnabled(True)
        self.ColorList.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.ColorList.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.ColorList.setFlow(QtWidgets.QListView.LeftToRight)
        self.ColorList.setObjectName("ColorList")
        self.gridLayout_10.addWidget(self.ColorList, 2, 1, 1, 1)

        #PieChart 
        self.pieChart = WebEngineView()
        self.gridLayout_6.addWidget(self.pieChart, 1, 0, 1, 1)
      
        self.btnClearColor = QtWidgets.QPushButton(self.frame_8)
        self.btnClearColor.setObjectName("btnClearColor")
        self.gridLayout_10.addWidget(self.btnClearColor, 2, 2, 1, 1)
        self.btnClearTheta = QtWidgets.QPushButton(self.frame_8)
        self.btnClearTheta.setObjectName("btnClearTheta")
        self.gridLayout_10.addWidget(self.btnClearTheta, 0, 2, 1, 1)
        self.gridLayout_6.addWidget(self.frame_8, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.frame_7 = QtWidgets.QFrame(self.page_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_9.addWidget(self.frame_7, 1, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.page_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setObjectName("label_8")
        self.gridLayout_8.addWidget(self.label_8, 0, 0, 1, 1)
       
        self.ColumnList_line = PlotList(self, self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ColumnList_line.sizePolicy().hasHeightForWidth())
        self.ColumnList_line.setSizePolicy(sizePolicy)
        self.ColumnList_line.setAcceptDrops(True)
        self.ColumnList_line.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ColumnList_line.setLineWidth(1)
        self.ColumnList_line.setDragEnabled(True)
        self.ColumnList_line.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.ColumnList_line.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.ColumnList_line.setFlow(QtWidgets.QListView.LeftToRight)
        self.ColumnList_line.setObjectName("ColumnList_line")
        self.gridLayout_8.addWidget(self.ColumnList_line, 0, 1, 1, 1)
        
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        self.label_9.setObjectName("label_9")
        self.gridLayout_8.addWidget(self.label_9, 2, 0, 1, 1)
       
        self.RowList_line = PlotList(self, self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RowList_line.sizePolicy().hasHeightForWidth())
        self.RowList_line.setSizePolicy(sizePolicy)
        self.RowList_line.setMinimumSize(QtCore.QSize(0, 0))
        self.RowList_line.setAcceptDrops(True)
        self.RowList_line.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.RowList_line.setDragEnabled(True)
        self.RowList_line.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.RowList_line.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.RowList_line.setFlow(QtWidgets.QListView.LeftToRight)
        self.RowList_line.setObjectName("RowList_line")
        self.gridLayout_8.addWidget(self.RowList_line, 2, 1, 1, 1)

        #LineChart 
        self.lineChart = WebEngineView()
        self.gridLayout_9.addWidget(self.lineChart, 1, 0, 1, 1)
      
        self.btnClearRow_line = QtWidgets.QPushButton(self.frame_4)
        self.btnClearRow_line.setObjectName("btnClearRow_line")
        self.gridLayout_8.addWidget(self.btnClearRow_line, 2, 2, 1, 1)
        self.btnClearColumn_line = QtWidgets.QPushButton(self.frame_4)
        self.btnClearColumn_line.setObjectName("btnClearColumn_line")
        self.gridLayout_8.addWidget(self.btnClearColumn_line, 0, 2, 1, 1)
        self.gridLayout_9.addWidget(self.frame_4, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
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
        self.btnClearColumn_2.setText(_translate("App", "Clear Dimension"))
        self.label.setText(_translate("App", "Dimension"))
        self.label_2.setText(_translate("App", "Measure"))
        self.btnClearRow_2.setText(_translate("App", "Clear Measure"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("App", "Table Detail"))
        self.comboBox_3.setItemText(0, _translate("App", "Bar Chart"))
        self.comboBox_3.setItemText(1, _translate("App", "Pie Chart"))
        self.comboBox_3.setItemText(2, _translate("App", "Line Charts"))
        self.label_7.setText(_translate("App", "Selection Chart"))
        self.label_6.setText(_translate("App", "Column"))
        self.label_5.setText(_translate("App", "Row"))
        self.btnClearRow_bar.setText(_translate("App", "Clear Row"))
        self.btnClearColumn_bar.setText(_translate("App", "Clear Column"))
        self.label_11.setText(_translate("App", "Theta"))
        self.label_12.setText(_translate("App", "Color"))
        self.btnClearColor.setText(_translate("App", "Clear Color"))
        self.btnClearTheta.setText(_translate("App", "Clear Theta"))
        self.label_8.setText(_translate("App", "Column"))
        self.label_9.setText(_translate("App", "Row"))
        self.btnClearRow_line.setText(_translate("App", "Clear Row"))
        self.btnClearColumn_line.setText(_translate("App", "Clear Column"))
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
