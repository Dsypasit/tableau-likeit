
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtChart import QChart, QChartView, QLineSeries
from PyQt5.QtCore import QPointF
 
class Window(QWidget):
    def __init__(self):
        super().__init__()
 
 
        self.setGeometry(200,200,600,400)
        self.setWindowTitle("Creating LineChart")
        self.setWindowIcon(QIcon("python.png"))
 
        series = QLineSeries()
 
        series.append(0,6)
        series.append(3,5)
        series.append(3,8)
        series.append(7,3)
        series.append(12,7)
 
        series << QPointF(11,1) << QPointF(13,3)\
        << QPointF(17,6) << QPointF(18,3) << QPointF(20,20)
 
 
        chart = QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Line Chart Example")
        chart.setTheme(QChart.ChartThemeBlueCerulean)
 
 
        chartview = QChartView(chart)
 
        vbox = QVBoxLayout()
        vbox.addWidget(chartview)
        self.setLayout(vbox)
 
 
 
App = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(App.exec())