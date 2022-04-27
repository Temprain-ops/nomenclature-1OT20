# This Python file uses the following encoding: utf-8
import os
import sys
from PySide2 import QtGui
from PySide2.QtWidgets import QApplication, QWidget, QMainWindow, QAbstractItemDelegate, QTableWidgetItem
from PySide2.QtCore import QFile, QIODevice
from PySide2.QtUiTools import QUiLoader
import ui.ui_mainwindow
import ui.ui_TestConfiguration
import ui.ui_TestProgress
import gerenerate_nomenclature.generator as gen
from nomenclatures import get_nomenclatures
from PyQt5 import QtCore, QtWidgets


class TestProgressWindow(QMainWindow):
    def __init__(self, TestConfigurationWindow, MainWindow):
        super(TestProgressWindow, self).__init__()
        self.ui = ui.ui_TestProgress.Ui_MainWindow()
        self.ui.setupUi(self)
        self.initialize_links(MainWindow, TestConfigurationWindow)
        self.initialize_table()
        self.set_signals()

    def initialize_links(self, MainWindow, TestConfigurationWindow):
        self.mw = MainWindow
        self.tcw = TestConfigurationWindow
        print("TPW init")

    def initialize_table(self):
        for i in range(3):
            for j in range(3):
                self.ui.MapTable.item(i, j).setTextAlignment(QtCore.Qt.AlignCenter)
#        self.ui.MapTable.item(0, 0).setBackground(QtGui.QBrush(QtGui.QColor(128, 0, 0)))

    def clear_table(self):
        for i in range(3):
            for j in range(3):
                self.ui.MapTable.setItem(i, j, QTableWidgetItem(""))

    def set_signals(self):
        self.ui.BackButton.clicked.connect(self.backButtonClicked)
        self.ui.NextButton.clicked.connect(self.nextButtonClicked)

    def toggle_test_configuration_window(self):
        self.tcw.toggle_progress_window()

    def setup_test_config(self, number_of_testcases, control, ten, quarter, half_hundred, hundred, two_hundred, half_million, million):
        self.number_of_testcases = number_of_testcases
        self.control = control
        self.ten = ten
        self.quarter = quarter
        self.half_hundred = half_hundred
        self.hundred = hundred
        self.two_hundred = two_hundred
        self.half_million = half_million
        self.million = million
        self.testcases = []
        self.current_testcase = 0

    def generate_testcases(self):
        while len(self.testcases) < self.number_of_testcases:
            if self.ten:
                testcase = gen.get_ten()
                self.testcases.append(get_nomenclatures(testcase))
            if self.quarter:
                testcase = gen.get_quarter()
                self.testcases.append(get_nomenclatures(testcase))
            if self.half_hundred:
                testcase = gen.get_half_hundred()
                self.testcases.append(get_nomenclatures(testcase))
            if self.hundred:
                testcase = gen.get_hundred()
                self.testcases.append(get_nomenclatures(testcase))
            if self.two_hundred:
                testcase = gen.get_two_hundred()
                self.testcases.append(get_nomenclatures(testcase))
            if self.half_million:
                testcase = gen.get_half_million()
                self.testcases.append(get_nomenclatures(testcase))
            if self.million:
                testcase = gen.get_million()
                self.testcases.append(get_nomenclatures(testcase))

    def show_current_testcase(self):
        self.clear_table()
        self.ui.MapTable.setItem(1, 1, QTableWidgetItem(self.testcases[self.current_testcase][4]))
        self.initialize_table()

    def proceed_to_next_testcase(self):
        self.current_testcase += 1
        self.show_current_testcase()

    def proceed_to_prev_testcase(self):
        self.current_testcase -= 1
        self.show_current_testcase()

    def update_text(self):
        if self.current_testcase == self.number_of_testcases-1:
            self.ui.NextButton.setText("Завершить")
        else:
            self.ui.NextButton.setText("Следующий")
        if self.current_testcase == 0:
            self.ui.BackButton.setText("К настройкам")
        else:
            self.ui.BackButton.setText("Предыдущий")

    def nextButtonClicked(self):
        if self.current_testcase < self.number_of_testcases-1:
            self.proceed_to_next_testcase()
        self.update_text()

    def backButtonClicked(self):
        if self.current_testcase > 0:
            self.proceed_to_prev_testcase()
        else:
            self.toggle_test_configuration_window()
        self.update_text()


class TestConfigurationWindow(QMainWindow):
    def __init__(self, MainWindow):
        super(TestConfigurationWindow, self).__init__()
        self.ui = ui.ui_TestConfiguration.Ui_MainWindow()
        self.ui.setupUi(self)
        self.initialize_links(MainWindow)
        self.set_signals()

    def initialize_links(self, MainWindow):
        self.mw = MainWindow
        self.tpw = TestProgressWindow(self, MainWindow)
        print("TCW init")

    def set_signals(self):
        self.ui.BackButton.clicked.connect(self.toggle_main_window)
        self.ui.BeginButton.clicked.connect(self.toggle_progress_window)

    def toggle_main_window(self):
        self.mw.toggle_test_config_window()

    def toggle_progress_window(self):
        if self.tpw.isVisible():
            self.tpw.hide()
            self.show()
        else:
            self.tpw.setup_test_config(7, self.ui.ControlRadioButton.isChecked(), self.ui.TenCheckBox.isChecked(), self.ui.QuarterCheckBox.isChecked(), self.ui.HalfHundredCheckBox.isChecked(),
                                        self.ui.HundredcheckBox.isChecked(), self.ui.TwoHundredCheckBox.isChecked(), self.ui.HalfMillionCheckBox.isChecked(),
                                        self.ui.MillionCheckBox.isChecked())
            self.tpw.generate_testcases()
            self.tpw.show_current_testcase()
            self.tpw.show()
            self.hide()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = ui.ui_mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.initialize_links()
        self.set_signals()

    def set_signals(self):
        self.ui.TestButton.clicked.connect(self.toggle_test_config_window)

    def initialize_links(self):
        self.tcw = TestConfigurationWindow(self)

    def toggle_test_config_window(self):
        if self.tcw.isVisible():
            self.tcw.hide()
            self.show()
        else:
            self.tcw.show()
            self.hide()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
