# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StartW.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(867, 419)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 10, 762, 497))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("FC.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 867, 18))
        self.menubar.setObjectName("menubar")
        self.menuACTIONS = QtWidgets.QMenu(self.menubar)
        self.menuACTIONS.setObjectName("menuACTIONS")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNEW = QtWidgets.QAction(MainWindow)
        self.actionNEW.setObjectName("actionNEW")
        self.actionOPEN = QtWidgets.QAction(MainWindow)
        self.actionOPEN.setObjectName("actionOPEN")
        self.actionEVALUATE = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE.setObjectName("actionEVALUATE")
        self.actionSAVE = QtWidgets.QAction(MainWindow)
        self.actionSAVE.setObjectName("actionSAVE")
        self.actionHELP = QtWidgets.QAction(MainWindow)
        self.actionHELP.setObjectName("actionHELP")
        self.menuACTIONS.addAction(self.actionNEW)
        self.menuACTIONS.addAction(self.actionOPEN)
        self.menuACTIONS.addAction(self.actionEVALUATE)
        self.menuACTIONS.addAction(self.actionSAVE)
        self.menuACTIONS.addAction(self.actionHELP)
        self.menubar.addAction(self.menuACTIONS.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #when menubar options are clicked        
        self.actionNEW.triggered.connect(self.neww)
        self.actionHELP.triggered.connect(self.helpw)
        self.actionOPEN.triggered.connect(self.openw)
        self.actionEVALUATE.triggered.connect(self.evaw)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "FANTASY CRICKET"))
        self.label_3.setText(_translate("MainWindow", "CLICK THE \"ACTIONS\" OPTION IN THE MENU BAR "))
        self.menuACTIONS.setTitle(_translate("MainWindow", "ACTIONS"))
        self.actionNEW.setText(_translate("MainWindow", "NEW"))
        self.actionNEW.setStatusTip(_translate("MainWindow", "Click this to create a new team"))
        self.actionOPEN.setText(_translate("MainWindow", "OPEN"))
        self.actionOPEN.setStatusTip(_translate("MainWindow", "Click this to open an existing team"))
        self.actionEVALUATE.setText(_translate("MainWindow", "EVALUATE"))
        self.actionEVALUATE.setStatusTip(_translate("MainWindow", "Click this to evaluate the score of your team"))
        self.actionSAVE.setText(_translate("MainWindow", "SAVE"))
        self.actionSAVE.setStatusTip(_translate("MainWindow", "Click this to save your team"))
        self.actionHELP.setText(_translate("MainWindow", "HELP"))
        self.actionHELP.setStatusTip(_translate("MainWindow", "Click this to know how the score is evaluated"))

    def helpw(self):
        #when help is clicked
        from Help import Ui_Dialog
        D = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(D)
        ret = D.exec()

    def evaw(self):
        #when evaluate is clicked
        from evaluate import Ui_Dialog
        D = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(D)
        ret = D.exec()

    def openw(self):
        #when open is clicked
        from Open import Ui_Dialog
        D = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(D)
        ret = D.exec()
        
        
    def neww(self):
        #when new is clicked
        from NewwFinal import Ui_Dialog
        D = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(D)
        ret = D.exec()

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
