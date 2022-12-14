from PyQt5 import QtCore, QtGui, QtWidgets


ICON = 'img/icon.jpg'

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 720))
        MainWindow.setBaseSize(QtCore.QSize(1000, 720))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setWindowIcon(QtGui.QIcon(ICON))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(1000, 750))
        self.centralwidget.setMaximumSize(QtCore.QSize(1000, 750))
        self.centralwidget.setObjectName("centralwidget")
        self.full_screen_widget = QtWidgets.QWidget(self.centralwidget)
        self.full_screen_widget.setGeometry(QtCore.QRect(0, -1, 1331, 731))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.full_screen_widget.sizePolicy().hasHeightForWidth())
        self.full_screen_widget.setSizePolicy(sizePolicy)
        self.full_screen_widget.setMinimumSize(QtCore.QSize(1000, 720))
        self.full_screen_widget.setBaseSize(QtCore.QSize(1000, 720))
        self.full_screen_widget.setWhatsThis("")
        self.full_screen_widget.setAutoFillBackground(False)
        self.full_screen_widget.setStyleSheet("background-color: rgb(24, 6, 0);")
        self.full_screen_widget.setObjectName("full_screen_widget")
# title
        self.Title_2 = QtWidgets.QLabel(self.full_screen_widget)
        self.Title_2.setGeometry(QtCore.QRect(900, 13, 91, 32))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.Title_2.setFont(font)
        self.Title_2.setStyleSheet("font: 75 italic 18pt \"Perpetua\";\n"
                                "color: rgb(255, 255, 255);\n"
                                "padding: .5px;"
                                )
        self.Title_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.Title_2.setObjectName("Title_2")
        self.Title_1 = QtWidgets.QLabel(self.full_screen_widget)
        self.Title_1.setGeometry(QtCore.QRect(788, 11, 111, 36))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.Title_1.sizePolicy().hasHeightForWidth())
        self.Title_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Title_1.setFont(font)
        self.Title_1.setStyleSheet("font: 75 18pt \"Perpetua\";\n"
                                "color: rgb(255, 255, 255);\n"
                                "padding: .5px;"
                                )
        self.Title_1.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.Title_1.setObjectName("Title_1")
# initialize the start button
        self.startButton = QtWidgets.QPushButton(self.full_screen_widget)
        self.startButton.setGeometry(QtCore.QRect(810, 45, 150, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)
        self.startButton.setMinimumSize(QtCore.QSize(100, 0))
        self.startButton.setBaseSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.startButton.setFont(font)
        self.startButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.startButton.setAutoFillBackground(True)
        self.startButton.setStyleSheet("background-color: rgb(201, 201, 210);\n"
                                        "color: rgb(255, 0, 0);\n"
                                        "font: 75 14pt \"Perpetua\";")
        self.startButton.setAutoDefault(True)
        self.startButton.setDefault(True)
        self.startButton.setFlat(False)
        self.startButton.setObjectName("startButton")
# left image
        self.left_image_landscape = QtWidgets.QLabel(self.full_screen_widget)
        self.left_image_landscape.setEnabled(True)
        self.left_image_landscape.setGeometry(QtCore.QRect(17, 306, 600, 400))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.left_image_landscape.sizePolicy().hasHeightForWidth())
        self.left_image_landscape.setSizePolicy(sizePolicy)
        self.left_image_landscape.setMinimumSize(QtCore.QSize(600, 400))
        self.left_image_landscape.setMaximumSize(QtCore.QSize(600, 400))
        self.left_image_landscape.setBaseSize(QtCore.QSize(600, 400))
        self.left_image_landscape.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.left_image_landscape.setAutoFillBackground(False)
        self.left_image_landscape.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_image_landscape.setText("")
        self.left_image_landscape.setScaledContents(True)
        self.left_image_landscape.setObjectName("left_image_landscape")
# right image
        self.right_image_portrait = QtWidgets.QLabel(self.full_screen_widget)
        self.right_image_portrait.setGeometry(QtCore.QRect(632, 183, 350, 525))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.right_image_portrait.sizePolicy().hasHeightForWidth())
        self.right_image_portrait.setSizePolicy(sizePolicy)
        self.right_image_portrait.setMinimumSize(QtCore.QSize(350, 525))
        self.right_image_portrait.setMaximumSize(QtCore.QSize(350, 525))
        self.right_image_portrait.setBaseSize(QtCore.QSize(350, 525))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.right_image_portrait.setFont(font)
        self.right_image_portrait.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.right_image_portrait.setText("")
        self.right_image_portrait.setScaledContents(True)
        self.right_image_portrait.setObjectName("right_image_portrait")
        self.widget = QtWidgets.QWidget(self.full_screen_widget)
        self.widget.setGeometry(QtCore.QRect(635, 55, 145, 110))
        self.widget.setObjectName("widget")
