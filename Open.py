# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Open.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
s= sqlite3.connect('DATA.db')
c = s.cursor()
c.execute("SELECT name,players FROM TEAM ")
t = c.fetchall()
tL  = [l[0] for l in t] #teams list
pL = [l[1] for l in t] #players list
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(392, 245)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setItalic(True)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.teamnames = QtWidgets.QListWidget(Dialog)
        self.teamnames.setObjectName("teamnames")
        self.verticalLayout.addWidget(self.teamnames)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.playerlist = QtWidgets.QListWidget(Dialog)
        self.playerlist.setObjectName("playerlist")
        self.verticalLayout.addWidget(self.playerlist)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        for i in range(len(tL)):
            #adding teams
            self.teamnames.addItem(tL[i])

        #on click of a team
        self.teamnames.itemClicked.connect(self.dispP)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def dispP(self,item):
        p=""
        for i in range(len(tL)):
            if tL[i]==item.text():
                p=pL[i]
        L =p.split(",")
        for i in range(11):
            #adding players of the team
            self.playerlist.addItem(L[i])

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "CLICK ON THE NAME OF THE TEAM YOU WANT TO OPEN"))
        self.label_2.setText(_translate("Dialog", "PLAYER LIST"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
