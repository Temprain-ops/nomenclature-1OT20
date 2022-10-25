# This Python file uses the following encoding: utf-8
import os
import sys
import base64
from io import BytesIO
import base64
from io import BytesIO
from PySide2 import QtGui
from PIL import Image, ImageQt
from PySide2.QtWidgets import QLabel, QVBoxLayout, QDialogButtonBox, QDialog, QApplication, QWidget, QMainWindow, QAbstractItemDelegate, QTableWidgetItem, QMessageBox, QAbstractItemView, QFileDialog, QHBoxLayout, QPushButton, QSizePolicy, QSlider, QStyle
from PySide2.QtCore import QFile, QIODevice, Qt, QDir, QUrl
from PySide2.QtMultimedia import QMediaContent, QMediaPlayer
from PySide2.QtMultimediaWidgets import QVideoWidget
from PySide2.QtUiTools import QUiLoader
import ui.ui_mainwindow
import ui.ui_TestConfiguration
import ui.ui_TestProgress
import ui.ui_TestDialog
import ui.ui_LearnConfiguration
import ui.ui_PracticeWindow
import gerenerate_nomenclature.generator as gen
import numpy as np
import PySide2
from nomenclatures import get_nomenclatures
from PySide2.QtGui import QPixmap, QImage, QIcon
from PyQt5 import QtCore
from photo.globus import globus, million, two_hundred, hundred, half_hundred, schema


class VideoPlayer(QMainWindow):
    def __init__(self, MainWindow):
        super().__init__()
        self.setWindowTitle("Номенклатура")
        self.initialize_links(MainWindow)
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.resize(800,600)
        videoWidget = QVideoWidget()
        self.dur = 0

        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)

        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        self.error = QLabel()
        self.error.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

        openButton = QPushButton("Выбрать видео")
        openButton.setToolTip("Выбрать видеофайл(.avi)")
        openButton.setStatusTip("Выбрать видеофайл(.avi)")
        openButton.setFixedHeight(24)
        openButton.clicked.connect(self.openFile)

        backButton = QPushButton("Выйти из обучения")
        backButton.setFixedHeight(24)
        backButton.clicked.connect(self.toggle_main_window)

        nextButton = QPushButton("Перейти к презентации")
        nextButton.setFixedHeight(24)
        nextButton.clicked.connect(self.toggle_theory_window)

        # Create a widget for window contents
        wid = QWidget(self)
        self.setCentralWidget(wid)

        # Create layouts to place inside widget
        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.positionSlider)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(backButton)
        buttonLayout.addWidget(openButton)
        buttonLayout.addWidget(nextButton)

        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        layout.addLayout(controlLayout)
        layout.addWidget(self.error)
        layout.addLayout(buttonLayout)

        # Set widget to contain window contents
        wid.setLayout(layout)

        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.error.connect(self.handleError)
        self.fileName = './Номенклатура топографических карт.avi'
        self.playVideo()

    def initialize_links(self, MainWindow):
        self.mw = MainWindow
        self.tw = TheoryWindow(self)

    def toggle_main_window(self):
        self.mw.toggle_video_window()

    def toggle_theory_window(self):
        if self.tw.isVisible():
            self.tw.hide()
            self.show()
            geometry = PySide2.QtCore.QRect()
            geometry.setX(self.tw.pos().toTuple()[0])
            geometry.setY(self.tw.pos().toTuple()[1]+30)
            self.setGeometry(geometry)
            self.resize(self.tw.width(), self.tw.height())
        else:
            self.tw.show()
            self.hide()
            geometry = PySide2.QtCore.QRect()
            geometry.setX(self.pos().toTuple()[0])
            geometry.setY(self.pos().toTuple()[1]+30)
            self.tw.setGeometry(geometry)
            self.tw.resize(self.width(), self.height())
        print(self.tw.pos())
        print(self.pos())

    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Movie", QDir.homePath())
        self.playVideo()

    def playVideo(self):
        if self.fileName != '':
            self.mediaPlayer.setMedia(
                    QMediaContent(QUrl.fromLocalFile(self.fileName)))
            self.playButton.setEnabled(True)

    def exitCall(self):
        sys.exit(app.exec_())

    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        if position == self.dur:
            self.setPosition(0)
            self.play()
        self.positionSlider.setValue(position)

    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)
        self.dur = duration

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)

    def handleError(self):
        self.playButton.setEnabled(False)
        self.error.setText("Error: " + self.mediaPlayer.errorString())


