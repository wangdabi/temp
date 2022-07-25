# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(593, 330)
        MainWindow.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.title = QLineEdit(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(10, 10, 411, 31))
        self.content = QTextEdit(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setGeometry(QRect(10, 60, 411, 131))
        self.choice = QLineEdit(self.centralwidget)
        self.choice.setObjectName(u"choice")
        self.choice.setGeometry(QRect(10, 210, 401, 31))
        self.right = QLineEdit(self.centralwidget)
        self.right.setObjectName(u"right")
        self.right.setGeometry(QRect(10, 250, 113, 31))
        self.append = QPushButton(self.centralwidget)
        self.append.setObjectName(u"append")
        self.append.setGeometry(QRect(130, 290, 261, 31))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(440, 10, 91, 31))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(440, 110, 91, 31))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(420, 210, 151, 21))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(140, 250, 111, 31))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.right.setInputMask("")
        self.append.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u5230\u5217\u8868\uff08\u5475\u5475\uff09", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6848\u4ef6\u540d\u79f0", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6848\u4ef6\u5185\u5bb9", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u9009\u9879\uff08\u7528\u7a7a\u683c\u9694\u5f00\uff09", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u6b63\u786e\u9009\u9879", None))
    # retranslateUi

