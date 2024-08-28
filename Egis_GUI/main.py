import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import Slot, QFile, QTextStream
from sidebar_ui import Ui_MainWindow
from PySide6.QtGui import QIcon



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.console_button_1.setChecked(True)

    #Gui Setting
        self.setWindowTitle("Eigs")
        self.setWindowIcon(QIcon("./icon/EgisLogo_app.png"))
        # self.setGeometry(100,100,800,600)

    #Connect Button to switch to differnet pages
        self.ui.console_button_1.clicked.connect(self.switch_to_console_btn_1)
        self.ui.console_button_2.clicked.connect(self.switch_to_console_btn_2)
        self.ui.code_button_1.clicked.connect(self.switch_to_code_btn_1)
        self.ui.code_button_2.clicked.connect(self.switch_to_code_btn2)
        self.ui.setting_button_1.clicked.connect(self.switch_to_setting_btn_1)
        self.ui.setting_button_2.clicked.connect(self.switch_to_setting_btn_2)

    # functions for changing sidebar page
    def switch_to_console_btn_1(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    def switch_to_console_btn_2(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    def switch_to_code_btn_1(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    def switch_to_code_btn2(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    def switch_to_setting_btn_1(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    def switch_to_setting_btn_2(self):
        self.ui.stackedWidget.setCurrentIndex(2)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    ## loading style file
    with open("style.qss", "r") as style_file:
        style_str = style_file.read()
    app.setStyleSheet(style_str)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())