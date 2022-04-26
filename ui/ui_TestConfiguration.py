# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TestConfiguration.ui'
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
        MainWindow.resize(823, 632)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_4 = QAction(MainWindow)
        self.action_4.setObjectName(u"action_4")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_3.addWidget(self.radioButton_2)

        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout_3.addWidget(self.radioButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.checkBox_4 = QCheckBox(self.centralwidget)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.gridLayout_3.addWidget(self.checkBox_4, 1, 1, 1, 1)

        self.checkBox_2 = QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout_3.addWidget(self.checkBox_2, 0, 1, 1, 1)

        self.checkBox_6 = QCheckBox(self.centralwidget)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.gridLayout_3.addWidget(self.checkBox_6, 2, 1, 1, 1)

        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_3.addWidget(self.checkBox, 0, 0, 1, 1)

        self.checkBox_5 = QCheckBox(self.centralwidget)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.gridLayout_3.addWidget(self.checkBox_5, 2, 0, 1, 1)

        self.checkBox_8 = QCheckBox(self.centralwidget)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.gridLayout_3.addWidget(self.checkBox_8, 3, 1, 1, 1)

        self.checkBox_7 = QCheckBox(self.centralwidget)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.gridLayout_3.addWidget(self.checkBox_7, 3, 0, 1, 1)

        self.checkBox_3 = QCheckBox(self.centralwidget)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout_3.addWidget(self.checkBox_3, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.Back = QPushButton(self.centralwidget)
        self.Back.setObjectName(u"Back")

        self.horizontalLayout_4.addWidget(self.Back)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.Begin = QPushButton(self.centralwidget)
        self.Begin.setObjectName(u"Begin")

        self.horizontalLayout_4.addWidget(self.Begin)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 823, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addSeparator()
        self.menu.addAction(self.action_4)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c \u0437\u0430\u043d\u043e\u0432\u043e", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0438\u0442\u044c \u0442\u0435\u0441\u0442", None))
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u0442\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0430\u043c\u043e\u043a\u043e\u043d\u0442\u0440\u043e\u043b\u044c", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0442\u0440\u043e\u043b\u044c \u0417\u043d\u0430\u043d\u0438\u0439", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"1:100000", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"1:25000", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"1:300000", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"1:10000", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"1:200000", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"1:1000000", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"1:500000", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"1:50000", None))
        self.Back.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.Begin.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c \u0442\u0435\u0441\u0442", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
    # retranslateUi

