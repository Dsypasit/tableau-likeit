
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtChart import QChart, QChartView, QPieSeries
 
class Window(QWidget):
    def __init__(self):
        super().__init__()
 
 
        self.setGeometry(200,200,600,400)
        self.setWindowTitle("Creating Donut Chart")
        self.setWindowIcon(QIcon("python.png"))
 
        series = QPieSeries()
        series.setHoleSize(0.40)
 
        series.append("Protein 4,3%", 4.3)
 
        my_slice = series.append("Fat 15.6%", 15.6)
        my_slice.setExploded(True)
        my_slice.setLabelVisible(True)
 
        series.append("Other 30%", 30)
        series.append("Carbs 57%", 57)
 
 
        chart = QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Dount Chart")
        chart.setTheme(QChart.ChartThemeBlueCerulean)
 
        chartview = QChartView(chart)
 
        vbox = QVBoxLayout()
        vbox.addWidget(chartview)
 
        self.setLayout(vbox)
 
 
 
 
App = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(App.exec())