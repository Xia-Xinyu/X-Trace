# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'charts_represent.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Charts_Represent(object):
    def setupUi(self, Charts_Represent):
        Charts_Represent.setObjectName("Charts_Represent")
        Charts_Represent.resize(926, 589)
        self.centralwidget = QtWidgets.QWidget(Charts_Represent)
        self.centralwidget.setObjectName("centralwidget")
        Charts_Represent.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Charts_Represent)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 926, 26))
        self.menubar.setObjectName("menubar")
        Charts_Represent.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Charts_Represent)
        self.statusbar.setObjectName("statusbar")
        Charts_Represent.setStatusBar(self.statusbar)

        self.retranslateUi(Charts_Represent)
        QtCore.QMetaObject.connectSlotsByName(Charts_Represent)

    def retranslateUi(self, Charts_Represent):
        _translate = QtCore.QCoreApplication.translate
        Charts_Represent.setWindowTitle(_translate("Charts_Represent", "行人流量曲线"))
