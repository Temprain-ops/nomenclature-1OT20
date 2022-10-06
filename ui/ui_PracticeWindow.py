# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PracticeWindow.ui'
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
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.MapTable = QTableWidget(self.centralwidget)
        if (self.MapTable.columnCount() < 3):
            self.MapTable.setColumnCount(3)
        if (self.MapTable.rowCount() < 3):
            self.MapTable.setRowCount(3)
        self.MapTable.setObjectName(u"MapTable")
        sizePolicy.setHeightForWidth(self.MapTable.sizePolicy().hasHeightForWidth())
        self.MapTable.setSizePolicy(sizePolicy)
        self.MapTable.setMinimumSize(QSize(780, 505))
        self.MapTable.setMaximumSize(QSize(780, 505))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.MapTable.setFont(font)
        self.MapTable.setSelectionMode(QAbstractItemView.NoSelection)
        self.MapTable.setRowCount(3)
        self.MapTable.setColumnCount(3)
        self.MapTable.horizontalHeader().setVisible(False)
        self.MapTable.horizontalHeader().setMinimumSectionSize(259)
        self.MapTable.horizontalHeader().setDefaultSectionSize(259)
        self.MapTable.verticalHeader().setVisible(False)
        self.MapTable.verticalHeader().setMinimumSectionSize(163)
        self.MapTable.verticalHeader().setDefaultSectionSize(167)

        self.verticalLayout.addWidget(self.MapTable)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setObjectName(u"backButton")

        self.horizontalLayout.addWidget(self.backButton)

        self.clearButton = QPushButton(self.centralwidget)
        self.clearButton.setObjectName(u"clearButton")
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(False)
        self.clearButton.setFont(font1)

        self.horizontalLayout.addWidget(self.clearButton)

        self.generateButton = QPushButton(self.centralwidget)
        self.generateButton.setObjectName(u"generateButton")

        self.horizontalLayout.addWidget(self.generateButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.backButton.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u043c\u0435\u043d\u044e", None))
        self.clearButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.generateButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
    # retranslateUi

