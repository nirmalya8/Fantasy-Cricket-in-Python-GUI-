# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewwFinal.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
s = sqlite3.connect('DATA.db')
c=s.cursor()
c.execute("SELECT Player,Price,Type FROM STATT")
t=c.fetchall()
playerlist = [l[0] for l in t] #list of players
pricelist =[l[1] for l in t]  #list of their prices
typelist = [l[2] for l in t]  #list of their categories
c.execute("SELECT name FROM TEAM")
t=c.fetchall()
teamlist = [l[0] for l in t] #list of existing teams

class Ui_Dialog(object):
    #setting up counters
    batc=0
    bowc=0
    arc=0
    wkc=0
    totc=0
    pa=1200
    pu=0
    pl=""
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(518, 433)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.save = QtWidgets.QPushButton(Dialog)
        self.save.setObjectName("save")
        self.gridLayout.addWidget(self.save, 6, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.team1 = QtWidgets.QLineEdit(Dialog)
        self.team1.setObjectName("team1")
        self.horizontalLayout_6.addWidget(self.team1)
        self.gridLayout.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_9.addWidget(self.label_16)
        self.pointsa_2 = QtWidgets.QLineEdit(Dialog)
        self.pointsa_2.setObjectName("pointsa_2")
        self.horizontalLayout_9.addWidget(self.pointsa_2)
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_9.addWidget(self.label_17)
        self.pointsu_2 = QtWidgets.QLineEdit(Dialog)
        self.pointsu_2.setObjectName("pointsu_2")
        self.horizontalLayout_9.addWidget(self.pointsu_2)
        self.gridLayout.addLayout(self.horizontalLayout_9, 4, 0, 1, 1)
        self.MB = QtWidgets.QLineEdit(Dialog)
        self.MB.setObjectName("MB")
        self.gridLayout.addWidget(self.MB, 8, 0, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.available_2 = QtWidgets.QListWidget(Dialog)
        self.available_2.setObjectName("available_2")
        self.horizontalLayout_10.addWidget(self.available_2)
        self.selected_2 = QtWidgets.QListWidget(Dialog)
        self.selected_2.setObjectName("selected_2")
        self.horizontalLayout_10.addWidget(self.selected_2)
        self.gridLayout.addLayout(self.horizontalLayout_10, 5, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_7.addWidget(self.label_11)
        self.bat_2 = QtWidgets.QLineEdit(Dialog)
        self.bat_2.setObjectName("bat_2")
        self.horizontalLayout_7.addWidget(self.bat_2)
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_7.addWidget(self.label_12)
        self.bow_2 = QtWidgets.QLineEdit(Dialog)
        self.bow_2.setObjectName("bow_2")
        self.horizontalLayout_7.addWidget(self.bow_2)
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_7.addWidget(self.label_13)
        self.wk_2 = QtWidgets.QLineEdit(Dialog)
        self.wk_2.setObjectName("wk_2")
        self.horizontalLayout_7.addWidget(self.wk_2)
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_7.addWidget(self.label_14)
        self.ar_2 = QtWidgets.QLineEdit(Dialog)
        self.ar_2.setObjectName("ar_2")
        self.horizontalLayout_7.addWidget(self.ar_2)
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_7.addWidget(self.label_15)
        self.tot_2 = QtWidgets.QLineEdit(Dialog)
        self.tot_2.setObjectName("tot_2")
        self.horizontalLayout_7.addWidget(self.tot_2)
        self.gridLayout.addLayout(self.horizontalLayout_7, 2, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.batrb_2 = QtWidgets.QRadioButton(Dialog)
        self.batrb_2.setObjectName("batrb_2")
        self.horizontalLayout_8.addWidget(self.batrb_2)
        self.bowrb_2 = QtWidgets.QRadioButton(Dialog)
        self.bowrb_2.setObjectName("bowrb_2")
        self.horizontalLayout_8.addWidget(self.bowrb_2)
        self.wkrb_2 = QtWidgets.QRadioButton(Dialog)
        self.wkrb_2.setObjectName("wkrb_2")
        self.horizontalLayout_8.addWidget(self.wkrb_2)
        self.arrb_2 = QtWidgets.QRadioButton(Dialog)
        self.arrb_2.setObjectName("arrb_2")
        self.horizontalLayout_8.addWidget(self.arrb_2)
        self.gridLayout.addLayout(self.horizontalLayout_8, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 7, 0, 1, 1)

        #setting the initial counters
        self.bat_2.setText(str(self.batc))
        self.bow_2.setText(str(self.bowc))
        self.ar_2.setText(str(self.arc))
        self.wk_2.setText(str(self.wkc))
        self.tot_2.setText(str(self.totc))
        self.pointsa_2.setText(str(self.pa))
        self.pointsu_2.setText(str(self.pu))

        #when radio buttons are toggled
        self.batrb_2.toggled.connect(self.b)
        self.bowrb_2.toggled.connect(self.bo)
        self.wkrb_2.toggled.connect(self.w)
        self.arrb_2.toggled.connect(self.a)

        #when items in the lists are clicked
        self.available_2.itemClicked.connect(self.removea)
        self.selected_2.itemClicked.connect(self.removes)

        #when save pushbutton is clicked
        self.save.clicked.connect(self.saveit) 
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def removea(self,item):
        #selects player into the team
        self.available_2.takeItem(self.available_2.row(item))
        self.selected_2.addItem(item.text())
        c=""
        for i in range(len(playerlist)):
            if item.text() == playerlist[i]:
                self.pu = self.pu+pricelist[i]
                self.pa = self.pa-pricelist[i]
                c = typelist[i]
                break
        if c == 'BAT':
            self.batc = self.batc+1
        if c == 'BOW':
            self.bowc = self.bowc+1
        if c == 'AR':
            self.arc = self.arc+1
        if c == 'WK':
            self.wkc = self.wkc+1

        self.totc = self.totc+1
        
        self.bat_2.setText(str(self.batc))
        self.bow_2.setText(str(self.bowc))
        self.ar_2.setText(str(self.arc))
        self.wk_2.setText(str(self.wkc))
        self.tot_2.setText(str(self.totc))
        self.pointsa_2.setText(str(self.pa))
        self.pointsu_2.setText(str(self.pu))

    def removes(self,item):
        #deselects the player from the team
        print("e")
        self.selected_2.takeItem(self.selected_2.row(item))
        self.available_2.addItem(item.text())
        
        
        c=""
        for i in range(len(playerlist)):
            if item.text() == playerlist[i]:
                self.pu = self.pu-pricelist[i]
                self.pa = self.pa+pricelist[i]
                c = typelist[i]
                break
        if c == 'BAT':
            self.batc = self.batc-1
        if c == 'BOW':
            self.bowc = self.bowc-1
        if c == 'AR':
            self.arc = self.arc-1
        if c == 'WK':
            self.wkc = self.wkc-1
        self.totc = self.totc-1
            
        
        self.bat_2.setText(str(self.batc))
        self.bow_2.setText(str(self.bowc))
        self.ar_2.setText(str(self.arc))
        self.wk_2.setText(str(self.wkc))
        self.tot_2.setText(str(self.totc))
        self.pointsa_2.setText(str(self.pa))
        self.pointsu_2.setText(str(self.pu))

    def saveit(self):
        #saves the team
        print("entered")
        tn = self.team1.text()
        f=True
        if self.totc>11:
            print("playernocheck>")
            f = False
            self.MB.setText(" MORE THAN 11 PLAYERS REMOVE SOME PLAYERS AND PRESS SAVE")
        for i in range(len(teamlist)):
            print("namecheck")
            if teamlist[i]== tn:
                print("namefalse")
                f = False
                self.MB.setText(" TEAM NAME ALREADY EXISTS, ENTER AGAIN AND PRESS SAVE")
                
        
        if self.totc<11:
            f = False
            self.MB.setText(" LESS THAN 11 PLAYERS ADD SOME PLAYERS AND PRESS SAVE")
        if self.pa<0:
            f = False
            self.MB.setText(" MORE THAN 1200 POINTS USED. KEEP POINTS TO LESS THAN 1200 AND PRESS SAVE")
        
        if f == True:
            p=""
            items = []
            for index in range(self.selected_2.count()):
                items.append(self.selected_2.item(index).text()) 
            for i in range(11):
                p = p+items[i]+","
            c.execute('''INSERT INTO TEAM (name,players,value) VALUES (?, ?, ?)''',(tn, p, self.pu))
            s.commit()
            self.MB.setText(" SAVED SUCCESSFULLY")
                
        
        
    #adding players to available list
    def b(self):
        self.available_2.clear()
        c.execute("SELECT Player FROM STATT WHERE Type ='BAT'")
        data = c.fetchall()
        for player in data: 
            self.available_2.addItem(player[0])

    def bo(self):
        self.available_2.clear()
        c.execute("SELECT Player FROM STATT WHERE Type ='BOW'")
        data = c.fetchall()
        for player in data: 
            self.available_2.addItem(player[0])

    def w(self):
        self.available_2.clear()
        c.execute("SELECT Player FROM STATT WHERE Type ='WK'")
        data = c.fetchall()
        for player in data: 
            self.available_2.addItem(player[0])
            
    def a(self):
        self.available_2.clear()
        c.execute("SELECT Player FROM STATT WHERE Type ='AR'")
        data = c.fetchall()
        for player in data: 
            self.available_2.addItem(player[0])

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.save.setText(_translate("Dialog", "SAVE"))
        self.label_10.setText(_translate("Dialog", "TEAM NAME"))
        self.label_16.setText(_translate("Dialog", "POINTS AVAILABLE -"))
        self.label_17.setText(_translate("Dialog", "POINTS USED  -"))
        self.label.setText(_translate("Dialog", "ENTER TEAM NAME AND SELECT THE PLAYERS"))
        self.label_11.setText(_translate("Dialog", "BAT - "))
        self.label_12.setText(_translate("Dialog", "BOW - "))
        self.label_13.setText(_translate("Dialog", "WK -"))
        self.label_14.setText(_translate("Dialog", "AR - "))
        self.label_15.setText(_translate("Dialog", "TOTAL -"))
        self.batrb_2.setText(_translate("Dialog", "BAT"))
        self.bowrb_2.setText(_translate("Dialog", "BOW"))
        self.wkrb_2.setText(_translate("Dialog", "WK"))
        self.arrb_2.setText(_translate("Dialog", "AR"))
        self.label_2.setText(_translate("Dialog", "MESSAGE BOX"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