class TheoryWindow(QMainWindow):
    def __init__(self, VideoWindow):
        super(TheoryWindow, self).__init__()
        self.ui = ui.ui_LearnConfiguration.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Номенклатура")
        self.initialize_links(VideoWindow)
        self.set_signals()
        self.image_list = [self.load_images(globus), self.load_images(million), self.load_images(two_hundred), self.load_images(hundred), self.load_images(half_hundred), self.load_images(schema)]
        self.cur_image = 0
        self.show_current_image()
        self.ui.label.installEventFilter(self)

    def eventFilter(self, source, event):
        if (source is self.ui.label and event.type() == QtCore.QEvent.Resize):
            # re-scale the pixmap when the label resizes
            self.ui.label.setMinimumSize(1, 1)
            self.ui.label.setPixmap(self.pixmap.scaled(
                self.ui.label.size(), PySide2.QtCore.Qt.KeepAspectRatio,
                PySide2.QtCore.Qt.SmoothTransformation))
        return super(TheoryWindow, self).eventFilter(source, event)

    def load_images(self, im):
        byte_data = base64.b64decode(im)
        image_data = BytesIO(byte_data)
        image = Image.open(image_data)
        qImage = ImageQt.ImageQt(image)
        return qImage

    def initialize_links(self, VideoWindow):
        self.vw = VideoWindow

    def set_signals(self):
        self.ui.backButton.clicked.connect(self.prev)
        self.ui.nextButton.clicked.connect(self.next)

    def toggle_video_window(self):
        self.vw.toggle_theory_window()

    def update_text_and_visibility(self):
        if self.cur_image == 0:
            self.ui.backButton.setText("Выйти из презентации")
            self.ui.nextButton.setText("Следующий слайд")
        elif self.cur_image == len(self.image_list)-1:
            self.ui.backButton.setText("Предыдущий слайд")
            self.ui.nextButton.setText("Выйти из презентации")
        else:
            self.ui.backButton.setText("Предыдущий слайд")
            self.ui.nextButton.setText("Следующий слайд")

    def show_current_image(self):
        self.pixmap = QPixmap(self.image_list[self.cur_image])
        self.ui.label.setPixmap(self.pixmap.scaled(
            self.ui.label.size(), PySide2.QtCore.Qt.KeepAspectRatio,
            PySide2.QtCore.Qt.SmoothTransformation))
        #self.ui.label.setAlignment(QtCore.Qt.AlignCenter)
        self.update_text_and_visibility()

    def next(self):
        if self.cur_image != len(self.image_list)-1:
            self.cur_image += 1
            self.show_current_image()
        else:
            self.cur_image = 0
            self.show_current_image()
            self.toggle_video_window()

    def prev(self):
        if self.cur_image != 0:
            self.cur_image -= 1
            self.show_current_image()
        else:
            self.toggle_video_window()