# HUD
        self.hudLayout = QtWidgets.QVBoxLayout(self.widget)
        self.hudLayout.setContentsMargins(0, 0, 0, 0)
        self.hudLayout.setObjectName("hudLayout")
        self.hudLayout_HP = QtWidgets.QGridLayout()
        self.hudLayout_HP.setContentsMargins(1, -1, 1, -1)
        self.hudLayout_HP.setObjectName("hudLayout_HP")
        self.boss_health_label = QtWidgets.QLabel(self.widget)
        self.boss_health_label.setStyleSheet("color: rgb(255, 208, 151);\n"
                        "font: 75 10pt \"Perpetua Titling MT\";")
        self.boss_health_label.setAlignment(QtCore.Qt.AlignCenter)
        self.boss_health_label.setObjectName("boss_health_label")
        self.hudLayout_HP.addWidget(self.boss_health_label, 0, 0, 1, 1)
        self.boss_LCD = QtWidgets.QLCDNumber(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.boss_LCD.sizePolicy().hasHeightForWidth())
        self.boss_LCD.setSizePolicy(sizePolicy)
        self.boss_LCD.setMaximumSize(QtCore.QSize(16777215, 16777211))
        self.boss_LCD.setDigitCount(3)
        self.boss_LCD.setProperty("intValue", 000)
        self.boss_LCD.setObjectName("boss_LCD")
        self.hudLayout_HP.addWidget(self.boss_LCD, 0, 1, 1, 1)

        self.hudLayout.addLayout(self.hudLayout_HP)
        
        self.widget1 = QtWidgets.QWidget(self.full_screen_widget)
        self.widget1.setGeometry(QtCore.QRect(13, 9, 607, 280))
        self.widget1.setObjectName("widget1")
        self.narratorLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.narratorLayout.setContentsMargins(0, 0, 0, 0)
        self.narratorLayout.setObjectName("narratorLayout")
        self.narratorText_1 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.narratorText_1.setFont(font)
        self.narratorText_1.setStyleSheet("font: 75 14pt \"Perpetua\";\n"
                                        "color: rgb(255, 254, 218);\n"
                                        "border-bottom-color: rgb(255, 0, 255);\n"
                                        "border-color: rgb(174, 119, 61);\n"
                                        "border-width: 3px;\n"
                                        "padding: 36px;\n"
                                        )
        self.narratorText_1.setFrameShape(QtWidgets.QFrame.Panel)
        self.narratorText_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.narratorText_1.setLineWidth(5)
        self.narratorText_1.setMidLineWidth(1)
        self.narratorText_1.setWordWrap(True)
        self.narratorText_1.setObjectName("narratorText_1")
        self.narratorLayout.addWidget(self.narratorText_1)
        self.narratorText_2 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.narratorText_2.setFont(font)
        self.narratorText_2.setStyleSheet("font: 75 14pt \"Perpetua\";\n"
                                        "color: rgb(255, 254, 218);\n"
                                        "border-bottom-color: rgb(255, 0, 255);\n"
                                        "border-color: rgb(174, 119, 61);\n"
                                        "border-width: 3px;\n"
                                        "padding: 34px;\n"
                                        )
        self.narratorText_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.narratorText_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.narratorText_2.setLineWidth(5)
        self.narratorText_2.setMidLineWidth(1)
        self.narratorText_2.setWordWrap(True)
        self.narratorText_2.setObjectName("narratorText_2")
        self.narratorLayout.addWidget(self.narratorText_2)
        MainWindow.setCentralWidget(self.centralwidget)

        # self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def story_text(self, text: str):
        self.narratorText_1.setText(text)

    def fight_text(self, text: str):
        self.narratorText_2.setText(text)

    def set_image_left(self, image: str):
        self.left_image_landscape.setPixmap(QtGui.QPixmap(image))

    def set_image_right(self, image: str):
        self.right_image_portrait.setPixmap(QtGui.QPixmap(image))

    # def retranslateUi(self, MainWindow):
    #     _translate = QtCore.QCoreApplication.translate
    #     MainWindow.setWindowTitle(_translate("MainWindow", "HERAKLES"))
    #     self.Title_2.setText(_translate("MainWindow", "Adventure"))
    #     self.Title_1.setText(_translate("MainWindow", "HERAKLES"))
    #     self.startButton.setText(_translate("MainWindow", "START/CONTINUE"))
        
        
    #     self.narratorText_1.setText(_translate("MainWindow", "Ut aliquam purus sit amet luctus venenatis lectus. Velit euismod in pellentesque massa placerat duis ultricies lacus sed."))
    #     self.narratorText_2.setText(_translate("MainWindow", "Ut aliquam purus sit amet luctus venenatis lectus. Velit euismod in pellentesque massa placerat duis ultricies lacus sed.Ut aliquam purus sit amet luctus venenatis lectus. Velit euismod in pellentesque massa placerat duis ultricies lacus sed."))
        
    