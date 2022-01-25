from PyQt5 import QtCore, QtGui, QtWidgets
import pendulum

class DateWidgetItem(QtGui.QTableWidgetItem):

    def __lt__(self, other):
        if isinstance(other, DateWidgetItem):
            date1_str = self.data(QtCore.Qt.UserRole).toString()
            date2_str = other.data(QtCore.Qt.UserRole).toString()
            date1 = pendulum.from_format(date1_str, 'DD/MM/YYYY')
            date2 = pendulum.from_format(date2_str, 'DD/MM/YYYY')
        return (date1 < date2)