class TestDialog(QDialog):
    def __init__(self, shown_text, TestConfigurationWindow, TestProgressWindow):
        super(TestDialog, self).__init__()
        self.ui = ui.ui_TestDialog.Ui_Dialog()
        self.ui.setupUi(self)
        self.initialize_links(TestConfigurationWindow, TestProgressWindow)
        self.initialize_ui(shown_text)
        self.set_signals()

    def initialize_links(self, TestConfigurationWindow, TestProgressWindow):
        self.tcw = TestConfigurationWindow
        self.tpw = TestProgressWindow

    def initialize_ui(self, shown_text):
        self.setWindowTitle("Результаты:")
        self.ui.label.setText(shown_text)
        self.ui.label.setAlignment(Qt.AlignLeft)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)

    def toggle_TestConfigurationWindow(self):
        self.tcw.toggle_progress_window()
        self.close()

    def toggle_TestProgressWindow(self):
        self.tcw.toggle_progress_window()
        self.tcw.toggle_progress_window()
        self.close()

    def set_signals(self):
        self.ui.AgainButton.clicked.connect(self.toggle_TestProgressWindow)
        self.ui.BackButton.clicked.connect(self.toggle_TestConfigurationWindow)


class PracticeWindow(QMainWindow):
    def __init__(self, MainWindow):
        super(PracticeWindow, self).__init__()
        self.ui = ui.ui_PracticeWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Номенклатура")
        self.initialize_links(MainWindow)
        self.initialize_table()
        self.set_signals()

    def initialize_links(self, MainWindow):
        self.mw = MainWindow

    def initialize_table(self):
        for i in range(3):
            for j in range(3):
                self.ui.MapTable.setItem(i, j, QTableWidgetItem(""))
                self.ui.MapTable.item(i, j).setTextAlignment(QtCore.Qt.AlignCenter)
                if i != 1 or j != 1:
                    self.ui.MapTable.item(i, j).setFlags(Qt.ItemIsEditable)

    def clear_table(self):
        for i in range(3):
            for j in range(3):
                self.ui.MapTable.setItem(i, j, QTableWidgetItem(""))

    def set_signals(self):
        self.ui.backButton.clicked.connect(self.backButtonClicked)
        self.ui.clearButton.clicked.connect(self.clear_table)
        self.ui.generateButton.clicked.connect(self.generate_and_show)

    def generate_and_show(self):
        try:
            self.answers = get_nomenclatures(self.ui.MapTable.item(1, 1).text())
        except:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Ошибка!")
            dlg.setText("Неверный формат!")
            button = dlg.exec()
            return
        for i in range(9):
            self.ui.MapTable.setItem(i//3, i%3, QTableWidgetItem(self.answers[i]))
            self.ui.MapTable.item(i//3, i%3).setTextAlignment(QtCore.Qt.AlignCenter)
            if i//3 != 1 or i%3 != 1:
                self.ui.MapTable.item(i//3, i%3).setFlags(Qt.ItemIsEditable)

    def backButtonClicked(self):
        self.mw.toggle_practice_window()
        self.clear_table()


class TestProgressWindow(QMainWindow):
    def __init__(self, TestConfigurationWindow, MainWindow):
        super(TestProgressWindow, self).__init__()
        self.ui = ui.ui_TestProgress.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Номенклатура")
        self.initialize_links(MainWindow, TestConfigurationWindow)
        self.set_signals()

    def initialize_links(self, MainWindow, TestConfigurationWindow):
        self.mw = MainWindow
        self.tcw = TestConfigurationWindow

    def initialize_table(self):
        for i in range(3):
            for j in range(3):
                self.ui.MapTable.item(i, j).setTextAlignment(QtCore.Qt.AlignCenter)

    def clear_table(self):
        for i in range(3):
            for j in range(3):
                self.ui.MapTable.setItem(i, j, QTableWidgetItem(""))

    def set_signals(self):
        self.ui.BackButton.clicked.connect(self.backButtonClicked)
        self.ui.NextButton.clicked.connect(self.nextButtonClicked)
        self.ui.CheckButton.pressed.connect(self.checkButtonPressed)
        self.ui.CheckButton.released.connect(self.checkButtonReleased)

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
        self.answers = [[""]*9]*self.number_of_testcases
        self.current_testcase = 0
        self.initialize_table()
        if control:
            self.ui.CheckButton.hide()
        else:
            self.ui.CheckButton.show()

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
        print(self.testcases)

    def save_answer(self):
        answer = []
        for i in range(3):
            for j in range(3):
                answer.append(self.ui.MapTable.item(i, j).text())
        self.answers[self.current_testcase] = answer
        print(self.answers)

    def show_current_testcase(self):
        self.clear_table()
        for i in range(9):
            self.ui.MapTable.setItem(i//3, i%3, QTableWidgetItem(self.answers[self.current_testcase][i]))
        self.ui.MapTable.setItem(1, 1, QTableWidgetItem(self.testcases[self.current_testcase][4]))
        self.ui.MapTable.item(1, 1).setFlags(Qt.ItemIsEditable)
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
        self.save_answer()
        if self.current_testcase < self.number_of_testcases-1:
            self.proceed_to_next_testcase()
        else:
            dlg = TestDialog(self.compileResult(), self.tcw, self)
            dlg.exec()
        self.update_text()

    def backButtonClicked(self):
        self.save_answer()
        if self.current_testcase > 0:
            self.proceed_to_prev_testcase()
        else:
            self.toggle_test_configuration_window()
        self.update_text()

    def checkButtonPressed(self):
        self.save_answer()
        matrix = [ans == case for ans, case in zip(self.answers[self.current_testcase], self.testcases[self.current_testcase])]
        for num in range(len(matrix)):
            if not matrix[num]:
                self.ui.MapTable.item(num//3, (num)%3).setBackground(QtGui.QBrush(QtGui.QColor(128, 0, 0)))
            else:
                self.ui.MapTable.item(num//3, (num)%3).setBackground(QtGui.QBrush(QtGui.QColor(0, 128, 0)))

    def checkButtonReleased(self):
        for i in range(3):
            for j in range(3):
                self.ui.MapTable.item(i, j).setBackground(QtGui.QBrush(QtGui.QColor(255, 255, 255)))

    def compileResult(self):
        results = np.sum([([ans == case for ans, case in zip(self.answers[i], self.testcases[i])]) for i in range(self.number_of_testcases)]) - self.number_of_testcases
        print(results)
        total_grade = round(10*results / (self.number_of_testcases*8), 1)
        summary = "Ваш результат: " + str(total_grade) + "\n" + "Номенклатуры в тесте: \n"
        if self.ten:
            summary += "1:10000 - Да\n"
        else:
            summary += "1:10000 - Нет\n"
        if self.quarter:
            summary += "1:25000 - Да\n"
        else:
            summary += "1:25000 - Нет\n"
        if self.half_hundred:
            summary += "1:50000 - Да\n"
        else:
            summary += "1:50000 - Нет\n"
        if self.hundred:
            summary += "1:100000 - Да\n"
        else:
            summary += "1:100000 - Нет\n"
        if self.two_hundred:
            summary += "1:200000 - Да\n"
        else:
            summary += "1:200000 - Нет\n"
        if self.half_million:
            summary += "1:500000 - Да\n"
        else:
            summary += "1:500000 - Нет\n"
        if self.million:
            summary += "1:1000000 - Да\n"
        else:
            summary += "1:1000000 - Нет\n"
        return summary


class TestConfigurationWindow(QMainWindow):
    def __init__(self, MainWindow):
        super(TestConfigurationWindow, self).__init__()
        self.ui = ui.ui_TestConfiguration.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Номенклатура")
        self.initialize_links(MainWindow)
        self.set_signals()

    def initialize_links(self, MainWindow):
        self.mw = MainWindow
        self.tpw = TestProgressWindow(self, MainWindow)

    def set_signals(self):
        self.ui.BackButton.clicked.connect(self.toggle_main_window)
        self.ui.BeginButton.clicked.connect(self.toggle_progress_window)
        self.ui.ControlRadioButton.clicked.connect(self.toggle_checkBoxes)
        self.ui.SelfRadioButton.clicked.connect(self.toggle_checkBoxes)

    def toggle_checkBoxes(self):
        if self.ui.ControlRadioButton.isChecked():
            self.ui.TenCheckBox.setCheckable(False)
            self.ui.QuarterCheckBox.setCheckable(False)
            self.ui.HalfHundredCheckBox.setCheckable(False)
            self.ui.HundredcheckBox.setCheckable(False)
            self.ui.TwoHundredCheckBox.setCheckable(False)
            self.ui.HalfMillionCheckBox.setCheckable(False)
            self.ui.MillionCheckBox.setCheckable(False)
        else:
            self.ui.TenCheckBox.setCheckable(True)
            self.ui.QuarterCheckBox.setCheckable(True)
            self.ui.HalfHundredCheckBox.setCheckable(True)
            self.ui.HundredcheckBox.setCheckable(True)
            self.ui.TwoHundredCheckBox.setCheckable(True)
            self.ui.HalfMillionCheckBox.setCheckable(True)
            self.ui.MillionCheckBox.setCheckable(True)

    def toggle_main_window(self):
        self.mw.toggle_test_config_window()

    def toggle_progress_window(self):
        if self.tpw.isVisible():
            self.tpw.hide()
            self.show()
        else:
            if self.ui.ControlRadioButton.isChecked():
                self.tpw.setup_test_config(7, self.ui.ControlRadioButton.isChecked(), True, True, True, True, True, True, True)
            elif self.ui.TenCheckBox.isChecked() or self.ui.QuarterCheckBox.isChecked() or self.ui.HalfHundredCheckBox.isChecked() or self.ui.HundredcheckBox.isChecked() or self.ui.TwoHundredCheckBox.isChecked() or self.ui.HalfMillionCheckBox.isChecked() or self.ui.MillionCheckBox.isChecked():
                self.tpw.setup_test_config(7, self.ui.ControlRadioButton.isChecked(), self.ui.TenCheckBox.isChecked(), self.ui.QuarterCheckBox.isChecked(), self.ui.HalfHundredCheckBox.isChecked(),
                                        self.ui.HundredcheckBox.isChecked(), self.ui.TwoHundredCheckBox.isChecked(), self.ui.HalfMillionCheckBox.isChecked(),
                                        self.ui.MillionCheckBox.isChecked())
            else:
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Ошибка!")
                dlg.setText("Выберите хотя бы один формат!")
                button = dlg.exec()
                return
            self.tpw.generate_testcases()
            self.tpw.show_current_testcase()
            self.tpw.update_text()
            self.tpw.show()
            self.hide()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = ui.ui_mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Номенклатура")
        self.initialize_links()
        self.set_signals()

    def set_signals(self):
        self.ui.TestButton.clicked.connect(self.toggle_test_config_window)
        #self.ui.theoryButton.clicked.connect(self.toggle_theory_window)
        self.ui.theoryButton.clicked.connect(self.toggle_video_window)
        self.ui.practiceButton.clicked.connect(self.toggle_practice_window)

    def initialize_links(self):
        self.tcw = TestConfigurationWindow(self)
        self.tw = TheoryWindow(self)
        self.pw = PracticeWindow(self)
        self.vw = VideoPlayer(self)

    def toggle_test_config_window(self):
        if self.tcw.isVisible():
            self.tcw.hide()
            self.show()
        else:
            self.tcw.show()
            self.hide()

    def toggle_theory_window(self):
        if self.tw.isVisible():
            self.tw.hide()
            self.show()
        else:
            self.tw.show()
            self.hide()

    def toggle_practice_window(self):
        if self.pw.isVisible():
            self.pw.hide()
            self.show()
        else:
            self.pw.show()
            self.hide()

    def toggle_video_window(self):
        if self.vw.isVisible():
            self.vw.hide()
            self.show()
        else:
            self.vw.show()
            self.hide()


if __name__ == "__main__":
    app = QApplication([])
    app.setAttribute(Qt.AA_DisableWindowContextHelpButton)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
