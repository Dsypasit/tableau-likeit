########################################################################
## CONVERT .UI & .QRC
# pyrcc5 resources.qrc -o resource_rc.py
# pyuic5 -x ui_interface.ui -o ui_interfaceDemo.py 
########################################################################

########################################################################
## IMPORTS
########################################################################
from json import tool
import os
import sys, random
import re

import altair as alt
from matplotlib.pyplot import title
from vega_datasets import data
import pandas as pd
import numpy as np

# Disabling MaxRowsError
alt.data_transformers.disable_max_rows()

from Widgets.DataManipulate import data_manipulate
from Widgets.DateItem import DateWidgetItem
from Widgets.Chart import WebEngineView

########################################################################
# IMPORT GUI FILE
from ui_interfaceDemo import *
from PyQt5.QtWidgets import *
from PyQt5.QtChart import QChart, QChartView, QValueAxis, QBarCategoryAxis, QBarSet, QBarSeries
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
        self.i1 = None
        self.i2 = None
        self.ip1 = None
        self.ip2 = None
        self.il1 = None
        self.il2 = None

        #######################################################################
        # ADD FUNCTION ELEMENT
        #######################################################################
        self.ui.menuImport.triggered.connect(self.open_file)
        self.ui.actionUnion.triggered.connect(self.union_file)
        self.ui.menuExit.triggered.connect(qApp.quit)

        self.ui.DimensionWidget.itemDoubleClicked.connect(self.to_measure)
        self.ui.MeasureWidget.itemDoubleClicked.connect(self.to_dimension)
        self.ui.MeasureList.itemChanged.connect(lambda: self.ui.tableWidget.make_table())
        self.ui.dataCombo.currentIndexChanged.connect(self.change_data)

        self.ui.filterData.textEdited.connect(self.searchDimensionMeasure)
        self.ui.btnClearFilterData.clicked.connect(self.clearSearch)

        self.ui.btnClearColumn_2.clicked.connect(self.ui.DimensionList.resetAll)
        self.ui.btnClearRow_2.clicked.connect(self.ui.MeasureList.resetAll)

        self.ui.btnClearColumn_bar.clicked.connect(self.ui.ColumnList_bar.resetAll)
        self.ui.btnClearRow_bar.clicked.connect(self.ui.RowList_bar.resetAll)

        self.ui.btnClearColumn_line.clicked.connect(self.ui.ColumnList_line.resetAll)
        self.ui.btnClearRow_line.clicked.connect(self.ui.RowList_line.resetAll)

        self.ui.btnClearTheta.clicked.connect(self.ui.ThetaList.resetAll)
        self.ui.btnClearColor.clicked.connect(self.ui.ColorList.resetAll)
        #######################################################################
        # SHOW WINDOW
        #######################################################################
        self.show()
        #######################################################################

    ########################################################################
    ## FUNCTION
    ########################################################################
    def change_data(self, index: int) -> None:
        """ This method working when change file"""
        if self.ui.dataCombo.count():
            self.ui.dataCombo.setCurrentIndex(index)
            self.dt.load_data(self.ui.dataCombo.itemText(index))    # load selected data
            self.dt.separated_dimension_measure()   # separated measure, dimension
            self.clear_all()
            self.make_table()
            self.dimension()
            self.Graph()
    
    def clear_all(self):
        self.ui.DimensionList.dimension = {}
        self.ui.MeasureList.measure = {}
        self.ui.MeasureList.measure_filter = {}
        self.ui.ColumnList_bar.resetAll()
        self.ui.RowList_bar.resetAll()
        self.ui.ColumnList_line.resetAll()
        self.ui.RowList_line.resetAll()
        self.ui.ThetaList.resetAll()
        self.ui.ColorList.resetAll()
        for i in range(self.ui.DimensionWidget.count()):   
            self.ui.DimensionWidget.takeItem(0)
        for i in range(self.ui.MeasureWidget.count()):   
            self.ui.MeasureWidget.takeItem(0)    
        for i in range(self.ui.DimensionList.count()):   
            self.ui.DimensionList.takeItem(0)
        for i in range(self.ui.MeasureList.count()):   
            self.ui.MeasureList.takeItem(0)    
        for i in range(self.ui.ColumnList_bar.count()):   
            self.ui.ColumnList_bar.takeItem(0)
        for i in range(self.ui.RowList_bar.count()):   
            self.ui.RowList_bar.takeItem(0)    
        for i in range(self.ui.ThetaList.count()):   
            self.ui.ThetaList.takeItem(0)    
        for i in range(self.ui.ColorList.count()):   
            self.ui.ColorList.takeItem(0)    
        for i in range(self.ui.ColumnList_line.count()):   
            self.ui.ColumnList_line.takeItem(0)    
        for i in range(self.ui.RowList_line.count()):   
            self.ui.RowList_line.takeItem(0)    

    def to_dimension(self, item: QtWidgets.QWidgetItem) -> None:
        """Thise method will change measure item to dimension item"""
        self.dt.change_to_dimension(item.text())
        self.dimension()

    def to_measure(self, item: QtWidgets.QWidgetItem):
        """Thise method will change measure item to measure item"""
        self.dt.change_to_measure(item.text())
        self.dimension()

    def union_file(self):
        """ This method will union selected file to current file"""
        filename, _ = QFileDialog.getOpenFileName(None, "open File", "", "CSV file (*.csv);; Excel file (*.xlsx)")
        if filename:
            self.path = filename
            self.dt.unioun_data(filename)
            self.make_table()
            self.dimension()
            self.Graph()
    
    def open_file(self):
        """ This method will load file to vitualize"""
        filename, _ = QFileDialog.getOpenFileName(None, "open File", "", "CSV file (*.csv);; Excel file (*.xlsx)")
        if filename:
            self.path = filename
            self.dt.load_data(filename)

            self.dataCombo.append(filename)
            self.ui.dataCombo.clear()
            self.ui.dataCombo.addItems(self.dataCombo)

            self.clear_all()
            # self.make_table()
            self.dt.separated_dimension_measure()
            self.dimension()
            # self.Graph()

    def make_table(self):
        """ This method will make table """
        self.header = self.dt.get_column() # get column and data
        self.data = self.dt.get_data()
        self.ui.tableWidget.setColumnCount(len(self.header))
        self.ui.tableWidget.setRowCount(len(self.data))
        self.ui.tableWidget.setHorizontalHeaderLabels(self.header)
        for row in range(len(self.data)):
            for col, item in enumerate(self.data[row]):
                if type(item) in (int, float):  # check item type
                    newItem = QTableWidgetItem()
                    newItem.setData(QtCore.Qt.DisplayRole, item)
                elif re.match('^(0[1-9]|[12][0-9]|3[01]|[1-9])/(0[1-9]|1[0-2]|[1-9])/\d{4}$', str(item)): # check date column
                    newItem = DateWidgetItem(str(item))
                else:
                    newItem = QTableWidgetItem(str(item))
                self.ui.tableWidget.setItem(row, col, newItem)

    def dimension(self):
        """ This method will make measure list widget and dimension list widget"""
        for i in range(self.ui.DimensionWidget.count()):    # clear dimension widget item
            self.ui.DimensionWidget.takeItem(0)
        for i in range(self.ui.MeasureWidget.count()):      # clear measure widget item
            self.ui.MeasureWidget.takeItem(0)
        dimension = self.dt.get_dimension()
        measure = self.dt.get_measure()
        for i in dimension:
            item = QListWidgetItem("{}".format(i))
            self.ui.DimensionWidget.addItem(item)
        for i in measure:
            item = QListWidgetItem("{}".format(i))
            self.ui.MeasureWidget.addItem(item)

    def check_dup(self, i1, i2, old_i1, old_i2):
        """ This method will check duplicate between two list and compare previouse two list """
        it1 = i1
        it2 = i2
        if old_i1 == i1 and old_i2 != i2:
            for i in i1:
                if i in i2:
                    it1.remove(i)
        elif old_i2 == i2 and old_i1 != i1:
            for i in i2:
                if i in i1:
                    it2.remove(i)
        return it1, it2

    def searchDimensionMeasure(self,e):
        """This method will search Dimension Measure in data source"""
        if e == "":
            self.dimension()
            return 
        # set dimension & measure
        dimension = self.dt.get_dimension()
        measure = self.dt.get_measure()
        # clear data when edit
        for i in range(self.ui.DimensionWidget.count()):   
            self.ui.DimensionWidget.takeItem(0)
        for i in range(self.ui.MeasureWidget.count()):   
            self.ui.MeasureWidget.takeItem(0)    
        # add item in DimensionWidget
        for fil in dimension:
            if e.lower() in fil.lower():
                item = QtWidgets.QListWidgetItem(fil)
                self.ui.DimensionWidget.addItem(item)
        # add item in MeasureWidget
        for fil in measure:
            if e.lower() in fil.lower():
                item = QtWidgets.QListWidgetItem(fil)
                self.ui.MeasureWidget.addItem(item)
    def clearSearch(self):
        """This method will clear search Dimension Measure in data source"""
        self.ui.filterData.clear()
        self.dimension()
        

    ########################################################################
    ## FUNCTION GRAPH
    ########################################################################
    def Graph(self):
        """
        This method will create Graph, it check every listwidget when items in list widget is change
        
        ...

        Chart can create now
        ----------
        - bar chart 
        - pie chart 
        - line chart    # in fact, in Tableau line axis x can use Date only Now not available
        
        """
        ########################################################################
        ## BAR CHART
        ########################################################################
        item_BarColumn, fil_BarColumn, measure_BarColumn = self.ui.ColumnList_bar.get_plot_item()
        item_BarRow, fil_BarRow, measure_BarRow  = self.ui.RowList_bar.get_plot_item()
        item_BarColumn, item_BarRow = self.check_dup(item_BarColumn, item_BarRow, self.i1, self.i2)
        data = None
        self.i1 = item_BarColumn
        self.i2 = item_BarRow
        test_bar = []
        tooltip_bar = []
        check_colrow = {'row':False, 'column':False, 'resolve_scale':True}

        min_bar = 0
        max_bar = 0

        if(len(item_BarColumn)>0 or len(item_BarRow)>0):
            data = self.dt.data_filter(item_BarColumn, item_BarRow , fil_BarColumn, fil_BarRow, measure_BarColumn, measure_BarRow)
           
            coll_Di_bar = {'row':{'count':0, 'list':[]},'column':{'count':0, 'list':[]}}
            coll_Me_bar = {'row':{'count':0, 'list':[]},'column':{'count':0, 'list':[]}}
            for i in item_BarColumn:
                if i in measure_BarColumn.keys() : 
                    coll_Me_bar['column']['count'] += 1
                    coll_Me_bar['column']['list'].append(i)
                else : 
                    coll_Di_bar['column']['count'] += 1
                    coll_Di_bar['column']['list'].append(i)
            for i in item_BarRow:
                if i in measure_BarRow.keys() : 
                    coll_Me_bar['row']['count'] += 1
                    coll_Me_bar['row']['list'].append(i)
                else : 
                    coll_Di_bar['row']['count'] += 1
                    coll_Di_bar['row']['list'].append(i)
            
            coll_Di_bar['row']['list'].reverse()
            coll_Di_bar['column']['list'].reverse()

            # print("coll_Di_bar['row']",coll_Di_bar['row']," \
            #     coll_Di_bar['column']",coll_Di_bar['column'])
            # print("coll_Me_bar['row']",coll_Me_bar['row']," \
            #     coll_Me_bar['column']",coll_Me_bar['column']) 

            # Check 1 Measure in ROW/COLUMN
            if coll_Me_bar['column']['count'] == 1 : #todo: a Measure in column
                check_colrow['column'] = True   # have Measure in Column
                if coll_Di_bar['row']['count'] == 1 :       # 1 dimension in row 
                    # check scale
                    if coll_Di_bar['column']['count'] == 0 :    # dimension row 1 col 0
                        tempMax = data.groupby([coll_Di_bar['row']['list'][0]], as_index=False)[coll_Me_bar['column']['list'][0]].agg(measure_BarColumn[coll_Me_bar['column']['list'][0]]).max()[1]
                        tempMin = data.groupby([coll_Di_bar['row']['list'][0]], as_index=False)[coll_Me_bar['column']['list'][0]].agg(measure_BarColumn[coll_Me_bar['column']['list'][0]]).min()[1]
                        if max_bar < int(tempMax) : max_bar = int(tempMax)
                        if min_bar > int(tempMin) : min_bar = int(tempMin)
                    elif coll_Di_bar['column']['count'] > 0 :   # dimension row 1 col > 0
                        tempMax = data.groupby([coll_Di_bar['column']['list'][0], coll_Di_bar['row']['list'][0]], as_index=False)[coll_Me_bar['column']['list'][0]].agg(measure_BarColumn[coll_Me_bar['column']['list'][0]]).max()[2]
                        tempMin = data.groupby([coll_Di_bar['column']['list'][0], coll_Di_bar['row']['list'][0]], as_index=False)[coll_Me_bar['column']['list'][0]].agg(measure_BarColumn[coll_Me_bar['column']['list'][0]]).min()[2]
                        if max_bar < int(tempMax) : max_bar = int(tempMax)
                        if min_bar > int(tempMin) : min_bar = int(tempMin)

                    # print(coll_Di_bar['row']['list'][0],' max_bar : ',max_bar,' min_bar : ',min_bar)

                    test_bar.append(alt.X(f"{measure_BarColumn[coll_Me_bar['column']['list'][0]]}({coll_Me_bar['column']['list'][0]})",scale=alt.Scale(domain=(min_bar, max_bar),clamp=True )))

                elif coll_Di_bar['row']['count'] >= 2 :     # 2 & 3 dimension in row
                    # check scale
                    if coll_Di_bar['column']['count'] == 0 :    # # dimension row > 1 col 0
                        tempMax = data.groupby([coll_Di_bar['row']['list'][0], coll_Di_bar['row']['list'][1]], as_index=False)[coll_Me_bar['column']['list'][0]].agg(measure_BarColumn[coll_Me_bar['column']['list'][0]]).max()[2]
                        tempMin = data.groupby([coll_Di_bar['row']['list'][0], coll_Di_bar['row']['list'][1]], as_index=False)[coll_Me_bar['column']['list'][0]].agg(measure_BarColumn[coll_Me_bar['column']['list'][0]]).min()[2]
                        if max_bar < int(tempMax) : max_bar = int(tempMax)
                        if min_bar > int(tempMin) : min_bar = int(tempMin)

                    elif coll_Di_bar['column']['count'] > 0 :  # # dimension row > 1 col > 0
                        tempMax = data.groupby([coll_Di_bar['column']['list'][0], coll_Di_bar['row']['list'][0], coll_Di_bar['row']['list'][1]], as_index=False)[coll_Me_bar['column']['list'][0]].agg(measure_BarColumn[coll_Me_bar['column']['list'][0]]).max()[3]
                        tempMin = data.groupby([coll_Di_bar['column']['list'][0], coll_Di_bar['row']['list'][0], coll_Di_bar['row']['list'][1]], as_index=False)[coll_Me_bar['column']['list'][0]].agg(measure_BarColumn[coll_Me_bar['column']['list'][0]]).min()[3]
                        if max_bar < int(tempMax) : max_bar = int(tempMax)
                        if min_bar > int(tempMin) : min_bar = int(tempMin)

                    test_bar.append(alt.X(f"{measure_BarColumn[coll_Me_bar['column']['list'][0]]}({coll_Me_bar['column']['list'][0]})",scale=alt.Scale(domain=(min_bar, max_bar),clamp=True )))

                else :  # 0 dimension in row
                    test_bar.append(alt.X(f"{measure_BarColumn[coll_Me_bar['column']['list'][0]]}({coll_Me_bar['column']['list'][0]})"))

                tooltip_bar.append(f"{measure_BarColumn[coll_Me_bar['column']['list'][0]]}({coll_Me_bar['column']['list'][0]})")

            elif coll_Me_bar['row']['count'] == 1 : #todo: a Measure in row
                check_colrow['row'] = True      # have Measure in Row
                if coll_Di_bar['column']['count'] == 1 :    # 1 dimension in column
                    # check scale
                    if coll_Di_bar['row']['count'] == 0 :   # dimension row 0 col 1
                        tempMax = data.groupby([coll_Di_bar['column']['list'][0]], as_index=False)[coll_Me_bar['row']['list'][0]].agg(measure_BarRow[coll_Me_bar['row']['list'][0]]).max()[1]
                        tempMin = data.groupby([coll_Di_bar['column']['list'][0]], as_index=False)[coll_Me_bar['row']['list'][0]].agg(measure_BarRow[coll_Me_bar['row']['list'][0]]).min()[1]
                        if max_bar < int(tempMax) : max_bar = int(tempMax)
                        if min_bar > int(tempMin) : min_bar = int(tempMin)

                    elif coll_Di_bar['row']['count'] > 0 :    # dimension row > 0 col 1
                        tempMax = data.groupby([coll_Di_bar['row']['list'][0], coll_Di_bar['column']['list'][0]], as_index=False)[coll_Me_bar['row']['list'][0]].agg(measure_BarRow[coll_Me_bar['row']['list'][0]]).max()[2]
                        tempMin = data.groupby([coll_Di_bar['row']['list'][0], coll_Di_bar['column']['list'][0]], as_index=False)[coll_Me_bar['row']['list'][0]].agg(measure_BarRow[coll_Me_bar['row']['list'][0]]).min()[2]
                        if max_bar < int(tempMax) : max_bar = int(tempMax)
                        if min_bar > int(tempMin) : min_bar = int(tempMin)

                    test_bar.append(alt.Y(f"{measure_BarRow[coll_Me_bar['row']['list'][0]]}({coll_Me_bar['row']['list'][0]})", scale=alt.Scale(domain=(min_bar, max_bar), clamp=True )))

                elif coll_Di_bar['column']['count'] >= 2 : # 2 & 3 dimension in column
                    # check scale
                    if coll_Di_bar['row']['count'] == 0 :   # dimension row 0 col > 1
                        tempMax = data.groupby([coll_Di_bar['column']['list'][0], coll_Di_bar['column']['list'][1]], as_index=False)[coll_Me_bar['row']['list'][0]].agg(measure_BarRow[coll_Me_bar['row']['list'][0]]).max()[2]
                        tempMin = data.groupby([coll_Di_bar['column']['list'][0], coll_Di_bar['column']['list'][1]], as_index=False)[coll_Me_bar['row']['list'][0]].agg(measure_BarRow[coll_Me_bar['row']['list'][0]]).min()[2]
                        if max_bar < int(tempMax) : max_bar = int(tempMax)
                        if min_bar > int(tempMin) : min_bar = int(tempMin)

                    elif coll_Di_bar['row']['count'] > 0 :   # dimension row > 0 col > 1
                        tempMax = data.groupby([coll_Di_bar['row']['list'][0], coll_Di_bar['column']['list'][0], coll_Di_bar['column']['list'][1]], as_index=False)[coll_Me_bar['row']['list'][0]].agg(measure_BarRow[coll_Me_bar['row']['list'][0]]).max()[3]
                        tempMin = data.groupby([coll_Di_bar['row']['list'][0], coll_Di_bar['column']['list'][0], coll_Di_bar['column']['list'][1]], as_index=False)[coll_Me_bar['row']['list'][0]].agg(measure_BarRow[coll_Me_bar['row']['list'][0]]).min()[3]
                        if max_bar < int(tempMax) : max_bar = int(tempMax)
                        if min_bar > int(tempMin) : min_bar = int(tempMin)

                    test_bar.append(alt.Y(f"{measure_BarRow[coll_Me_bar['row']['list'][0]]}({coll_Me_bar['row']['list'][0]})", scale=alt.Scale(domain=(min_bar, max_bar), clamp=True )))

                else :  # 0 dimension in column
                    test_bar.append(alt.Y(f"{measure_BarRow[coll_Me_bar['row']['list'][0]]}({coll_Me_bar['row']['list'][0]})"))

                tooltip_bar.append(f"{measure_BarRow[coll_Me_bar['row']['list'][0]]}({coll_Me_bar['row']['list'][0]})")

            ########################################################################
            ##todo dimension&measure in same ROW/COLUMN
            # a Dimension Measure in column
            if (coll_Me_bar['column']['count'] == 1) and (coll_Di_bar['column']['count'] == 1) and (coll_Di_bar['row']['count'] == 0):
                # check scale
                tempMax = data.groupby([coll_Di_bar['column']['list'][0]], as_index=False)[coll_Me_bar['column']['list'][0]].agg(measure_BarColumn[coll_Me_bar['column']['list'][0]]).max()[1]
                tempMin = data.groupby([coll_Di_bar['column']['list'][0]], as_index=False)[coll_Me_bar['column']['list'][0]].agg(measure_BarColumn[coll_Me_bar['column']['list'][0]]).min()[1]
                if max_bar < int(tempMax) : max_bar = int(tempMax)
                if min_bar > int(tempMin) : min_bar = int(tempMin)

                test_bar, tooltip_bar = [], []
                test_bar.append(alt.X(f"{measure_BarColumn[coll_Me_bar['column']['list'][0]]}({coll_Me_bar['column']['list'][0]})", scale=alt.Scale(domain=(min_bar, max_bar), clamp=True )))
                tooltip_bar.append(f"{measure_BarColumn[coll_Me_bar['column']['list'][0]]}({coll_Me_bar['column']['list'][0]})")
                test_bar.append(alt.Column(coll_Di_bar['column']['list'][0]))
                tooltip_bar.append(coll_Di_bar['column']['list'][0])
                

            # a Dimension Measure in row
            elif (coll_Me_bar['row']['count'] == 1) and (coll_Di_bar['column']['count'] == 0) and (coll_Di_bar['row']['count'] == 1) :
                # check scale
                tempMax = data.groupby([coll_Di_bar['row']['list'][0]], as_index=False)[coll_Me_bar['row']['list'][0]].agg(measure_BarRow[coll_Me_bar['row']['list'][0]]).max()[1]
                tempMin = data.groupby([coll_Di_bar['row']['list'][0]], as_index=False)[coll_Me_bar['row']['list'][0]].agg(measure_BarRow[coll_Me_bar['row']['list'][0]]).min()[1]
                if max_bar < int(tempMax) : max_bar = int(tempMax)
                if min_bar > int(tempMin) : min_bar = int(tempMin)

                test_bar, tooltip_bar = [], []
                test_bar.append(alt.Y(f"{measure_BarRow[coll_Me_bar['row']['list'][0]]}({coll_Me_bar['row']['list'][0]})", scale=alt.Scale(domain=(min_bar, max_bar), clamp=True )))
                tooltip_bar.append(f"{measure_BarRow[coll_Me_bar['row']['list'][0]]}({coll_Me_bar['row']['list'][0]})")
                test_bar.append(alt.Row(coll_Di_bar['row']['list'][0]))
                tooltip_bar.append(coll_Di_bar['row']['list'][0])
            ########################################################################
            else :   
                # Part Dimension ROW
                if coll_Di_bar['row']['count'] >= 1:
                    if check_colrow['row'] :
                        test_bar.append(alt.Row(coll_Di_bar['row']['list'][0]+':O'))
                        tooltip_bar.append(coll_Di_bar['row']['list'][0]+':O')
                        check_colrow['resolve_scale'] = False
                    else:
                        test_bar.append(alt.Y(coll_Di_bar['row']['list'][0]+':O'))
                        tooltip_bar.append(coll_Di_bar['row']['list'][0]+':O')
                if coll_Di_bar['row']['count'] >= 2:
                    if check_colrow['row'] :
                        test_bar.append(alt.Color(coll_Di_bar['row']['list'][1]+':O'))
                        tooltip_bar.append(coll_Di_bar['row']['list'][1]+':O')
                    else:
                        test_bar.append(alt.Row(coll_Di_bar['row']['list'][1]+':O'))
                        tooltip_bar.append(coll_Di_bar['row']['list'][1]+':O')
                if coll_Di_bar['row']['count'] >= 3:
                    if check_colrow['row'] :
                        pass    # Not do anything when it more than >3
                    else:
                        test_bar.append(alt.Color(coll_Di_bar['row']['list'][2]+':O'))
                        tooltip_bar.append(coll_Di_bar['row']['list'][2]+':O')
                # Part Dimension COLUMN
                if coll_Di_bar['column']['count'] >= 1:
                    if check_colrow['column'] :
                        test_bar.append(alt.Column(coll_Di_bar['column']['list'][0]+':O'))
                        tooltip_bar.append(coll_Di_bar['column']['list'][0]+':O')
                        check_colrow['resolve_scale'] = False
                    else:
                        test_bar.append(alt.X(coll_Di_bar['column']['list'][0]+':O'))
                        tooltip_bar.append(coll_Di_bar['column']['list'][0]+':O')
                if coll_Di_bar['column']['count'] >= 2:
                    if check_colrow['column'] :
                        test_bar.append(alt.Color(coll_Di_bar['column']['list'][1]+':O'))
                        tooltip_bar.append(coll_Di_bar['column']['list'][1]+':O')
                    else:
                        test_bar.append(alt.Column(coll_Di_bar['column']['list'][1]+':O'))
                        tooltip_bar.append(coll_Di_bar['column']['list'][1]+':O')
                if coll_Di_bar['column']['count'] >= 3:
                    if check_colrow['column'] :
                        pass    # Not do anything when it more than >3
                    else:
                        test_bar.append(alt.Color(coll_Di_bar['column']['list'][2]+':O'))
                        tooltip_bar.append(coll_Di_bar['column']['list'][2]+':O')
            
        ########################################################################
            '''Create Bar Chart'''    
            # measure >1
            if (coll_Me_bar['row']['count'] > 1) or (coll_Me_bar['column']['count'] > 1) : 
                bar_charts = []
                # tooltip_bar.pop(0) # del tooltip first measure

                if  coll_Me_bar['row']['count'] > 1 :   # Measure row 
                    for i in range(coll_Me_bar['row']['count']):
                        # edit tooltip
                        temp_tooltip = tooltip_bar.copy()
                        temp_tooltip.append(f"{measure_BarRow[coll_Me_bar['row']['list'][i]]}({coll_Me_bar['row']['list'][i]})")
                        temp_test_bar = test_bar.copy()
                        min_bar, max_bar= 0, 0
                        
                        if coll_Di_bar['column']['count'] == 1 :       # 1 dimension
                            # check scale
                            tempMax = data.groupby([coll_Di_bar['column']['list'][0]], as_index=False)[coll_Me_bar['row']['list'][i]].agg(measure_BarRow[coll_Me_bar['row']['list'][i]]).max()[1]
                            tempMin = data.groupby([coll_Di_bar['column']['list'][0]], as_index=False)[coll_Me_bar['row']['list'][i]].agg(measure_BarRow[coll_Me_bar['row']['list'][i]]).min()[1]
                            if max_bar < int(tempMax) : max_bar = int(tempMax)
                            if min_bar > int(tempMin) : min_bar = int(tempMin)

                            temp_test_bar.append(alt.Y(f"{measure_BarRow[coll_Me_bar['row']['list'][i]]}({coll_Me_bar['row']['list'][i]})",scale=alt.Scale(domain=(min_bar, max_bar),clamp=True )))
                        
                        elif coll_Di_bar['column']['count'] >= 2 :      # 2 & 3 dime???nsion
                            # check scale
                            tempMax = data.groupby([coll_Di_bar['column']['list'][0], coll_Di_bar['column']['list'][1]], as_index=False)[coll_Me_bar['row']['list'][i]].agg(measure_BarRow[coll_Me_bar['row']['list'][i]]).max()[2]
                            tempMin = data.groupby([coll_Di_bar['column']['list'][0], coll_Di_bar['column']['list'][1]], as_index=False)[coll_Me_bar['row']['list'][i]].agg(measure_BarRow[coll_Me_bar['row']['list'][i]]).min()[2]
                            if max_bar < int(tempMax) : max_bar = int(tempMax)
                            if min_bar > int(tempMin) : min_bar = int(tempMin)

                            temp_test_bar.append(alt.Y(f"{measure_BarRow[coll_Me_bar['row']['list'][i]]}({coll_Me_bar['row']['list'][i]})",scale=alt.Scale(domain=(min_bar, max_bar),clamp=True )))

                        else :      # 0 dimension
                            temp_test_bar.append(alt.Y(f"{measure_BarRow[coll_Me_bar['row']['list'][i]]}({coll_Me_bar['row']['list'][i]})"))
                        
                        # print(temp_test_bar)
                        bar_charts.append(alt.Chart(data).mark_bar().encode(*temp_test_bar,alt.Tooltip(temp_tooltip))
                        .resolve_scale(
                            x='independent',
                            y='independent'
                        ))

                    barchart = alt.vconcat(*bar_charts)

                elif coll_Me_bar['column']['count'] > 1 :   # Measure column 
                    for i in range(coll_Me_bar['column']['count']):
                        # edit tooltip
                        temp_tooltip = tooltip_bar.copy()
                        temp_tooltip.append(f"{measure_BarColumn[coll_Me_bar['column']['list'][i]]}({coll_Me_bar['column']['list'][i]})")
                        temp_test_bar = test_bar.copy()
                        
                        min_bar, max_bar= 0, 0
                        if coll_Di_bar['row']['count'] == 1 :       # 1 dimension
                            # check scale
                            tempMax = data.groupby([coll_Di_bar['row']['list'][0]], as_index=False)[coll_Me_bar['column']['list'][i]].agg(measure_BarColumn[coll_Me_bar['column']['list'][i]]).max()[1]
                            tempMin = data.groupby([coll_Di_bar['row']['list'][0]], as_index=False)[coll_Me_bar['column']['list'][i]].agg(measure_BarColumn[coll_Me_bar['column']['list'][i]]).min()[1]
                            if max_bar < int(tempMax) : max_bar = int(tempMax)
                            if min_bar > int(tempMin) : min_bar = int(tempMin)

                            temp_test_bar.append(alt.X(f"{measure_BarColumn[coll_Me_bar['column']['list'][i]]}({coll_Me_bar['column']['list'][i]})",scale=alt.Scale(domain=(min_bar, max_bar),clamp=True )))
                        
                        elif coll_Di_bar['row']['count'] >= 2 :     # 2 & 3 dimension
                            # check scale
                            tempMax = data.groupby([coll_Di_bar['row']['list'][0], coll_Di_bar['row']['list'][1]], as_index=False)[coll_Me_bar['column']['list'][i]].sum().max()[2]
                            tempMin = data.groupby([coll_Di_bar['row']['list'][0], coll_Di_bar['row']['list'][1]], as_index=False)[coll_Me_bar['column']['list'][i]].sum().min()[2]
                            if max_bar < int(tempMax) : max_bar = int(tempMax)
                            if min_bar > int(tempMin) : min_bar = int(tempMin)

                            temp_test_bar.append(alt.X(f"{measure_BarColumn[coll_Me_bar['column']['list'][i]]}({coll_Me_bar['column']['list'][i]})",scale=alt.Scale(domain=(min_bar, max_bar),clamp=True )))

                        else :      # 0 dimension
                            temp_test_bar.append(alt.X(f"{measure_BarColumn[coll_Me_bar['column']['list'][i]]}({coll_Me_bar['column']['list'][i]})"))
                    
                        bar_charts.append(alt.Chart(data).mark_bar().encode(*temp_test_bar,alt.Tooltip(temp_tooltip)).resolve_scale( x='independent', y='independent' ))

                    barchart = alt.concat(*bar_charts)

            # measure =1
            else : 
                # Create Bar Chart        
                test_bar.append(alt.Tooltip(tooltip_bar))
                if  check_colrow['resolve_scale'] :
                    barchart = alt.Chart(data).mark_bar().encode(*test_bar).resolve_scale(x='independent', y='independent')
                else : barchart = alt.Chart(data).mark_bar().encode(*test_bar)
            # Set chart
            self.ui.barChart.updateChart(barchart)

        ########################################################################

         ########################################################################
        ## PIE CHART
        ########################################################################
        item_Theta, fil_Theta, measure_Theta = self.ui.ThetaList.get_plot_item()
        item_Color, fil_Color, measure_Color  = self.ui.ColorList.get_plot_item()

        if(len(item_Theta)>0 or len(item_Color)>0):
            data = self.dt.data_filter(item_Theta, item_Color , fil_Theta, fil_Color, measure_Theta, measure_Color )

            thetaList = item_Theta.copy()
            thetaList.reverse()
            colorList = item_Color.copy()
            colorList.reverse()

            theta_charts = []
            temp_chart_pie = []
            temp_tooltip_pie = []

            # theta >= 2
            if (len(thetaList) > 1) and (thetaList[0] not in measure_Theta.keys()):
                        temp_chart_pie.append(alt.Column(thetaList[0]))
                        temp_tooltip_pie.append(thetaList[0])
            # color >= 2
            if (len(colorList) > 1) and (colorList[0] not in measure_Color.keys()):
                        temp_chart_pie.append(alt.Row(colorList[0]))
                        temp_tooltip_pie.append(colorList[0])

            # have only item_Theta
            if  (len(item_Theta)>=1) and (len(item_Color)==0) : 
                if len(thetaList) == 1 :
                    temp = thetaList[0]
                    title = temp
                    # Check item is Measure
                    if temp in measure_Theta.keys(): 
                        title = f"{measure_Theta[temp]} of {temp}"
                        temp = f"{measure_Theta[temp]}({temp}):Q"

                    piechart = alt.Chart(data).mark_arc().encode(
                            alt.Theta(temp),
                            alt.Tooltip([temp])
                        ).properties(
                            title = title
                        ).resolve_scale(theta="independent", color="independent")

                elif len(thetaList) > 1 :
                    theta_chart = []
                    for j in range(1,len(thetaList)):
                        temp = thetaList[j]
                        title = temp
                        # Check item is Measure
                        if temp in measure_Theta.keys(): 
                            title = f"{measure_Theta[temp]} of {temp}"
                            temp = f"{measure_Theta[temp]}({temp}):Q"

                        theta_chart.append(alt.Chart(data).mark_arc().encode(
                            *temp_chart_pie, alt.Theta(temp),
                            alt.Tooltip([*temp_tooltip_pie, temp])
                        ).properties(
                            title = title
                        ))
                    piechart = alt.hconcat(*theta_chart).resolve_scale(theta="independent", color="independent")
                    
            # have only item_Color
            elif  (len(item_Theta)==0) and (len(item_Color)>=1) : 
                if len(colorList) == 1 :
                    temp = colorList[0]
                    title = temp
                    # Check item is Measure
                    if temp in measure_Color.keys(): 
                        title = f"{measure_Color[temp]} of {temp}"
                        temp = f"{measure_Color[temp]}({temp}):Q"

                    piechart = alt.Chart(data).mark_arc().encode(
                            alt.Color(temp),
                            alt.Tooltip([temp])
                        ).properties(
                            title = title
                        ).resolve_scale(theta="independent", color="independent")
                
                elif len(colorList) > 1 :
                    color_chart = []
                    for i in range(1,len(colorList)):
                        temp = colorList[j]
                        title = temp
                        # Check item is Measure
                        if temp in measure_Color.keys(): 
                            title = f"{measure_Color[temp]} of {temp}"
                            temp = f"{measure_Color[temp]}({temp}):Q"

                        color_chart.append(alt.Chart(data).mark_arc().encode(
                            *temp_chart_pie, alt.Color(temp),
                            alt.Tooltip([*temp_tooltip_pie, temp])
                        ).properties(
                            title = title
                        ))
                    piechart = alt.vconcat(*color_chart).resolve_scale(theta="independent", color="independent")

            else : 
                if (len(item_Theta)==1) and (len(item_Color)==1) :
                    temp_theta = thetaList[0]
                    titleTheta = temp_theta
                    temp_color = colorList[0]
                    titleColor = temp_color
                    # Check theta is Measure
                    if temp_theta in measure_Theta.keys(): 
                        titleTheta = f"{measure_Theta[temp_theta]} of {temp_theta}"
                        temp_theta = f"{measure_Theta[temp_theta]}({temp_theta}):Q"
                    # Check color is Measure
                    if temp_color in measure_Color.keys(): 
                        titleColor = f"{measure_Color[temp_color]} of {temp_color}"
                        temp_color = f"{measure_Color[temp_color]}({temp_color}):Q" 

                    piechart = alt.Chart(data).mark_arc().encode(
                            alt.Theta(temp_theta),
                            alt.Color(temp_color),
                            alt.Tooltip([temp_theta, temp_color])
                        ).properties(
                            title = titleTheta + " and " + titleColor
                        ).resolve_scale(theta="independent", color="independent")

                elif (len(item_Theta)>=1) and (len(item_Color)>=1):
                    if (len(item_Theta)==1) and (len(item_Color)>=1):
                        temp_theta = thetaList[0]
                        titleTheta = temp_theta
                        # Check item is Measure
                        if temp_theta in measure_Theta.keys(): 
                            titleTheta = f"{measure_Theta[temp_theta]} of {temp_theta}"
                            temp_theta = f"{measure_Theta[temp_theta]}({temp_theta}):Q"

                        color_chart = []
                        for i in range(1,len(colorList)):
                            temp_color = colorList[i]
                            titleColor = temp_color
                            # Check item is Measure
                            if temp_color in measure_Color.keys(): 
                                titleColor = f"{measure_Color[temp_color]} of {temp_color}"
                                temp_color = f"{measure_Color[temp_color]}({temp_color}):Q"
                            
                            color_chart.append(alt.Chart(data).mark_arc().encode(
                                *temp_chart_pie, 
                                alt.Color(temp_color), 
                                alt.Theta(temp_theta),
                                alt.Tooltip([*temp_tooltip_pie, temp_color, temp_theta])
                            ).properties(
                                title = titleTheta + " and " + titleColor
                            ).resolve_scale(theta="independent", color="independent"))
                        piechart = alt.vconcat(*color_chart).resolve_scale(theta="independent", color="independent")

                    elif (len(item_Theta)>=1) and (len(item_Color)==1) :
                        temp_color = colorList[0]
                        titleColor = temp_color
                        # Check item is Measure
                        if temp_color in measure_Color.keys(): 
                            titleColor = f"{measure_Color[temp_color]} of {temp_color}"
                            temp_color = f"{measure_Color[temp_color]}({temp_color}):Q"

                        theta_chart = []
                        for j in range(1,len(thetaList)):
                            temp_theta = thetaList[j]
                            titleTheta = temp_theta
                            # Check item is Measure
                            if temp_theta in measure_Theta.keys(): 
                                titleTheta = f"{measure_Theta[temp_theta]} of {temp_theta}"
                                temp_theta = f"{measure_Theta[temp_theta]}({temp_theta}):Q"

                            theta_chart.append(alt.Chart(data).mark_arc().encode(
                                *temp_chart_pie, 
                                alt.Color(temp_color), 
                                alt.Theta(temp_theta),
                                alt.Tooltip([*temp_tooltip_pie, temp_color, temp_theta])
                            ).properties(
                                title = titleTheta + " and " + titleColor
                            ).resolve_scale(theta="independent", color="independent"))
                        piechart = alt.hconcat(*theta_chart).resolve_scale(theta="independent", color="independent")

                    else:
                        for i in range(1,len(colorList)):
                            temp_color = colorList[i]
                            titleColor = temp_color

                            # Check color is Measure
                            if temp_color in measure_Color.keys(): 
                                titleColor = f"{measure_Color[temp_color]} of {temp_color}"
                                temp_color = f"{measure_Color[temp_color]}({temp_color}):Q"

                            theta_chart = []
                            for j in range(1,len(thetaList)):
                                temp_theta = thetaList[j]
                                titleTheta = temp_theta

                                # Check item is Measure
                                if temp_theta in measure_Theta.keys(): 
                                    titleTheta = f"{measure_Theta[temp_theta]} of {temp_theta}"
                                    temp_theta = f"{measure_Theta[temp_theta]}({temp_theta}):Q"

                                theta_chart.append(alt.Chart(data).mark_arc().encode(
                                    *temp_chart_pie,
                                    alt.Theta(temp_theta),
                                    alt.Color(temp_color),
                                    alt.Tooltip([*temp_tooltip_pie, temp_theta, temp_color]),
                                ).properties(
                                    title = titleTheta + " and " + titleColor
                                ).resolve_scale(theta="independent", color="independent"))
                                # print(theta_chart)

                            if len(theta_chart) >= 1:
                                theta_charts.append(alt.hconcat(*theta_chart).resolve_scale(theta="independent", color="independent"))
                        piechart = alt.vconcat(*theta_charts).resolve_scale(theta="independent", color="independent")

            self.ui.pieChart.updateChart(piechart)

        ########################################################################

        ########################################################################
        ## LINE CHART
        ########################################################################
        item_LineColumn, fil_LineColumn, measure_LineColumn = self.ui.ColumnList_line.get_plot_item()
        item_LineRow, fil_LineRow, measure_LineRow  = self.ui.RowList_line.get_plot_item()
        item_LineColumn, item_LineRow = self.check_dup(item_LineColumn, item_LineRow, self.i1, self.i2)
        data = None
        self.i1 = item_LineColumn
        self.i2 = item_LineRow
        test_line = []
        tooltip_line = []
        check_colrow = {'row':False, 'column':False, 'resolve_scale':True}

        min_line = 0
        max_line = 0

        if(len(item_LineColumn)>0 or len(item_LineRow)>0):
            data = self.dt.data_filter(item_LineColumn, item_LineRow , fil_LineColumn, fil_LineRow, measure_LineColumn, measure_LineRow)
           
            coll_Di_line = {'row':{'count':0, 'list':[]},'column':{'count':0, 'list':[]}}
            coll_Me_line = {'row':{'count':0, 'list':[]},'column':{'count':0, 'list':[]}}
            for i in item_LineColumn:
                if i in measure_LineColumn.keys() : 
                    coll_Me_line['column']['count'] += 1
                    coll_Me_line['column']['list'].append(i)
                else : 
                    coll_Di_line['column']['count'] += 1
                    coll_Di_line['column']['list'].append(i)
            for i in item_LineRow:
                if i in measure_LineRow.keys() : 
                    coll_Me_line['row']['count'] += 1
                    coll_Me_line['row']['list'].append(i)
                else : 
                    coll_Di_line['row']['count'] += 1
                    coll_Di_line['row']['list'].append(i)
            
            coll_Di_line['row']['list'].reverse()
            coll_Di_line['column']['list'].reverse()

            # print("coll_Di_bar['row']",coll_Di_bar['row']," \
            #     coll_Di_bar['column']",coll_Di_bar['column'])
            # print("coll_Me_bar['row']",coll_Me_bar['row']," \
            #     coll_Me_bar['column']",coll_Me_bar['column']) 

            # Check 1 Measure in ROW/COLUMN
            if coll_Me_line['column']['count'] == 1 : #todo: a Measure in column
                check_colrow['column'] = True   # have Measure in Column
                if coll_Di_line['row']['count'] == 1 :       # 1 dimension in row 
                    # check scale
                    if coll_Di_line['column']['count'] == 0 :    # dimension row 1 col 0
                        tempMax = data.groupby([coll_Di_line['row']['list'][0]], as_index=False)[coll_Me_line['column']['list'][0]].agg(measure_LineColumn[coll_Me_line['column']['list'][0]]).max()[1]
                        tempMin = data.groupby([coll_Di_line['row']['list'][0]], as_index=False)[coll_Me_line['column']['list'][0]].agg(measure_LineColumn[coll_Me_line['column']['list'][0]]).min()[1]
                        if max_line < int(tempMax) : max_line = int(tempMax)
                        if min_line > int(tempMin) : min_line = int(tempMin)
                    elif coll_Di_line['column']['count'] > 0 :   # dimension row 1 col > 0
                        tempMax = data.groupby([coll_Di_line['column']['list'][0], coll_Di_line['row']['list'][0]], as_index=False)[coll_Me_line['column']['list'][0]].agg(measure_LineColumn[coll_Me_line['column']['list'][0]]).max()[2]
                        tempMin = data.groupby([coll_Di_line['column']['list'][0], coll_Di_line['row']['list'][0]], as_index=False)[coll_Me_line['column']['list'][0]].agg(measure_LineColumn[coll_Me_line['column']['list'][0]]).min()[2]
                        if max_line < int(tempMax) : max_line = int(tempMax)
                        if min_line > int(tempMin) : min_line = int(tempMin)

                    # print(coll_Di_bar['row']['list'][0],' max_bar : ',max_bar,' min_bar : ',min_bar)

                    test_line.append(alt.X(f"{measure_LineColumn[coll_Me_line['column']['list'][0]]}({coll_Me_line['column']['list'][0]})",scale=alt.Scale(domain=(min_line, max_line),clamp=True )))

                elif coll_Di_line['row']['count'] >= 2 :     # 2 & 3 dimension in row
                    # check scale
                    if coll_Di_line['column']['count'] == 0 :    # # dimension row > 1 col 0
                        tempMax = data.groupby([coll_Di_line['row']['list'][0], coll_Di_line['row']['list'][1]], as_index=False)[coll_Me_line['column']['list'][0]].agg(measure_LineColumn[coll_Me_line['column']['list'][0]]).max()[2]
                        tempMin = data.groupby([coll_Di_line['row']['list'][0], coll_Di_line['row']['list'][1]], as_index=False)[coll_Me_line['column']['list'][0]].agg(measure_LineColumn[coll_Me_line['column']['list'][0]]).min()[2]
                        if max_line < int(tempMax) : max_line = int(tempMax)
                        if min_line > int(tempMin) : min_line = int(tempMin)

                    elif coll_Di_line['column']['count'] > 0 :  # # dimension row > 1 col > 0
                        tempMax = data.groupby([coll_Di_line['column']['list'][0], coll_Di_line['row']['list'][0], coll_Di_line['row']['list'][1]], as_index=False)[coll_Me_line['column']['list'][0]].agg(measure_LineColumn[coll_Me_line['column']['list'][0]]).max()[3]
                        tempMin = data.groupby([coll_Di_line['column']['list'][0], coll_Di_line['row']['list'][0], coll_Di_line['row']['list'][1]], as_index=False)[coll_Me_line['column']['list'][0]].agg(measure_LineColumn[coll_Me_line['column']['list'][0]]).min()[3]
                        if max_line < int(tempMax) : max_line = int(tempMax)
                        if min_line > int(tempMin) : min_line = int(tempMin)

                    test_line.append(alt.X(f"{measure_LineColumn[coll_Me_line['column']['list'][0]]}({coll_Me_line['column']['list'][0]})",scale=alt.Scale(domain=(min_line, max_line),clamp=True )))

                else :  # 0 dimension in row
                    test_line.append(alt.X(f"{measure_LineColumn[coll_Me_line['column']['list'][0]]}({coll_Me_line['column']['list'][0]})"))

                tooltip_line.append(f"{measure_LineColumn[coll_Me_line['column']['list'][0]]}({coll_Me_line['column']['list'][0]})")

            elif coll_Me_line['row']['count'] == 1 : #todo: a Measure in row
                check_colrow['row'] = True      # have Measure in Row
                if coll_Di_line['column']['count'] == 1 :    # 1 dimension in column
                    # check scale
                    if coll_Di_line['row']['count'] == 0 :   # dimension row 0 col 1
                        tempMax = data.groupby([coll_Di_line['column']['list'][0]], as_index=False)[coll_Me_line['row']['list'][0]].agg(measure_LineRow[coll_Me_line['row']['list'][0]]).max()[1]
                        tempMin = data.groupby([coll_Di_line['column']['list'][0]], as_index=False)[coll_Me_line['row']['list'][0]].agg(measure_LineRow[coll_Me_line['row']['list'][0]]).min()[1]
                        if max_line < int(tempMax) : max_line = int(tempMax)
                        if min_line > int(tempMin) : min_line = int(tempMin)

                    elif coll_Di_line['row']['count'] > 0 :    # dimension row > 0 col 1
                        tempMax = data.groupby([coll_Di_line['row']['list'][0], coll_Di_line['column']['list'][0]], as_index=False)[coll_Me_line['row']['list'][0]].agg(measure_LineRow[coll_Me_line['row']['list'][0]]).max()[2]
                        tempMin = data.groupby([coll_Di_line['row']['list'][0], coll_Di_line['column']['list'][0]], as_index=False)[coll_Me_line['row']['list'][0]].agg(measure_LineRow[coll_Me_line['row']['list'][0]]).min()[2]
                        if max_line < int(tempMax) : max_line = int(tempMax)
                        if min_line > int(tempMin) : min_line = int(tempMin)

                    test_line.append(alt.Y(f"{measure_LineRow[coll_Me_line['row']['list'][0]]}({coll_Me_line['row']['list'][0]})", scale=alt.Scale(domain=(min_line, max_line), clamp=True )))

                elif coll_Di_line['column']['count'] >= 2 : # 2 & 3 dimension in column
                    # check scale
                    if coll_Di_line['row']['count'] == 0 :   # dimension row 0 col > 1
                        tempMax = data.groupby([coll_Di_line['column']['list'][0], coll_Di_line['column']['list'][1]], as_index=False)[coll_Me_line['row']['list'][0]].agg(measure_LineRow[coll_Me_line['row']['list'][0]]).max()[2]
                        tempMin = data.groupby([coll_Di_line['column']['list'][0], coll_Di_line['column']['list'][1]], as_index=False)[coll_Me_line['row']['list'][0]].agg(measure_LineRow[coll_Me_line['row']['list'][0]]).min()[2]
                        if max_line < int(tempMax) : max_line = int(tempMax)
                        if min_line > int(tempMin) : min_line = int(tempMin)

                    elif coll_Di_line['row']['count'] > 0 :   # dimension row > 0 col > 1
                        tempMax = data.groupby([coll_Di_line['row']['list'][0], coll_Di_line['column']['list'][0], coll_Di_line['column']['list'][1]], as_index=False)[coll_Me_line['row']['list'][0]].agg(measure_LineRow[coll_Me_line['row']['list'][0]]).max()[3]
                        tempMin = data.groupby([coll_Di_line['row']['list'][0], coll_Di_line['column']['list'][0], coll_Di_line['column']['list'][1]], as_index=False)[coll_Me_line['row']['list'][0]].agg(measure_LineRow[coll_Me_line['row']['list'][0]]).min()[3]
                        if max_line < int(tempMax) : max_line = int(tempMax)
                        if min_line > int(tempMin) : min_line = int(tempMin)

                    test_line.append(alt.Y(f"{measure_LineRow[coll_Me_line['row']['list'][0]]}({coll_Me_line['row']['list'][0]})", scale=alt.Scale(domain=(min_line, max_line), clamp=True )))

                else :  # 0 dimension in column
                    test_line.append(alt.Y(f"{measure_LineRow[coll_Me_line['row']['list'][0]]}({coll_Me_line['row']['list'][0]})"))

                tooltip_line.append(f"{measure_LineRow[coll_Me_line['row']['list'][0]]}({coll_Me_line['row']['list'][0]})")

            ########################################################################
            ##todo dimension&measure in same ROW/COLUMN 
            # a Dimension Measure in column
            if (coll_Me_line['column']['count'] == 1) and (coll_Di_line['column']['count'] == 1) and (coll_Di_line['row']['count'] == 0):
                # check scale
                tempMax = data.groupby([coll_Di_line['column']['list'][0]], as_index=False)[coll_Me_line['column']['list'][0]].agg(measure_LineColumn[coll_Me_line['column']['list'][0]]).max()[1]
                tempMin = data.groupby([coll_Di_line['column']['list'][0]], as_index=False)[coll_Me_line['column']['list'][0]].agg(measure_LineColumn[coll_Me_line['column']['list'][0]]).min()[1]
                if max_line < int(tempMax) : max_line = int(tempMax)
                if min_line > int(tempMin) : min_line = int(tempMin)

                test_line, tooltip_line = [], []
                test_line.append(alt.X(f"{measure_LineColumn[coll_Me_line['column']['list'][0]]}({coll_Me_line['column']['list'][0]})", scale=alt.Scale(domain=(min_line, max_line), clamp=True )))
                tooltip_line.append(f"{measure_LineColumn[coll_Me_line['column']['list'][0]]}({coll_Me_line['column']['list'][0]})")
                test_line.append(alt.Column(coll_Di_line['column']['list'][0]))
                tooltip_line.append(coll_Di_line['column']['list'][0])
                

            # a Dimension Measure in row
            elif (coll_Me_line['row']['count'] == 1) and (coll_Di_line['column']['count'] == 0) and (coll_Di_line['row']['count'] == 1) :
                # check scale
                tempMax = data.groupby([coll_Di_line['row']['list'][0]], as_index=False)[coll_Me_line['row']['list'][0]].agg(measure_LineRow[coll_Me_line['row']['list'][0]]).max()[1]
                tempMin = data.groupby([coll_Di_line['row']['list'][0]], as_index=False)[coll_Me_line['row']['list'][0]].agg(measure_LineRow[coll_Me_line['row']['list'][0]]).min()[1]
                if max_line < int(tempMax) : max_line = int(tempMax)
                if min_line > int(tempMin) : min_line = int(tempMin)

                test_line, tooltip_line = [], []
                test_line.append(alt.Y(f"{measure_LineRow[coll_Me_line['row']['list'][0]]}({coll_Me_line['row']['list'][0]})", scale=alt.Scale(domain=(min_line, max_line), clamp=True )))
                tooltip_line.append(f"{measure_LineRow[coll_Me_line['row']['list'][0]]}({coll_Me_line['row']['list'][0]})")
                test_line.append(alt.Row(coll_Di_line['row']['list'][0]))
                tooltip_line.append(coll_Di_line['row']['list'][0])
            ########################################################################
            else :   
                # Part Dimension ROW
                if coll_Di_line['row']['count'] >= 1:
                    if check_colrow['row'] :
                        test_line.append(alt.Row(coll_Di_line['row']['list'][0]+':O'))
                        tooltip_line.append(coll_Di_line['row']['list'][0]+':O')
                        check_colrow['resolve_scale'] = False
                    else:
                        test_line.append(alt.Y(coll_Di_line['row']['list'][0]+':O'))
                        tooltip_line.append(coll_Di_line['row']['list'][0]+':O')
                if coll_Di_line['row']['count'] >= 2:
                    if check_colrow['row'] :
                        test_line.append(alt.Color(coll_Di_line['row']['list'][1]+':O'))
                        tooltip_line.append(coll_Di_line['row']['list'][1]+':O')
                    else:
                        test_line.append(alt.Row(coll_Di_line['row']['list'][1]+':O'))
                        tooltip_line.append(coll_Di_line['row']['list'][1]+':O')
                if coll_Di_line['row']['count'] >= 3:
                    if check_colrow['row'] :
                        pass    # Not do anything when it more than >3
                    else:
                        test_line.append(alt.Color(coll_Di_line['row']['list'][2]+':O'))
                        tooltip_line.append(coll_Di_line['row']['list'][2]+':O')
                # Part Dimension COLUMN
                if coll_Di_line['column']['count'] >= 1:
                    if check_colrow['column'] :
                        test_line.append(alt.Column(coll_Di_line['column']['list'][0]+':O'))
                        tooltip_line.append(coll_Di_line['column']['list'][0]+':O')
                        check_colrow['resolve_scale'] = False
                    else:
                        test_line.append(alt.X(coll_Di_line['column']['list'][0]+':O'))
                        tooltip_line.append(coll_Di_line['column']['list'][0]+':O')
                if coll_Di_line['column']['count'] >= 2:
                    if check_colrow['column'] :
                        test_line.append(alt.Color(coll_Di_line['column']['list'][1]+':O'))
                        tooltip_line.append(coll_Di_line['column']['list'][1]+':O')
                    else:
                        test_line.append(alt.Column(coll_Di_line['column']['list'][1]+':O'))
                        tooltip_line.append(coll_Di_line['column']['list'][1]+':O')
                if coll_Di_line['column']['count'] >= 3:
                    if check_colrow['column'] :
                        pass    # Not do anything when it more than >3
                    else:
                        test_line.append(alt.Color(coll_Di_line['column']['list'][2]+':O'))
                        tooltip_line.append(coll_Di_line['column']['list'][2]+':O')
            
        ########################################################################
            '''Create Line Chart'''    
            # measure >1
            if (coll_Me_line['row']['count'] > 1) or (coll_Me_line['column']['count'] > 1) : 
                line_charts = []
                if  coll_Me_line['row']['count'] > 1 :   # Measure row 
                    for i in range(coll_Me_line['row']['count']):
                        # edit tooltip
                        temp_tooltip = tooltip_line.copy()
                        temp_tooltip.append(f"{measure_LineRow[coll_Me_line['row']['list'][i]]}({coll_Me_line['row']['list'][i]})")
                        temp_test_line = test_line.copy()
                        min_line, max_line= 0, 0
                        
                        if coll_Di_line['column']['count'] == 1 :       # 1 dimension
                            # check scale
                            tempMax = data.groupby([coll_Di_line['column']['list'][0]], as_index=False)[coll_Me_line['row']['list'][i]].agg(measure_LineRow[coll_Me_line['row']['list'][i]]).max()[1]
                            tempMin = data.groupby([coll_Di_line['column']['list'][0]], as_index=False)[coll_Me_line['row']['list'][i]].agg(measure_LineRow[coll_Me_line['row']['list'][i]]).min()[1]
                            if max_line < int(tempMax) : max_line = int(tempMax)
                            if min_line > int(tempMin) : min_line = int(tempMin)

                            temp_test_line.append(alt.Y(f"{measure_LineRow[coll_Me_line['row']['list'][i]]}({coll_Me_line['row']['list'][i]})",scale=alt.Scale(domain=(min_line, max_line),clamp=True )))
                        
                        elif coll_Di_line['column']['count'] >= 2 :      # 2 & 3 dimension
                            # check scale
                            tempMax = data.groupby([coll_Di_line['column']['list'][0], coll_Di_line['column']['list'][1]], as_index=False)[coll_Me_line['row']['list'][i]].agg(measure_LineRow[coll_Me_line['row']['list'][i]]).max()[2]
                            tempMin = data.groupby([coll_Di_line['column']['list'][0], coll_Di_line['column']['list'][1]], as_index=False)[coll_Me_line['row']['list'][i]].agg(measure_LineRow[coll_Me_line['row']['list'][i]]).min()[2]
                            if max_line < int(tempMax) : max_line = int(tempMax)
                            if min_line > int(tempMin) : min_line = int(tempMin)

                            temp_test_line.append(alt.Y(f"{measure_LineRow[coll_Me_line['row']['list'][i]]}({coll_Me_line['row']['list'][i]})",scale=alt.Scale(domain=(min_line, max_line),clamp=True )))

                        else :      # 0 dimension
                            temp_test_line.append(alt.Y(f"{measure_LineRow[coll_Me_line['row']['list'][i]]}({coll_Me_line['row']['list'][i]})"))
                        
                        # print(temp_test_line)
                        line_charts.append(alt.Chart(data).mark_line().encode(*temp_test_line,alt.Tooltip(temp_tooltip))
                        .resolve_scale(
                            x='independent',
                            y='independent'
                        ))

                    linechart = alt.vconcat(*line_charts)

                elif coll_Me_line['column']['count'] > 1 :   # Measure column 
                    for i in range(coll_Me_line['column']['count']):
                        # edit tooltip
                        temp_tooltip = tooltip_line.copy()
                        temp_tooltip.append(f"{measure_LineColumn[coll_Me_line['column']['list'][i]]}({coll_Me_line['column']['list'][i]})")
                        temp_test_line = test_line.copy()
                        
                        min_line, max_line= 0, 0
                        if coll_Di_line['row']['count'] == 1 :       # 1 dimension
                            # check scale
                            tempMax = data.groupby([coll_Di_line['row']['list'][0]], as_index=False)[coll_Me_line['column']['list'][i]].agg(measure_LineColumn[coll_Me_line['column']['list'][i]]).max()[1]
                            tempMin = data.groupby([coll_Di_line['row']['list'][0]], as_index=False)[coll_Me_line['column']['list'][i]].agg(measure_LineColumn[coll_Me_line['column']['list'][i]]).min()[1]
                            if max_line < int(tempMax) : max_line = int(tempMax)
                            if min_line > int(tempMin) : min_line = int(tempMin)

                            temp_test_line.append(alt.X(f"{measure_LineColumn[coll_Me_line['column']['list'][i]]}({coll_Me_line['column']['list'][i]})",scale=alt.Scale(domain=(min_line, max_line),clamp=True )))
                        
                        elif coll_Di_line['row']['count'] >= 2 :     # 2 & 3 dimension
                            # check scale
                            tempMax = data.groupby([coll_Di_line['row']['list'][0], coll_Di_line['row']['list'][1]], as_index=False)[coll_Me_line['column']['list'][i]].sum().max()[2]
                            tempMin = data.groupby([coll_Di_line['row']['list'][0], coll_Di_line['row']['list'][1]], as_index=False)[coll_Me_line['column']['list'][i]].sum().min()[2]
                            if max_line < int(tempMax) : max_line = int(tempMax)
                            if min_line > int(tempMin) : min_line = int(tempMin)

                            temp_test_line.append(alt.X(f"{measure_LineColumn[coll_Me_line['column']['list'][i]]}({coll_Me_line['column']['list'][i]})",scale=alt.Scale(domain=(min_line, max_line),clamp=True )))

                        else :      # 0 dimension
                            temp_test_line.append(alt.X(f"{measure_LineColumn[coll_Me_line['column']['list'][i]]}({coll_Me_line['column']['list'][i]})"))
                    
                        line_charts.append(alt.Chart(data).mark_line().encode(*temp_test_line,alt.Tooltip(temp_tooltip)).resolve_scale( x='independent', y='independent' ))

                    linechart = alt.concat(*line_charts)

            # measure =1
            else : 
                # Create Line Chart        
                test_line.append(alt.Tooltip(tooltip_line))
                if  check_colrow['resolve_scale'] :
                    linechart = alt.Chart(data).mark_line().encode(*test_line).resolve_scale(x='independent', y='independent')
                else : linechart = alt.Chart(data).mark_line().encode(*test_line)
            # Set chart
            self.ui.lineChart.updateChart(linechart)

            # Set chart
            self.ui.lineChart.updateChart(linechart)
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
