from PyQt5 import QtCore, QtGui, QtWidgets
import pendulum
import datetime

class DateWidgetItem(QtWidgets.QTableWidgetItem):

    def __lt__(self, other):
        if isinstance(other, DateWidgetItem):
            date1_str = self.data(QtCore.Qt.EditRole).split('/')
            date2_str = other.data(QtCore.Qt.EditRole).split('/')
            # date1_str = self.data(QtCore.Qt.EditRole)
            # date2_str = other.data(QtCore.Qt.EditRole)
            # date1 = pendulum.from_format(date1_str, 'DD/MM/YYYY')
            # date2 = pendulum.from_format(date2_str, 'DD/MM/YYYY')
            date1 = datetime.datetime(int(date1_str[2]), int(date1_str[1]), int(date1_str[0]))
            date2 = datetime.datetime(int(date2_str[2]), int(date2_str[1]), int(date2_str[0]))
        return (date1 < date2)
    