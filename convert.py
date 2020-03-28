# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'convert.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from pydub import AudioSegment
from pydub.playback import play
from pathlib import Path
from PyQt5.QtWidgets import QMessageBox 


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(583, 294)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 40, 141, 61))
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 50, 171, 41))
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 150, 141, 51))
        self.pushButton_2.setObjectName("pushButton_2")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 150, 151, 41))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 583, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Browse your file"))
        self.pushButton.clicked.connect(self.open_box)

        self.label.setText(_translate("MainWindow", "No File Selected"))

        self.pushButton_2.setText(_translate("MainWindow", "Convert To MP3"))
        self.pushButton_2.clicked.connect(self.convert_file)

    
    def open_box(self):
        self.name = QtWidgets.QFileDialog.getOpenFileName(None,'OpenFile',"")
        global path,fil,change
        path = self.name[0]
        fil = Path(path).name
        self.label.setText(fil)
        print(path)
        change = path.replace(".wav",".mp3")
        
        
    def convert_file(self):
        global n
        try:
            self.org = AudioSegment.from_file(path)
            self.org.export(out_f=change,format="mp3")
            n = Path(change).name
            self.label_2.setText(n)
        except:
            msg = QMessageBox()
            msg.setWindowTitle("Error Ocurred")
            msg.setText("Audio File not slected")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Retry)
            x = msg.exec_()
            # self.label_2.setText("Please select an audio File")
        # print("success")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
