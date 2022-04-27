# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TestProgress.ui'
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
        __qtablewidgetitem = QTableWidgetItem()
        self.MapTable.setItem(0, 0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.MapTable.setItem(0, 1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.MapTable.setItem(0, 2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.MapTable.setItem(1, 0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.MapTable.setItem(1, 1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.MapTable.setItem(1, 2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.MapTable.setItem(2, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.MapTable.setItem(2, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.MapTable.setItem(2, 2, __qtablewidgetitem8)
        self.MapTable.setObjectName(u"MapTable")
        sizePolicy.setHeightForWidth(self.MapTable.sizePolicy().hasHeightForWidth())
        self.MapTable.setSizePolicy(sizePolicy)
        self.MapTable.setMinimumSize(QSize(780, 505))
        self.MapTable.setMaximumSize(QSize(780, 505))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.MapTable.setFont(font)
        self.MapTable.setLayoutDirection(Qt.LeftToRight)
        self.MapTable.setTextElideMode(Qt.ElideLeft)
        self.MapTable.setRowCount(3)
        self.MapTable.setColumnCount(3)
        self.MapTable.horizontalHeader().setVisible(False)
        self.MapTable.horizontalHeader().setMinimumSectionSize(259)
        self.MapTable.horizontalHeader().setDefaultSectionSize(259)
        self.MapTable.verticalHeader().setVisible(False)
        self.MapTable.verticalHeader().setMinimumSectionSize(163)
        self.MapTable.verticalHeader().setDefaultSectionSize(167)

        self.verticalLayout.addWidget(self.MapTable)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.BackButton = QPushButton(self.centralwidget)
        self.BackButton.setObjectName(u"BackButton")

        self.horizontalLayout_3.addWidget(self.BackButton)

        self.CheckButton = QPushButton(self.centralwidget)
        self.CheckButton.setObjectName(u"CheckButton")

        self.horizontalLayout_3.addWidget(self.CheckButton)

        self.NextButton = QPushButton(self.centralwidget)
        self.NextButton.setObjectName(u"NextButton")

        self.horizontalLayout_3.addWidget(self.NextButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


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

        __sortingEnabled = self.MapTable.isSortingEnabled()
        self.MapTable.setSortingEnabled(False)
        self.MapTable.setSortingEnabled(__sortingEnabled)

        self.BackButton.setText(QCoreApplication.translate("MainWindow", u"\u041a \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430\u043c", None))
        self.CheckButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u043a\u0430", None))
        self.NextButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u0439", None))
    # retranslateUi

