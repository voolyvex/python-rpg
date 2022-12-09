# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1338, 754)
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.full_screen_widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.full_screen_widget.sizePolicy().hasHeightForWidth())
        self.full_screen_widget.setSizePolicy(sizePolicy)
        self.full_screen_widget.setMinimumSize(QtCore.QSize(1320, 691))
        self.full_screen_widget.setAutoFillBackground(False)
        self.full_screen_widget.setStyleSheet("\n"
"background-color: rgb(24, 6, 0);")
        self.full_screen_widget.setObjectName("full_screen_widget")
        self.scrollArea = QtWidgets.QScrollArea(self.full_screen_widget)
        self.scrollArea.setGeometry(QtCore.QRect(790, 100, 291, 491))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(24, 6, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 6, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 6, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 6, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 6, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 6, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 6, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 6, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 6, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.scrollArea.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.scrollArea.setFont(font)
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(-17, -97, 289, 569))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.footerLabel = QtWidgets.QLabel(self.full_screen_widget)
        self.footerLabel.setGeometry(QtCore.QRect(400, 610, 87, 19))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.footerLabel.sizePolicy().hasHeightForWidth())
        self.footerLabel.setSizePolicy(sizePolicy)
        self.footerLabel.setStyleSheet("font: 8pt \"Perpetua\";\n"
"color: rgb(243, 187, 103);")
        self.footerLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.footerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.footerLabel.setObjectName("footerLabel")
        self.hero_LCD = QtWidgets.QLCDNumber(self.full_screen_widget)
        self.hero_LCD.setGeometry(QtCore.QRect(900, 10, 46, 23))
        self.hero_LCD.setDigitCount(3)
        self.hero_LCD.setProperty("intValue", 20)
        self.hero_LCD.setObjectName("hero_LCD")
        self.boss_LCD = QtWidgets.QLCDNumber(self.full_screen_widget)
        self.boss_LCD.setGeometry(QtCore.QRect(900, 40, 46, 23))
        self.boss_LCD.setDigitCount(3)
        self.boss_LCD.setProperty("intValue", 20)
        self.boss_LCD.setObjectName("boss_LCD")
        self.hero_health_label = QtWidgets.QLabel(self.full_screen_widget)
        self.hero_health_label.setGeometry(QtCore.QRect(830, 10, 70, 19))
        self.hero_health_label.setStyleSheet("color: rgb(255, 208, 151);\n"
"font: 75 12pt \"Perpetua Titling MT\";")
        self.hero_health_label.setObjectName("hero_health_label")
        self.boss_health_label = QtWidgets.QLabel(self.full_screen_widget)
        self.boss_health_label.setGeometry(QtCore.QRect(830, 40, 65, 19))
        self.boss_health_label.setStyleSheet("color: rgb(255, 208, 151);\n"
"font: 75 12pt \"Perpetua Titling MT\";")
        self.boss_health_label.setObjectName("boss_health_label")
        self.gameText = QtWidgets.QLabel(self.full_screen_widget)
        self.gameText.setGeometry(QtCore.QRect(790, 100, 271, 471))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(12)
        font.setKerning(True)
        self.gameText.setFont(font)
        self.gameText.setStyleSheet("font: 12pt \"Perpetua\";\n"
"color: rgb(255, 254, 218);;\n"
"margin-left: 3px;\n"
"")
        self.gameText.setWordWrap(True)
        self.gameText.setIndent(0)
        self.gameText.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.gameText.setObjectName("gameText")
        self.footerLabel.raise_()
        self.scrollArea.raise_()
        self.hero_LCD.raise_()
        self.boss_LCD.raise_()
        self.hero_health_label.raise_()
        self.boss_health_label.raise_()
        self.gameText.raise_()
        self.gridLayout.addWidget(self.full_screen_widget, 0, 0, 1, 1)
        self.background = QtWidgets.QFrame(self.centralwidget)
        self.background.setEnabled(True)
        self.background.setGeometry(QtCore.QRect(-1, -1, 800, 600))
        self.background.setMinimumSize(QtCore.QSize(800, 600))
        self.background.setMaximumSize(QtCore.QSize(800, 600))
        self.background.setAutoFillBackground(False)
        self.background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background.setObjectName("background")
        self.background_image = QtWidgets.QLabel(self.background)
        self.background_image.setGeometry(QtCore.QRect(10, 10, 800, 600))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.background_image.sizePolicy().hasHeightForWidth())
        self.background_image.setSizePolicy(sizePolicy)
        self.background_image.setMinimumSize(QtCore.QSize(800, 600))
        self.background_image.setMaximumSize(QtCore.QSize(999, 750))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(218, 218, 218))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 34, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 218, 218))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 34, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 218, 218))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.background_image.setPalette(palette)
        self.background_image.setText("")
        self.background_image.setPixmap(QtGui.QPixmap("../../img/landscape_greece_parthenon.jpg"))
        self.background_image.setScaledContents(True)
        self.background_image.setObjectName("background_image")
        self.setting_frame = QtWidgets.QFrame(self.background)
        self.setting_frame.setGeometry(QtCore.QRect(20, 130, 500, 375))
        self.setting_frame.setMinimumSize(QtCore.QSize(500, 375))
        self.setting_frame.setMaximumSize(QtCore.QSize(500, 375))
        self.setting_frame.setAutoFillBackground(False)
        self.setting_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setting_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setting_frame.setObjectName("setting_frame")
        self.image_box = QtWidgets.QLabel(self.setting_frame)
        self.image_box.setEnabled(True)
        self.image_box.setGeometry(QtCore.QRect(0, 30, 500, 375))
        self.image_box.setMinimumSize(QtCore.QSize(500, 375))
        self.image_box.setBaseSize(QtCore.QSize(500, 375))
        self.image_box.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.image_box.setText("")
        self.image_box.setPixmap(QtGui.QPixmap("../../img/greece_ruins.jpg"))
        self.image_box.setScaledContents(True)
        self.image_box.setObjectName("image_box")
        self.narratorText = QtWidgets.QLabel(self.background)
        self.narratorText.setGeometry(QtCore.QRect(16, 12, 511, 121))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.narratorText.setFont(font)
        self.narratorText.setStyleSheet("font: 75 14pt \"Perpetua\";\n"
"color: rgb(255, 254, 218);\n"
"border-bottom-color: rgb(255, 0, 255);\n"
"border-color: rgb(174, 119, 61);\n"
"border-width: 3px;\n"
"padding: 3px;\n"
"\n"
"\n"
"\n"
"")
        self.narratorText.setFrameShape(QtWidgets.QFrame.Panel)
        self.narratorText.setFrameShadow(QtWidgets.QFrame.Raised)
        self.narratorText.setLineWidth(1)
        self.narratorText.setMidLineWidth(1)
        self.narratorText.setWordWrap(True)
        self.narratorText.setObjectName("narratorText")
        self.startButton = QtWidgets.QPushButton(self.background)
        self.startButton.setGeometry(QtCore.QRect(531, 35, 235, 31))
        self.startButton.setMinimumSize(QtCore.QSize(235, 0))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.startButton.setFont(font)
        self.startButton.setAutoFillBackground(False)
        self.startButton.setStyleSheet("background-color: rgb(201, 201, 210);\n"
"color: rgb(255, 0, 0);\n"
"font: 75 14pt \"Perpetua\";")
        self.startButton.setAutoDefault(False)
        self.startButton.setDefault(True)
        self.startButton.setFlat(False)
        self.startButton.setObjectName("startButton")
        self.Title = QtWidgets.QLabel(self.background)
        self.Title.setGeometry(QtCore.QRect(532, 11, 105, 26))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.Title.sizePolicy().hasHeightForWidth())
        self.Title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Title.setFont(font)
        self.Title.setStyleSheet("font: 75 16pt \"Perpetua\";\n"
"color: rgb(255, 255, 255);\n"
"padding: .5px;\n"
"\n"
"")
        self.Title.setObjectName("Title")
        self.itemButton = QtWidgets.QPushButton(self.background)
        self.itemButton.setGeometry(QtCore.QRect(560, 110, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.itemButton.setFont(font)
        self.itemButton.setAutoFillBackground(False)
        self.itemButton.setStyleSheet("background-color: grey;\n"
"color: white;\n"
"font: 75 14pt \"Perpetua\";\n"
"")
        self.itemButton.setAutoDefault(True)
        self.itemButton.setDefault(True)
        self.itemButton.setFlat(False)
        self.itemButton.setObjectName("itemButton")
        self.attackButton = QtWidgets.QPushButton(self.background)
        self.attackButton.setGeometry(QtCore.QRect(690, 110, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.attackButton.setFont(font)
        self.attackButton.setAutoFillBackground(False)
        self.attackButton.setStyleSheet("background-color: darkgrey;\n"
"color: white;\n"
"font: 75 14pt \"Perpetua\";\n"
"")
        self.attackButton.setAutoDefault(False)
        self.attackButton.setDefault(True)
        self.attackButton.setFlat(False)
        self.attackButton.setObjectName("attackButton")
        self.title_image_box = QtWidgets.QLabel(self.background)
        self.title_image_box.setGeometry(QtCore.QRect(540, 150, 235, 352))
        self.title_image_box.setBaseSize(QtCore.QSize(400, 300))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title_image_box.setFont(font)
        self.title_image_box.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.title_image_box.setText("")
        self.title_image_box.setPixmap(QtGui.QPixmap("../../img/hero_lion_skin_stylized.jpg"))
        self.title_image_box.setScaledContents(False)
        self.title_image_box.setObjectName("title_image_box")
        self.Title_2 = QtWidgets.QLabel(self.background)
        self.Title_2.setGeometry(QtCore.QRect(643, 11, 77, 26))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.Title_2.setFont(font)
        self.Title_2.setStyleSheet("font: 75 italic 16pt \"Perpetua\";\n"
"color: rgb(255, 255, 255);\n"
"padding: .5px;\n"
"\n"
"")
        self.Title_2.setObjectName("Title_2")
        self.background_image.raise_()
        self.narratorText.raise_()
        self.setting_frame.raise_()
        self.startButton.raise_()
        self.Title.raise_()
        self.attackButton.raise_()
        self.Title_2.raise_()
        self.title_image_box.raise_()
        self.itemButton.raise_()
        self.full_screen_widget.raise_()
        self.background.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1338, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.startButton, self.scrollArea)
        MainWindow.setTabOrder(self.scrollArea, self.attackButton)
        MainWindow.setTabOrder(self.attackButton, self.itemButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HERAKLES"))
        self.footerLabel.setText(_translate("MainWindow", "Footer text goes here"))
        self.hero_health_label.setText(_translate("MainWindow", "Hero HP"))
        self.boss_health_label.setText(_translate("MainWindow", "Boss HP"))
        self.gameText.setText(_translate("MainWindow", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."))
        self.narratorText.setText(_translate("MainWindow", "Ut aliquam purus sit amet luctus venenatis lectus. Velit euismod in pellentesque massa placerat duis ultricies lacus sed."))
        self.startButton.setText(_translate("MainWindow", "START GAME!"))
        self.Title.setText(_translate("MainWindow", "HERAKLES"))
        self.itemButton.setText(_translate("MainWindow", "Item"))
        self.attackButton.setText(_translate("MainWindow", "Attack"))
        self.Title_2.setText(_translate("MainWindow", "Adventure"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())