# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sidebar.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1464, 940)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(90, 90))
        self.label.setMaximumSize(QSize(90, 90))
        self.label.setPixmap(QPixmap(u":/icon/icon/EgisLogo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.console_button_1 = QPushButton(self.icon_only_widget)
        self.console_button_1.setObjectName(u"console_button_1")
        icon = QIcon()
        icon.addFile(u":/icon/images/icons/cil-browser.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.console_button_1.setIcon(icon)
        self.console_button_1.setIconSize(QSize(20, 20))
        self.console_button_1.setCheckable(True)
        self.console_button_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.console_button_1)

        self.code_button_1 = QPushButton(self.icon_only_widget)
        self.code_button_1.setObjectName(u"code_button_1")
        icon1 = QIcon()
        icon1.addFile(u":/icon/images/icons/cil-file.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.code_button_1.setIcon(icon1)
        self.code_button_1.setIconSize(QSize(20, 20))
        self.code_button_1.setCheckable(True)
        self.code_button_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.code_button_1)

        self.setting_button_1 = QPushButton(self.icon_only_widget)
        self.setting_button_1.setObjectName(u"setting_button_1")
        icon2 = QIcon()
        icon2.addFile(u":/icon/images/icons/cil-settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.setting_button_1.setIcon(icon2)
        self.setting_button_1.setIconSize(QSize(20, 20))
        self.setting_button_1.setCheckable(True)
        self.setting_button_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.setting_button_1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 582, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.full_menu_widget = QWidget(self.centralwidget)
        self.full_menu_widget.setObjectName(u"full_menu_widget")
        self.verticalLayout_4 = QVBoxLayout(self.full_menu_widget)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.full_menu_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(120, 120))
        self.label_2.setMaximumSize(QSize(120, 120))
        self.label_2.setPixmap(QPixmap(u":/icon/icon/EgisLogo.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.console_button_2 = QPushButton(self.full_menu_widget)
        self.console_button_2.setObjectName(u"console_button_2")
        self.console_button_2.setIcon(icon)
        self.console_button_2.setIconSize(QSize(14, 14))
        self.console_button_2.setCheckable(True)
        self.console_button_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.console_button_2)

        self.code_button_2 = QPushButton(self.full_menu_widget)
        self.code_button_2.setObjectName(u"code_button_2")
        self.code_button_2.setIcon(icon1)
        self.code_button_2.setIconSize(QSize(14, 14))
        self.code_button_2.setCheckable(True)
        self.code_button_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.code_button_2)

        self.setting_button_2 = QPushButton(self.full_menu_widget)
        self.setting_button_2.setObjectName(u"setting_button_2")
        self.setting_button_2.setIcon(icon2)
        self.setting_button_2.setIconSize(QSize(14, 14))
        self.setting_button_2.setCheckable(True)
        self.setting_button_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.setting_button_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 555, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.gridLayout.addWidget(self.full_menu_widget, 0, 1, 1, 1)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 0))
        self.verticalLayout_5 = QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.header_widget = QWidget(self.widget_3)
        self.header_widget.setObjectName(u"header_widget")
        self.horizontalLayout_3 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.header_widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 0))
        icon3 = QIcon()
        icon3.addFile(u":/icon/icon/menu-4-32.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(1174, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addWidget(self.header_widget)

        self.stackedWidget = QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.console_page = QWidget()
        self.console_page.setObjectName(u"console_page")
        self.gridLayout_3 = QGridLayout(self.console_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.console_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.console_page)
        self.code_page = QWidget()
        self.code_page.setObjectName(u"code_page")
        self.gridLayout_2 = QGridLayout(self.code_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(self.code_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.code_page)
        self.setting_page = QWidget()
        self.setting_page.setObjectName(u"setting_page")
        self.gridLayout_4 = QGridLayout(self.setting_page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_5 = QLabel(self.setting_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.setting_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.console_button_1.toggled.connect(self.console_button_2.setChecked)
        self.code_button_1.toggled.connect(self.code_button_2.setChecked)
        self.setting_button_1.toggled.connect(self.setting_button_2.setChecked)
        self.console_button_2.toggled.connect(self.console_button_1.setChecked)
        self.code_button_2.toggled.connect(self.code_button_1.setChecked)
        self.setting_button_2.toggled.connect(self.setting_button_1.setChecked)
        self.pushButton.toggled.connect(self.icon_only_widget.setVisible)
        self.pushButton.toggled.connect(self.full_menu_widget.setHidden)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.console_button_1.setText("")
        self.code_button_1.setText("")
        self.setting_button_1.setText("")
        self.label_2.setText("")
        self.console_button_2.setText(QCoreApplication.translate("MainWindow", u"Console   ", None))
        self.code_button_2.setText(QCoreApplication.translate("MainWindow", u"Code", None))
        self.setting_button_2.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.pushButton.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"console", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"code", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"setting", None))
    # retranslateUi

