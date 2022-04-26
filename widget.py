# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide2.QtWidgets import QApplication, QWidget, QMainWindow
from PySide2.QtCore import QFile, QIODevice
from PySide2.QtUiTools import QUiLoader
import ui.ui_mainwindow
import ui.ui_TestConfiguration
import ui.ui_TestProgress


class TestProgress(QMainWindow):
    def __init__(self):
        super(TestProgress, self).__init__()
        self.ui = ui.ui_TestProgress.Ui_MainWindow()
        self.ui.setupUi(self)


class TestConfigurationWindow(QMainWindow):
    def __init__(self, MainWindow):
        super(TestConfigurationWindow, self).__init__()
        self.ui = ui.ui_TestConfiguration.Ui_MainWindow()
        self.ui.setupUi(self)
        self.mw = MainWindow
        self.pw = TestProgress()
        self.ui.Back.clicked.connect(self.toggle_main_window)
        self.ui.Begin.clicked.connect(self.toggle_progress_window)

    def toggle_main_window(self):
        self.mw.toggle_test_config_window()

    def toggle_progress_window(self):
        if self.pw.isVisible():
            self.pw.hide()
            self.show()
        else:
            self.pw.show()
            self.hide()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = ui.ui_mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.tcw = TestConfigurationWindow(self)
        self.ui.TestButton.clicked.connect(self.toggle_test_config_window)

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
