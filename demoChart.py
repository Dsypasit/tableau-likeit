########################################################################
## CONVERT .UI & .QRC
# pyrcc5 resources.qrc -o resource_rc.py
# pyuic5 -x ui_interface.ui -o ui_interface.py 
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
        self.i1 = None
        self.i2 = None

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
            self.dt.separated_dimension_measure()
            self.dimension()

            self.Graph()

    def make_table(self):
        self.header = self.dt.get_column()
        self.data = self.dt.get_data()
        self.ui.tableWidget.setColumnCount(len(self.header))
        self.ui.tableWidget.setRowCount(len(self.data))
        self.ui.tableWidget.setHorizontalHeaderLabels(self.header)
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

    def check_dup(self, i1, i2):
        it1 = i1
        it2 = i2
        if self.i1 == i1 and self.i2 != i2:
            for i in i1:
                if i in i2:
                    it1.remove(i)
        elif self.i2 == i2 and self.i1 != i1:
            for i in i2:
                if i in i1:
                    it2.remove(i)
        return it1, it2

    def Graph(self):
        item1, fil1, measure1 = self.ui.DimensionList_2.get_plot_item()
        item2, fil2, measure2 = self.ui.MeasureList_2.get_plot_item()
        item1, item2 = self.check_dup(item1, item2)
        data = None
        print(item1, item2)
        self.i1 = item1
        self.i2 = item2
        test = []
        tooltip = []
        if(len(item1)>0 or len(item2)>0):
            data = self.dt.data_filter(item1, item2, fil1, fil2)
            # for i in item1:
        
            if(len(item1)>=1):
                if item1[0] in measure1.keys():
                    test.append(alt.X(f'{measure1[item1[0]]}({item1[0]})'))
                    tooltip.append(f'{measure1[item1[0]]}({item1[0]})')
                else:
                    test.append(alt.X(item1[0]))
                    tooltip.append(item1[0])
            if(len(item2)>=1):
                if item2[0] in measure2.keys():
                    test.append(alt.Y(f'{measure2[item2[0]]}({item2[0]})'))
                    tooltip.append(f'{measure2[item2[0]]}({item2[0]})')
                else:
                    test.append(alt.Y(item2[0]))
                    tooltip.append(item2[0])
            if(len(item1)>=2):
                if item1[1] in measure1.keys():
                    test.append(alt.Column(f'{measure1[item1[1]]}({item1[1]})'))
                    tooltip.append(f'{measure1[item1[1]]}({item1[1]})')
                else:
                    test.append(alt.Column(item1[1]))
                    tooltip.append(item1[1])
            if(len(item2)>=2):
                if item2[1] in measure2.keys():
                    test.append(alt.Row(f'{measure2[item2[1]]}({item2[1]})'))
                    tooltip.append(f'{measure2[item2[1]]}({item2[1]})')
                else:
                    test.append(alt.Row(item2[1]))
                    tooltip.append(item2[1])
            if(len(item1)>=3):
                if item1[2] in measure1.keys():
                    test.append(alt.Color(f'{measure1[item1[2]]}({item1[2]})'))
                    tooltip.append(f'{measure1[item1[2]]}({item1[2]})')
                else:
                    test.append(alt.Color(item1[2]))
                    tooltip.append(item1[2])
            if(len(item2)>=3):
                if item2[2] in measure2.keys():
                    test.append(alt.Color(f'{measure2[item2[2]]}({item2[2]})'))
                    tooltip.append(f'{measure2[item2[2]]}({item2[2]})')
                else:
                    test.append(alt.Color(item2[2]))
                    tooltip.append(item2[2])
            test.append(alt.Tooltip(tooltip))
            # test =  (alt.X('Sub-Category'), alt.Y('Profit'))
            # test =  [ alt.X('Sub-Category'), alt.Y('Profit'), alt.Column('Category') ]


            barchart = alt.Chart(data).mark_bar().encode(
                *test
            ).resolve_scale(
            x='independent'
            )
            self.ui.barChart.updateChart(barchart)

        piechart = alt.Chart(self.dt.data).mark_arc().encode(
            theta="sum(Sales):Q",
            color="Sub-Category",
            tooltip=['sum(Sales)'],
        )

        linechart = alt.Chart(self.dt.data).mark_line().encode(
            y = alt.Y('sum(Profit)'),
            x = alt.X('Sub-Category', title=None),
            column = ('Category'),
            tooltip=['sum(Profit)'],
        ).resolve_scale(
        x='independent'
        )

        self.ui.pieChart.updateChart(piechart)
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
