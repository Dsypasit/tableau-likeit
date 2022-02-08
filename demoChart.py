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

        #######################################################################
        # ADD FUNCTION ELEMENT
        #######################################################################
        self.ui.menuImport.triggered.connect(self.open_file)
        self.ui.actionUnion.triggered.connect(self.union_file)
        self.ui.menuExit.triggered.connect(qApp.quit)

        self.ui.DimensionWidget.itemDoubleClicked.connect(self.to_measure)
        self.ui.MeasureWidget.itemDoubleClicked.connect(self.to_dimension)
        self.ui.MeasureList.itemChanged.connect(lambda: self.ui.tableWidget.make_table())
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
            self.dimension()

            #self.Graph()

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
        # Bar Chart
        item_BarColumn, fil_BarColumn, measure_BarColumn = self.ui.ColumnList_bar.get_plot_item()
        item_BarRow, fil_BarRow, measure_BarRow  = self.ui.RowList_bar.get_plot_item()
        data = None
        test_bar = []
        tooltip_bar = []
        if(len(item_BarColumn)>0 or len(item_BarRow)>0):
            data = self.dt.data_filter(item_BarColumn, item_BarRow , fil_BarColumn, fil_BarRow )
            # for i in item1:
            if(len(item_BarColumn)>=1):
                if item_BarColumn[0] in measure_BarColumn.keys():
                    test_bar.append(alt.X(f'{measure_BarColumn[item_BarColumn[0]]}({item_BarColumn[0]})'))
                    tooltip_bar.append(f'{measure_BarColumn[item_BarColumn[0]]}({item_BarColumn[0]})')
                else:
                    test_bar.append(alt.X(item_BarColumn[0]))
                    tooltip_bar.append(item_BarColumn[0])
            if(len(item_BarRow)>=1):
                if item_BarRow[0] in measure_BarRow.keys():
                    test_bar.append(alt.Y(f'{measure_BarRow[item_BarRow[0]]}({item_BarRow[0]})'))
                    tooltip_bar.append(f'{measure_BarRow[item_BarRow[0]]}({item_BarRow[0]})')
                else:
                    test_bar.append(alt.Y(item_BarRow[0]))
                    tooltip_bar.append(item_BarRow[0])
            if(len(item_BarColumn)>=2):
                if item_BarColumn[1] in measure_BarColumn.keys():
                    test_bar.append(alt.Column(f'{measure_BarColumn[item_BarColumn[1]]}({item_BarColumn[1]})'))
                    tooltip_bar.append(f'{measure_BarColumn[item_BarColumn[1]]}({item_BarColumn[1]})')
                else:
                    test_bar.append(alt.Column(item_BarColumn[1]))
                    tooltip_bar.append(item_BarColumn[1])
            if(len(item_BarRow)>=2):
                if item_BarRow[1] in measure_BarRow.keys():
                    test_bar.append(alt.Row(f'{measure_BarRow[item_BarRow[1]]}({item_BarRow[1]})'))
                    tooltip_bar.append(f'{measure_BarRow[item_BarRow[1]]}({item_BarRow[1]})')
                else:
                    test_bar.append(alt.Row(item_BarRow[1]))
                    tooltip_bar.append(item_BarRow[1])
            if(len(item_BarColumn)>=3):
                if item_BarColumn[2] in measure_BarColumn.keys():
                    test_bar.append(alt.Color(f'{measure_BarColumn[item_BarColumn[2]]}({item_BarColumn[2]})'))
                    tooltip_bar.append(f'{measure_BarColumn[item_BarColumn[2]]}({item_BarColumn[2]})')
                else:
                    test_bar.append(alt.Color(item_BarColumn[2]))
                    tooltip_bar.append(item_BarColumn[2])
            if(len(item_BarRow)>=3):
                if item_BarRow[2] in measure_BarRow.keys():
                    test_bar.append(alt.Color(f'{measure_BarRow[item_BarRow[2]]}({item_BarRow[2]})'))
                    tooltip_bar.append(f'{measure_BarRow[item_BarRow[2]]}({item_BarRow[2]})')
                else:
                    test_bar.append(alt.Color(item_BarRow[2]))
                    tooltip_bar.append(item_BarRow[2])
            test_bar.append(alt.Tooltip(tooltip_bar))
            # test =  (alt.X('Sub-Category'), alt.Y('Profit'))
            # test =  [ alt.X('Sub-Category'), alt.Y('Profit'), alt.Column('Category') ]
            print(test_bar)

            barchart = alt.Chart(data).mark_bar().encode(
                *test_bar
            ).resolve_scale(
                x='independent'
            )
            self.ui.barChart.updateChart(barchart)

        # Pie Chart
        item_Theta, fil_Theta, measure_Theta = self.ui.ThetaList.get_plot_item()
        item_Color, fil_Color, measure_Color  = self.ui.ColorList.get_plot_item()
        data = None
        test_pie = []
        tooltip_pie = []
        piechart = alt.Chart(self.dt.data).mark_arc().encode(
            theta="sum(Sales):Q",
            color="Sub-Category",
            tooltip=['sum(Sales)'],
        )
        #self.ui.pieChart.updateChart(piechart)

        # Line Chart
        item_LineColumn, fil_LineColumn, measure_LineColumn = self.ui.ColumnList_line.get_plot_item()
        item_LineRow, fil_LineRow, measure_LineRow  = self.ui.RowList_line.get_plot_item()
        data = None
        test_line = []
        tooltip_line = []
        if(len(item_LineColumn)>0 or len(item_LineRow)>0):
            data = self.dt.data_filter(item_LineColumn, item_LineRow , fil_LineColumn, fil_LineRow )
            # for i in item1:
            if(len(item_LineColumn)>=1):
                if item_LineColumn[0] in measure_LineColumn.keys():
                    test_line.append(alt.X(f'{measure_LineColumn[item_LineColumn[0]]}({item_LineColumn[0]})'))
                    tooltip_line.append(f'{measure_LineColumn[item_LineColumn[0]]}({item_LineColumn[0]})')
                else:
                    test_line.append(alt.X(item_LineColumn[0]))
                    tooltip_line.append(item_LineColumn[0])
            if(len(item_LineRow)>=1):
                if item_LineRow[0] in measure_LineRow.keys():
                    test_line.append(alt.Y(f'{measure_LineRow[item_LineRow[0]]}({item_LineRow[0]})'))
                    tooltip_line.append(f'{measure_LineRow[item_LineRow[0]]}({item_LineRow[0]})')
                else:
                    test_line.append(alt.Y(item_LineRow[0]))
                    tooltip_line.append(item_LineRow[0])
            if(len(item_LineColumn)>=2):
                if item_LineColumn[1] in measure_LineColumn.keys():
                    test_line.append(alt.Column(f'{measure_LineColumn[item_LineColumn[1]]}({item_BarColumn[1]})'))
                    tooltip_line.append(f'{measure_LineColumn[item_LineColumn[1]]}({item_LineColumn[1]})')
                else:
                    test_line.append(alt.Column(item_LineColumn[1]))
                    tooltip_line.append(item_LineColumn[1])
            if(len(item_LineRow)>=2):
                if item_LineRow[1] in measure_LineRow.keys():
                    test_line.append(alt.Row(f'{measure_LineRow[item_LineRow[1]]}({item_LineRow[1]})'))
                    tooltip_line.append(f'{measure_LineRow[item_LineRow[1]]}({item_LineRow[1]})')
                else:
                    test_line.append(alt.Row(item_LineRow[1]))
                    tooltip_line.append(item_LineRow[1])
            if(len(item_LineColumn)>=3):
                if item_LineColumn[2] in measure_LineColumn.keys():
                    test_line.append(alt.Color(f'{measure_LineColumn[item_LineColumn[2]]}({item_LineColumn[2]})'))
                    tooltip_line.append(f'{measure_LineColumn[item_LineColumn[2]]}({item_LineColumn[2]})')
                else:
                    test_line.append(alt.Color(item_LineColumn[2]))
                    tooltip_line.append(item_LineColumn[2])
            if(len(item_LineRow)>=3):
                if item_LineRow[2] in measure_LineRow.keys():
                    test_line.append(alt.Color(f'{measure_LineRow[item_LineRow[2]]}({item_LineRow[2]})'))
                    tooltip_line.append(f'{measure_LineRow[item_LineRow[2]]}({item_LineRow[2]})')
                else:
                    test_line.append(alt.Color(item_LineRow[2]))
                    tooltip_line.append(item_LineRow[2])
            test_line.append(alt.Tooltip(tooltip_line))
            # test =  (alt.X('Sub-Category'), alt.Y('Profit'))
            # test =  [ alt.X('Sub-Category'), alt.Y('Profit'), alt.Column('Category') ]
            print(test_line)

        linechart = alt.Chart(self.dt.data).mark_line(point=True).encode(
            *test_line
        ).resolve_scale(
            x='independent'
        )

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
