# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'popup.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_popupWindow(object):
    def setupUi(self, popupWindow):
        popupWindow.setObjectName("popupWindow")
        popupWindow.resize(442, 370)
        self.centralwidget = QtWidgets.QWidget(popupWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 2, 0, 1, 4)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)
        self.selectButton = QtWidgets.QPushButton(self.centralwidget)
        self.selectButton.setObjectName("selectButton")
        self.gridLayout.addWidget(self.selectButton, 1, 0, 1, 1)
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setObjectName("clearButton")
        self.gridLayout.addWidget(self.clearButton, 1, 3, 1, 1)
        self.searchEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.searchEdit.setObjectName("searchEdit")
        self.gridLayout.addWidget(self.searchEdit, 1, 1, 1, 2)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 2, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 2)
        popupWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(popupWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 442, 26))
        self.menubar.setObjectName("menubar")
        popupWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(popupWindow)
        self.statusbar.setObjectName("statusbar")
        popupWindow.setStatusBar(self.statusbar)

        self.retranslateUi(popupWindow)
        QtCore.QMetaObject.connectSlotsByName(popupWindow)

    def retranslateUi(self, popupWindow):
        _translate = QtCore.QCoreApplication.translate
        popupWindow.setWindowTitle(_translate("popupWindow", "MainWindow"))
        self.label.setText(_translate("popupWindow", "TextLabel"))
        self.selectButton.setText(_translate("popupWindow", "All Selection"))
        self.clearButton.setText(_translate("popupWindow", "All Clear"))
        self.pushButton_2.setText(_translate("popupWindow", "Cancel"))
        self.pushButton.setText(_translate("popupWindow", "Done"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    popupWindow = QtWidgets.QMainWindow()
    ui = Ui_popupWindow()
    ui.setupUi(popupWindow)
    popupWindow.show()
    sys.exit(app.exec_())
