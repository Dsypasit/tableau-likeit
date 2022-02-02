
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
import sys
from PyQt5.QtGui import QIcon, QPen
from PyQt5.QtChart import QChart, QChartView, QPieSeries
from PyQt5.QtCore import Qt
 
 
 
class Window(QWidget):
    def __init__(self):
        super().__init__()
 
        # window requirements
        self.setGeometry(200,200,600,400)
        self.setWindowTitle("Creating PieChart")
        self.setWindowIcon(QIcon("python.png"))
 
        # change the color of the window
        self.setStyleSheet('background-color:red')
 
        #create pieseries
        series  = QPieSeries()
 
        #append some data to the series 
        series.append("Apple", 80)
        series.append("Banana", 70)
        series.append("Pear", 50)
        series.append("Melon", 80)
        series.append("Water Melon", 30)
 
        #slice
        my_slice = series.slices()[3]
        my_slice.setExploded(True)
        my_slice.setLabelVisible(True)
        my_slice.setPen(QPen(Qt.green, 4))
        my_slice.setBrush(Qt.green)
 
 
 
        #create QChart object
        chart = QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Fruits Pie Chart")
        chart.setTheme(QChart.ChartThemeDark)
 
        # create QChartView object and add chart in thier 
        chartview = QChartView(chart)
 
 
        vbox = QVBoxLayout()
        vbox.addWidget(chartview)
 
        self.setLayout(vbox)
 
 
 
App = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(App.exec())