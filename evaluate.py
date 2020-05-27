# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evaluate.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from CalcScore import pt
#connecting to database
s= sqlite3.connect('DATA.db')
c = s.cursor()
c.execute("SELECT name,players FROM TEAM ")
t = c.fetchall()
tL  = [l[0] for l in t]
pL = [l[1] for l in t]
c.execute("SELECT p,r,b,f,s,bow,rc,w,c,st,ro FROM MATCHDATA ")
d = c.fetchall()
#getting all the stats of the match in different lists
name =[]
for i in range(15):
    name.append(d[i][0]) #name
rs =[]
for i in range(15):
    rs.append(d[i][1]) #runs scored
bf =[]
for i in range(15):
    bf.append(d[i][2]) #balls faced
f =[]
for i in range(15):
    f.append(d[i][3]) #fours
s =[]
for i in range(15):
    s.append(d[i][4]) #sixes
bow =[]
for i in range(15):
    bow.append(d[i][5]) #overs bowled
rc =[]
for i in range(15):
    rc.append(d[i][6]) #runs conceded
w =[]
for i in range(15):
    w.append(d[i][7])#wickets taken
f =[]
for i in range(15):
    f.append(d[i][8]+d[i][9]+d[i][10])#fielding stats

points = []
for i in range(15):
    points.append(pt(rs[i],bf[i],f[i],s[i],w[i],bow[i],rc[i],f[i])) #points each player has earned

class Ui_Dialog(object):
    s=0
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 369)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Modern")
        font.setPointSize(11)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.team = QtWidgets.QListWidget(Dialog)
        self.team.setObjectName("team")
        self.gridLayout.addWidget(self.team, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.total = QtWidgets.QLineEdit(Dialog)
        self.total.setObjectName("total")
        self.horizontalLayout_2.addWidget(self.total)
        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.player = QtWidgets.QListWidget(Dialog)
        self.player.setObjectName("player")
        self.horizontalLayout_3.addWidget(self.player)
        self.point = QtWidgets.QListWidget(Dialog)
        self.point.setObjectName("point")
        self.horizontalLayout_3.addWidget(self.point)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)

        for i in range(len(tL)):
            self.team.addItem(tL[i])
        self.team.itemClicked.connect(self.fn)
        self.pushButton.clicked.connect(self.calc)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def calc(self):
        self.total.setText(str(self.s)) #setting the total points

    def fn(self,item): 
        p=""
        self.s=0
        for i in range(len(tL)):
            if tL[i]==item.text():
                p=pL[i]
        L =p.split(",")
        for i in range(11):
            self.player.addItem(L[i]) #adding players
        for i in range(15):
            for j in range(11):
                if name[i] == L[j]:
                    self.s = self.s+points[i] #summing points
                    
                    self.point.addItem(str(points[i])) #adding points
                    
            
                    
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "CLICK ON THE TEAM WHO\'S PERFORMANCE YOU WOULD LIKE TO EVALUATE"))
        self.label_2.setText(_translate("Dialog", "PLAYERS"))
        self.label_3.setText(_translate("Dialog", "POINTS"))
        self.pushButton.setText(_translate("Dialog", "CALCULATE"))
        self.label_4.setText(_translate("Dialog", "TOTAL POINTS - "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
