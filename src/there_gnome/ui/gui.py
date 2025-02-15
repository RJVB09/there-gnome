# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFrame,
    QHBoxLayout, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpinBox, QStatusBar,
    QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
        def change_butt(self, butt):
                if butt:
                        self.frame.setStyleSheet(u"background-image: url(:/Images/gnomebutt.jpg);\n"
                        "background-color: #cccccc;\n"
                        "background-position: center;\n"
                        "border-image: url(:/Images/gnomebutt.jpg) 0 0 0 0 stretch stretch;")
                else:
                        self.frame.setStyleSheet(u"background-image: url(:/Images/gnomenobutt.jpg);\n"
                        "background-color: #cccccc;\n"
                        "background-position: center;\n"
                        "border-image: url(:/Images/gnomenobutt.jpg) 0 0 0 0 stretch stretch;")
                
        def change_laser_eyes(self, laser_eyes):
                if laser_eyes:
                      self.frame_2.setStyleSheet(u"background-image: url(:/Images/gnomelazer_eyes.png);\n"
                        "background-color: #cccccc;\n"
                        "background-position: center;\n"
                        "border-image: url(:/Images/gnomelazer_eyes.png) 0 0 0 0 stretch stretch;")
                else:
                      self.frame_2.setStyleSheet(u"background-image: url(:/Images/gnome.png);\n"
                        "background-color: #cccccc;\n"
                        "background-position: center;\n"
                        "border-image: url(:/Images/gnome.png) 0 0 0 0 stretch stretch;")

        def setupUi(self, MainWindow):
                if not MainWindow.objectName():
                        MainWindow.setObjectName(u"MainWindow")
                MainWindow.resize(1013, 790)
                MainWindow.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 0, 0, 255), stop:0.479904 rgba(255, 0, 0, 255), stop:0.522685 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.33 rgba(0, 0, 0, 255), stop:0.34 rgba(255, 30, 30, 255), stop:0.66 rgba(255, 0, 0, 255), stop:0.67 rgba(255, 255, 0, 255), stop:1 rgba(255, 255, 0, 255));")
                self.centralwidget = QWidget(MainWindow)
                self.centralwidget.setObjectName(u"centralwidget")
                self.centralwidget.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.273, fy:0.238636, stop:0 rgba(126, 148, 146, 255), stop:0.465909 rgba(0, 86, 79, 255), stop:1 rgba(22, 22, 22, 255));")
                self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
                self.verticalLayout_3.setObjectName(u"verticalLayout_3")
                self.label_2 = QLabel(self.centralwidget)
                self.label_2.setObjectName(u"label_2")
                self.label_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
        "color: rgb(25, 25, 25);\n"
        "font: 30pt \"Impact\";")
                self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

                self.verticalLayout_3.addWidget(self.label_2)

                self.horizontalLayout = QHBoxLayout()
                self.horizontalLayout.setObjectName(u"horizontalLayout")
                self.verticalLayout_4 = QVBoxLayout()
                self.verticalLayout_4.setObjectName(u"verticalLayout_4")
                self.horizontalLayout_3 = QHBoxLayout()
                self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
                self.frame = QFrame(self.centralwidget)
                self.frame.setObjectName(u"frame")
                sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
                self.frame.setSizePolicy(sizePolicy)
                self.frame.setMinimumSize(QSize(150, 0))
                self.frame.setStyleSheet(u"background-image: url(:/Images/gnomenobutt.jpg);\n"
        "background-color: #cccccc;\n"
        "background-position: center;\n"
        "border-image: url(:/Images/gnomenobutt.jpg) 0 0 0 0 stretch stretch;")
                self.frame.setFrameShape(QFrame.Shape.StyledPanel)
                self.frame.setFrameShadow(QFrame.Shadow.Raised)

                self.horizontalLayout_3.addWidget(self.frame)

                self.verticalLayout_9 = QVBoxLayout()
                self.verticalLayout_9.setObjectName(u"verticalLayout_9")
                self.toneDisplay = QLabel(self.centralwidget)
                self.toneDisplay.setObjectName(u"toneDisplay")
                self.toneDisplay.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
        "font: bold 30pt \"Comic Sans MS\";\n"
        "color: rgb(255, 255, 255);")
                self.toneDisplay.setTextFormat(Qt.TextFormat.PlainText)
                self.toneDisplay.setAlignment(Qt.AlignmentFlag.AlignCenter)

                self.verticalLayout_9.addWidget(self.toneDisplay)

                self.plot_widget = PlotWidget(self.centralwidget)
                self.plot_widget.setObjectName(u"plot_widget")
                self.plot_widget.setMinimumSize(QSize(650, 0))
                self.plot_widget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(65, 111, 120, 255));")

                self.verticalLayout_9.addWidget(self.plot_widget)


                self.horizontalLayout_3.addLayout(self.verticalLayout_9)

                self.frame_2 = QFrame(self.centralwidget)
                self.frame_2.setObjectName(u"frame_2")
                sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
                self.frame_2.setSizePolicy(sizePolicy)
                self.frame_2.setMinimumSize(QSize(150, 0))
                self.frame_2.setStyleSheet(u"background-image: url(:/Images/gnome.png);\n"
        "background-color: #cccccc;\n"
        "background-position: center;\n"
        "border-image: url(:/Images/gnome.png) 0 0 0 0 stretch stretch;")
                self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
                self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

                self.horizontalLayout_3.addWidget(self.frame_2)


                self.verticalLayout_4.addLayout(self.horizontalLayout_3)

                self.Settings = QHBoxLayout()
                self.Settings.setObjectName(u"Settings")
                self.verticalLayout = QVBoxLayout()
                self.verticalLayout.setObjectName(u"verticalLayout")
                self.lengthLabel = QLabel(self.centralwidget)
                self.lengthLabel.setObjectName(u"lengthLabel")
                self.lengthLabel.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
        "font: bold 10pt \"Comic Sans MS\";\n"
        "color: rgb(255, 255, 255);")
                self.lengthLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

                self.verticalLayout.addWidget(self.lengthLabel)

                self.lengthDoubleSpinBox = QDoubleSpinBox(self.centralwidget)
                self.lengthDoubleSpinBox.setObjectName(u"lengthDoubleSpinBox")
                self.lengthDoubleSpinBox.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
        "font: bold 10pt \"Comic Sans MS\";\n"
        "color: rgb(0, 0, 0);")
                self.lengthDoubleSpinBox.setDecimals(0)
                self.lengthDoubleSpinBox.setMinimum(1.000000000000000)
                self.lengthDoubleSpinBox.setMaximum(100.000000000000000)
                self.lengthDoubleSpinBox.setSingleStep(1.000000000000000)
                self.lengthDoubleSpinBox.setValue(50.000000000000000)

                self.verticalLayout.addWidget(self.lengthDoubleSpinBox)


                self.Settings.addLayout(self.verticalLayout)

                self.verticalLayout_2 = QVBoxLayout()
                self.verticalLayout_2.setObjectName(u"verticalLayout_2")
                self.offsetLabel = QLabel(self.centralwidget)
                self.offsetLabel.setObjectName(u"offsetLabel")
                self.offsetLabel.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
        "font: bold 10pt \"Comic Sans MS\";\n"
        "color: rgb(255, 255, 255);")
                self.offsetLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

                self.verticalLayout_2.addWidget(self.offsetLabel)

                self.offsetSpinBox = QSpinBox(self.centralwidget)
                self.offsetSpinBox.setObjectName(u"offsetSpinBox")
                self.offsetSpinBox.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
        "font: bold 10pt \"Comic Sans MS\";\n"
        "color: rgb(0, 0, 0);")
                self.offsetSpinBox.setMinimum(-20)
                self.offsetSpinBox.setMaximum(20)

                self.verticalLayout_2.addWidget(self.offsetSpinBox)


                self.Settings.addLayout(self.verticalLayout_2)

                self.verticalLayout_5 = QVBoxLayout()
                self.verticalLayout_5.setObjectName(u"verticalLayout_5")
                self.invertedToggle = QCheckBox(self.centralwidget)
                self.invertedToggle.setObjectName(u"invertedToggle")
                self.invertedToggle.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
        "font: bold 10pt \"Comic Sans MS\";\n"
        "color: rgb(0, 0, 0);")

                self.verticalLayout_5.addWidget(self.invertedToggle)


                self.Settings.addLayout(self.verticalLayout_5)

                self.verticalLayout_6 = QVBoxLayout()
                self.verticalLayout_6.setObjectName(u"verticalLayout_6")
                self.rangeLabel = QLabel(self.centralwidget)
                self.rangeLabel.setObjectName(u"rangeLabel")
                self.rangeLabel.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
        "font: bold 10pt \"Comic Sans MS\";\n"
        "color: rgb(255, 255, 255);")
                self.rangeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

                self.verticalLayout_6.addWidget(self.rangeLabel)

                self.rangeDoubleSpinBox = QDoubleSpinBox(self.centralwidget)
                self.rangeDoubleSpinBox.setObjectName(u"rangeDoubleSpinBox")
                self.rangeDoubleSpinBox.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
        "font: bold 10pt \"Comic Sans MS\";\n"
        "color: rgb(0, 0, 0);")
                self.rangeDoubleSpinBox.setDecimals(0)
                self.rangeDoubleSpinBox.setMaximum(1000.000000000000000)
                self.rangeDoubleSpinBox.setSingleStep(100.000000000000000)
                self.rangeDoubleSpinBox.setValue(300.000000000000000)

                self.verticalLayout_6.addWidget(self.rangeDoubleSpinBox)


                self.Settings.addLayout(self.verticalLayout_6)

                self.verticalLayout_7 = QVBoxLayout()
                self.verticalLayout_7.setObjectName(u"verticalLayout_7")
                self.label = QLabel(self.centralwidget)
                self.label.setObjectName(u"label")
                self.label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
        "font: bold 10pt \"Comic Sans MS\";\n"
        "color: rgb(255, 255, 255);")
                self.label.setTextFormat(Qt.TextFormat.MarkdownText)
                self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

                self.verticalLayout_7.addWidget(self.label)

                self.volfalloffDoubleSpinBox = QDoubleSpinBox(self.centralwidget)
                self.volfalloffDoubleSpinBox.setObjectName(u"volfalloffDoubleSpinBox")
                self.volfalloffDoubleSpinBox.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
        "font: bold 10pt \"Comic Sans MS\";\n"
        "color: rgb(0, 0, 0);")
                self.volfalloffDoubleSpinBox.setMinimum(-10.000000000000000)
                self.volfalloffDoubleSpinBox.setMaximum(10.000000000000000)

                self.verticalLayout_7.addWidget(self.volfalloffDoubleSpinBox)


                self.Settings.addLayout(self.verticalLayout_7)


                self.verticalLayout_4.addLayout(self.Settings)


                self.horizontalLayout.addLayout(self.verticalLayout_4)


                self.verticalLayout_3.addLayout(self.horizontalLayout)

                self.horizontalLayout_2 = QHBoxLayout()
                self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
                self.stopButton = QPushButton(self.centralwidget)
                self.stopButton.setObjectName(u"stopButton")
                self.stopButton.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 142, 0, 255));\n"
        "font: bold 10pt \"Comic Sans MS\";\n"
        "color: rgb(0, 0, 0);")

                self.horizontalLayout_2.addWidget(self.stopButton)

                self.playButton = QPushButton(self.centralwidget)
                self.playButton.setObjectName(u"playButton")
                self.playButton.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
        "font: bold 10pt \"Comic Sans MS\";\n"
        "color: rgb(0, 0, 0);")

                self.horizontalLayout_2.addWidget(self.playButton)


                self.verticalLayout_3.addLayout(self.horizontalLayout_2)

                MainWindow.setCentralWidget(self.centralwidget)
                self.menubar = QMenuBar(MainWindow)
                self.menubar.setObjectName(u"menubar")
                self.menubar.setGeometry(QRect(0, 0, 1013, 22))
                MainWindow.setMenuBar(self.menubar)
                self.statusbar = QStatusBar(MainWindow)
                self.statusbar.setObjectName(u"statusbar")
                MainWindow.setStatusBar(self.statusbar)

                self.retranslateUi(MainWindow)

                QMetaObject.connectSlotsByName(MainWindow)
        # setupUi

        def retranslateUi(self, MainWindow):
                MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"THERE-GNOME (Premium-edition)", None))
                self.label_2.setText(QCoreApplication.translate("MainWindow", u"THERE-GNOME", None))
                self.lengthLabel.setText(QCoreApplication.translate("MainWindow", u"Note length (mm)", None))
                self.offsetLabel.setText(QCoreApplication.translate("MainWindow", u"Offset", None))
                self.invertedToggle.setText(QCoreApplication.translate("MainWindow", u"Inverted", None))
                self.rangeLabel.setText(QCoreApplication.translate("MainWindow", u"Range (mm)", None))
                self.label.setText(QCoreApplication.translate("MainWindow", u"Volume falloff", None))
                self.stopButton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
                self.playButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        # retranslateUi

