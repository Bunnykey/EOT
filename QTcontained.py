# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import random
from igraph import *
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(958, 727)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.refreshname = QtGui.QPushButton(self.centralwidget)
        self.refreshname.setObjectName(_fromUtf8("refreshname"))
        self.horizontalLayout.addWidget(self.refreshname)
        self.playname = QtGui.QPushButton(self.centralwidget)
        self.playname.setObjectName(_fromUtf8("playname"))
        self.horizontalLayout.addWidget(self.playname)
        self.endname = QtGui.QPushButton(self.centralwidget)
        self.endname.setObjectName(_fromUtf8("endname"))
        self.horizontalLayout.addWidget(self.endname)
        self.gridLayout_4.addLayout(self.horizontalLayout, 5, 1, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.spinBoxyn4 = QtGui.QSpinBox(self.centralwidget)
        self.spinBoxyn4.setMinimum(-99)
        self.spinBoxyn4.setProperty("value", 3)
        self.spinBoxyn4.setObjectName(_fromUtf8("spinBoxyn4"))
        self.gridLayout_3.addWidget(self.spinBoxyn4, 3, 5, 1, 1)
        self.spinBoxyn3 = QtGui.QSpinBox(self.centralwidget)
        self.spinBoxyn3.setMinimum(-99)
        self.spinBoxyn3.setProperty("value", -1)
        self.spinBoxyn3.setObjectName(_fromUtf8("spinBoxyn3"))
        self.gridLayout_3.addWidget(self.spinBoxyn3, 3, 4, 1, 1)
        self.spinBoxyn2 = QtGui.QSpinBox(self.centralwidget)
        self.spinBoxyn2.setMinimum(-99)
        self.spinBoxyn2.setProperty("value", -1)
        self.spinBoxyn2.setObjectName(_fromUtf8("spinBoxyn2"))
        self.gridLayout_3.addWidget(self.spinBoxyn2, 3, 1, 1, 1)
        self.spinBoxnn1 = QtGui.QSpinBox(self.centralwidget)
        self.spinBoxnn1.setMinimum(-99)
        self.spinBoxnn1.setObjectName(_fromUtf8("spinBoxnn1"))
        self.gridLayout_3.addWidget(self.spinBoxnn1, 5, 2, 1, 1)
        self.spinBoxyn1 = QtGui.QSpinBox(self.centralwidget)
        self.spinBoxyn1.setMinimum(-99)
        self.spinBoxyn1.setProperty("value", 3)
        self.spinBoxyn1.setObjectName(_fromUtf8("spinBoxyn1"))
        self.gridLayout_3.addWidget(self.spinBoxyn1, 3, 0, 1, 1)
        self.spinBoxnn2 = QtGui.QSpinBox(self.centralwidget)
        self.spinBoxnn2.setMinimum(-99)
        self.spinBoxnn2.setObjectName(_fromUtf8("spinBoxnn2"))
        self.gridLayout_3.addWidget(self.spinBoxnn2, 5, 3, 1, 1)
        self.nnname = QtGui.QLabel(self.centralwidget)
        self.nnname.setObjectName(_fromUtf8("nnname"))
        self.gridLayout_3.addWidget(self.nnname, 4, 2, 1, 1)
        self.yn2name = QtGui.QLabel(self.centralwidget)
        self.yn2name.setObjectName(_fromUtf8("yn2name"))
        self.gridLayout_3.addWidget(self.yn2name, 2, 4, 1, 1)
        self.spinBoxyy2 = QtGui.QSpinBox(self.centralwidget)
        self.spinBoxyy2.setMinimum(-99)
        self.spinBoxyy2.setProperty("value", 2)
        self.spinBoxyy2.setObjectName(_fromUtf8("spinBoxyy2"))
        self.gridLayout_3.addWidget(self.spinBoxyy2, 1, 2, 1, 1)
        self.yn1name = QtGui.QLabel(self.centralwidget)
        self.yn1name.setObjectName(_fromUtf8("yn1name"))
        self.gridLayout_3.addWidget(self.yn1name, 2, 0, 1, 1)
        self.spinBoxyy1 = QtGui.QSpinBox(self.centralwidget)
        self.spinBoxyy1.setMinimum(-99)
        self.spinBoxyy1.setProperty("value", 2)
        self.spinBoxyy1.setObjectName(_fromUtf8("spinBoxyy1"))
        self.gridLayout_3.addWidget(self.spinBoxyy1, 1, 3, 1, 1)
        self.yyname = QtGui.QLabel(self.centralwidget)
        self.yyname.setObjectName(_fromUtf8("yyname"))
        self.gridLayout_3.addWidget(self.yyname, 0, 2, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 0, 3, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 2, 5, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_3.addWidget(self.label_4, 4, 3, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 4, 1, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.spinBox = QtGui.QSpinBox(self.centralwidget)
        self.spinBox.setProperty("value", 20)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.gridLayout.addWidget(self.spinBox, 4, 2, 1, 1)
        self.randomname = QtGui.QLabel(self.centralwidget)
        self.randomname.setAlignment(QtCore.Qt.AlignCenter)
        self.randomname.setObjectName(_fromUtf8("randomname"))
        self.gridLayout.addWidget(self.randomname, 4, 0, 1, 1)
        self.spinBoxno = QtGui.QSpinBox(self.centralwidget)
        self.spinBoxno.setProperty("value", 20)
        self.spinBoxno.setObjectName(_fromUtf8("spinBoxno"))
        self.gridLayout.addWidget(self.spinBoxno, 1, 2, 1, 1)
        self.yesnoname = QtGui.QLabel(self.centralwidget)
        self.yesnoname.setAlignment(QtCore.Qt.AlignCenter)
        self.yesnoname.setObjectName(_fromUtf8("yesnoname"))
        self.gridLayout.addWidget(self.yesnoname, 2, 0, 1, 1)
        self.yesname = QtGui.QLabel(self.centralwidget)
        self.yesname.setAlignment(QtCore.Qt.AlignCenter)
        self.yesname.setObjectName(_fromUtf8("yesname"))
        self.gridLayout.addWidget(self.yesname, 0, 0, 1, 1)
        self.horizontalSlider = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider.setProperty("value", 20)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.gridLayout.addWidget(self.horizontalSlider, 0, 1, 1, 1)
        self.horizontalSlider_2 = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider_2.setProperty("value", 20)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName(_fromUtf8("horizontalSlider_2"))
        self.gridLayout.addWidget(self.horizontalSlider_2, 1, 1, 1, 1)
        self.horizontalSlider_3 = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider_3.setProperty("value", 20)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName(_fromUtf8("horizontalSlider_3"))
        self.gridLayout.addWidget(self.horizontalSlider_3, 2, 1, 1, 1)
        self.spinBoxyesno = QtGui.QSpinBox(self.centralwidget)
        self.spinBoxyesno.setProperty("value", 20)
        self.spinBoxyesno.setObjectName(_fromUtf8("spinBoxyesno"))
        self.gridLayout.addWidget(self.spinBoxyesno, 2, 2, 1, 1)
        self.spinBoxyes = QtGui.QSpinBox(self.centralwidget)
        self.spinBoxyes.setProperty("value", 20)
        self.spinBoxyes.setObjectName(_fromUtf8("spinBoxyes"))
        self.gridLayout.addWidget(self.spinBoxyes, 0, 2, 1, 1)
        self.spinBoxlike = QtGui.QSpinBox(self.centralwidget)
        self.spinBoxlike.setProperty("value", 20)
        self.spinBoxlike.setObjectName(_fromUtf8("spinBoxlike"))
        self.gridLayout.addWidget(self.spinBoxlike, 3, 2, 1, 1)
        self.noname = QtGui.QLabel(self.centralwidget)
        self.noname.setAlignment(QtCore.Qt.AlignCenter)
        self.noname.setObjectName(_fromUtf8("noname"))
        self.gridLayout.addWidget(self.noname, 1, 0, 1, 1)
        self.likename = QtGui.QLabel(self.centralwidget)
        self.likename.setAlignment(QtCore.Qt.AlignCenter)
        self.likename.setObjectName(_fromUtf8("likename"))
        self.gridLayout.addWidget(self.likename, 3, 0, 1, 1)
        self.horizontalSlider_4 = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider_4.setProperty("value", 20)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName(_fromUtf8("horizontalSlider_4"))
        self.gridLayout.addWidget(self.horizontalSlider_4, 3, 1, 1, 1)
        self.horizontalSlider_5 = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider_5.setProperty("value", 20)
        self.horizontalSlider_5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_5.setObjectName(_fromUtf8("horizontalSlider_5"))
        self.gridLayout.addWidget(self.horizontalSlider_5, 4, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 1, 1, 1, 1)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.spinBoxlose = QtGui.QSpinBox(self.centralwidget)
        self.spinBoxlose.setProperty("value", 5)
        self.spinBoxlose.setObjectName(_fromUtf8("spinBoxlose"))
        self.gridLayout_5.addWidget(self.spinBoxlose, 1, 2, 1, 1)
        self.losename = QtGui.QLabel(self.centralwidget)
        self.losename.setObjectName(_fromUtf8("losename"))
        self.gridLayout_5.addWidget(self.losename, 1, 3, 1, 1)
        self.spinBoxwin = QtGui.QSpinBox(self.centralwidget)
        self.spinBoxwin.setProperty("value", 5)
        self.spinBoxwin.setObjectName(_fromUtf8("spinBoxwin"))
        self.gridLayout_5.addWidget(self.spinBoxwin, 1, 0, 1, 1)
        self.winname = QtGui.QLabel(self.centralwidget)
        self.winname.setObjectName(_fromUtf8("winname"))
        self.gridLayout_5.addWidget(self.winname, 1, 1, 1, 1)
        self.spinBoxround = QtGui.QSpinBox(self.centralwidget)
        self.spinBoxround.setProperty("value", 5)
        self.spinBoxround.setObjectName(_fromUtf8("spinBoxround"))
        self.gridLayout_5.addWidget(self.spinBoxround, 0, 0, 1, 1)
        self.roundname = QtGui.QLabel(self.centralwidget)
        self.roundname.setObjectName(_fromUtf8("roundname"))
        self.gridLayout_5.addWidget(self.roundname, 0, 1, 1, 1)
        self.mistakename = QtGui.QLabel(self.centralwidget)
        self.mistakename.setObjectName(_fromUtf8("mistakename"))
        self.gridLayout_5.addWidget(self.mistakename, 2, 0, 1, 1)
        self.spinBoxmistake = QtGui.QSpinBox(self.centralwidget)
        self.spinBoxmistake.setObjectName(_fromUtf8("spinBoxmistake"))
        self.gridLayout_5.addWidget(self.spinBoxmistake, 2, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_5.addWidget(self.label_5, 2, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_5, 5, 0, 1, 1)
        self.picturename = GraphicsLayoutWidget(self.centralwidget)
        self.picturename.setObjectName(_fromUtf8("picturename"))
        self.gridLayout_4.addWidget(self.picturename, 0, 0, 3, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 2, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem1, 0, 1, 1, 1)
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout_4.addWidget(self.textEdit, 4, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 958, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.endname.clicked.connect(self.ending)  ###추가한부분
        self.refreshname.clicked.connect(self.refreshing)
        self.playname.clicked.connect(self.playing)





        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBoxyes.setValue)
        QtCore.QObject.connect(self.horizontalSlider_2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBoxno.setValue)
        QtCore.QObject.connect(self.horizontalSlider_3, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBoxyesno.setValue)
        QtCore.QObject.connect(self.horizontalSlider_4, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBoxlike.setValue)
        QtCore.QObject.connect(self.spinBoxyy1, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBoxyy2.setValue)
        QtCore.QObject.connect(self.spinBoxyn2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBoxyn3.setValue)
        QtCore.QObject.connect(self.spinBoxyn1, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBoxyn4.setValue)
        QtCore.QObject.connect(self.spinBoxnn1, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBoxnn2.setValue)
        QtCore.QObject.connect(self.spinBoxwin, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBoxlose.setValue)
        QtCore.QObject.connect(self.horizontalSlider_5, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBox.setValue)
        QtCore.QObject.connect(self.spinBoxyy2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBoxyy1.setValue)
        QtCore.QObject.connect(self.spinBoxyn3, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBoxyn2.setValue)
        QtCore.QObject.connect(self.spinBoxyn4, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBoxyn1.setValue)
        QtCore.QObject.connect(self.spinBoxnn2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBoxnn1.setValue)
        QtCore.QObject.connect(self.spinBoxlose, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBoxwin.setValue)
        QtCore.QObject.connect(self.spinBoxyes, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.horizontalSlider.setValue)
        QtCore.QObject.connect(self.spinBoxno, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.horizontalSlider_2.setValue)
        QtCore.QObject.connect(self.spinBoxyesno, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.horizontalSlider_3.setValue)
        QtCore.QObject.connect(self.spinBoxlike, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.horizontalSlider_4.setValue)
        QtCore.QObject.connect(self.spinBox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.horizontalSlider_5.setValue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def ending(self):                                  ###추가한부분
        sys.exit()


    def playing(self):
        class Player(object):
            def __init__(self):
                self.score = 0

            def algorithm(self):
                raise NotImplementedError  ###하위 클래스에서 구현이 안되어있을 경우 에러 발생

        class OnlyHelper(Player):
            def __init__(self):
                Player.__init__(self)

            def algorithm(self):
                return True

        class OnlyBetrayer(Player):
            def __init__(self):
                Player.__init__(self)

            def algorithm(self):
                return False

        class ReactPlayer(Player):  ### 상대의 행동에 영향받는 플레이어의 클래스
            def __init__(self):
                Player.__init__(self)
                self.prevEnemyAction = True

            def update(self, input):
                raise NotImplementedError

        class Mirror(ReactPlayer):
            def __init__(self):
                ReactPlayer.__init__(self)

            def update(self, input):
                self.prevEnemyAction = input  ### 상대의 전번선택을 input 변수로 받아와서 prevEnemyAction에 저장

            def algorithm(self):
                return self.prevEnemyAction  ### prevEnemyAction을 따라서 행동함

        class Revenger(ReactPlayer):
            def __init__(self):
                ReactPlayer.__init__(self)

            def update(self, input):
                self.prevEnemyAction &= input  ### A &= B : only when A and B is True, A is True

            def algorithm(self):
                return self.prevEnemyAction

        class Randomer(Player):
            def __init__(self):
                Player.__init__(self)

            def algorithm(self):
                return bool(random.randint(0, 1))  ### bool타입 활용 (bool(1) = True, bool(0)= False))

        class Game(object):
            def __init__(self, PlayerTypes, Option):
                self.Playerlist = []
                self.option = Option
                self.PlayerClass = [OnlyHelper, OnlyBetrayer, Mirror, Revenger, Randomer]
                for i in range(0, 5):
                    for j in range(0, PlayerTypes[i]):
                        self.Playerlist.append(self.PlayerClass[i]())
                lineUp = []
                for i in range(0, self.Playerlist.__len__()):
                    for j in range(i + 1, self.Playerlist.__len__()):
                        lineUp.append((i, j))
                self.g = Graph(lineUp)

            class Option(object):
                def __init__(self, reward, rounds, leagueLoop):
                    self.rounds = rounds
                    self.reward = reward
                    self.leagueLoop = leagueLoop

            @staticmethod  # 호출된 클래스나 인스턴스에 대해 모르는 메소드
            def validate(A, B):
                params = [A, B]
                res = list(map(lambda x: x.algorithm(), params))
                for i in range(0, 2):
                    if type(params[i]) is ReactPlayer:
                        params[i].update(res[(i + 1) % 2])

                if res[0] and res[1]:  # 둘 다 협력
                    return 0
                elif not (res[0] or res[1]):  # 둘 다 배신
                    return 1
                elif res[1]:  # A 가  배신
                    return 2
                else:  # B 가  배신
                    return 3

            def Battle(self, A, B):
                result = Game.validate(A, B)
                if result == 0:
                    A.score += self.option.reward['BothHelp']
                    B.score += self.option.reward['BothHelp']
                elif result == 1:
                    A.score += self.option.reward['BothBetray']
                    B.score += self.option.reward['BothBetray']
                elif result == 2:
                    A.score += self.option.reward['BetrayBenefit']
                    B.score += self.option.reward['HelpPenalty']
                else:
                    A.score += self.option.reward['HelpPenalty']
                    B.score += self.option.reward['BetrayBenefit']

            def mutation(self):
                print("----------------------")
                self.Playerlist.sort(key=lambda x: x.score, reverse=True)
                for i in range(0, 5):
                    self.Playerlist.pop()
                for i in range(0, 5):
                    self.Playerlist.append(type(self.Playerlist[i])())

            def monitor(self):
                winnerList = []
                winnerCount = []
                #for i in self.Playerlist:
                    #print(i.score, type(i).__name__)
                for i in range(0, len(self.Playerlist)):
                    winnerList.append(str(type(self.Playerlist[i])))
                for i in self.PlayerClass:
                    winnerCount.append(winnerList.count(str(i)))
                return 'Remain number\n\nHELPman:{} \nREJECTman:{} \nimitator:{} \nrevenger:{} \nrandom:{}'.format(winnerCount[0],winnerCount[1],winnerCount[2],winnerCount[3],winnerCount[4])

            def scoreResetter(self):
                for i in self.Playerlist:
                    i.score = 0

            def league(self):
                playerlength = self.Playerlist.__len__()
                for i in range(0, playerlength):
                    for j in range(i + 1, playerlength):
                        for k in range(0, self.option.rounds):
                            self.Battle(self.Playerlist[i], self.Playerlist[j])
                            if (type(self.Playerlist[i]) is ReactPlayer):
                                self.Playerlist[i].update(True)
                            if (type(self.Playerlist[j]) is ReactPlayer):
                                self.Playerlist[j].update(True)
                self.mutation()
                self.scoreResetter()

            def leagueStart(self):
                for i in range(0, self.option.leagueLoop):
                    self.league()
                    self.visualize()

            def graphSetter(self):
                self.g.vs["player"] = list(map(lambda x: type(x).__name__, self.Playerlist))

            def visualize(self):
                gameInstance.graphSetter()
                myGraph = self.g
                layout = myGraph.layout_circle()  ## dim=2
                color_dict = {"Mirror": "green", "Randomer": "pink", "Revenger": "yellow", "OnlyBetrayer": "red",
                              "OnlyHelper": "blue"}
                graphic = plot(myGraph,
                               layout=layout,
                               bbox=(512, 512),
                               margin=16,
                               vertex_color=[color_dict[player] for player in myGraph.vs["player"]],
                               vertex_size=16)

        gameInstance = Game(PlayerTypes=[self.spinBoxyes.value(), self.spinBoxno.value(), self.spinBoxyesno.value(),
                                         self.spinBoxlike.value(), self.spinBox.value()],
                            Option=Game.Option(
                                reward={'BothBetray': self.spinBoxnn1.value(), 'BothHelp': self.spinBoxyy1.value(), 'BetrayBenefit': self.spinBoxyn1.value(), 'HelpPenalty': self.spinBoxyn2.value()},
                                rounds=1,
                                leagueLoop=self.spinBoxround.value()))

        gameInstance.leagueStart()  # 시작 버튼을 누르면 실행
        self.textEdit.setText(str(gameInstance.monitor()))  # 결과를 보고 싶습니다

    def refreshing(self):
        self.spinBoxyy1.setProperty("value", 2)
        self.spinBoxyy2.setProperty("value", 2)
        self.spinBoxyn1.setProperty("value", 3)
        self.spinBoxyn2.setProperty("value", -1)
        self.spinBoxyn3.setProperty("value", -1)
        self.spinBoxyn4.setProperty("value", 3)
        self.horizontalSlider_2.setProperty("value", 20)
        self.spinBoxno.setProperty("value", 20)
        self.horizontalSlider.setProperty("value", 20)
        self.horizontalSlider_3.setProperty("value", 20)
        self.spinBoxyesno.setProperty("value", 20)
        self.spinBoxyes.setProperty("value", 20)
        self.horizontalSlider_4.setProperty("value", 20)
        self.spinBoxlike.setProperty("value", 20)
        self.spinBoxround.setProperty("value", 5)
        self.spinBoxlose.setProperty("value", 5)
        self.spinBoxwin.setProperty("value", 5)





    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.refreshname.setText(_translate("MainWindow", "initialization", None))
        self.playname.setText(_translate("MainWindow", "play", None))
        self.endname.setText(_translate("MainWindow", "end", None))
        self.nnname.setText(_translate("MainWindow", "reject", None))
        self.yn2name.setText(_translate("MainWindow", "help", None))
        self.yn1name.setText(_translate("MainWindow", "reject", None))
        self.yyname.setText(_translate("MainWindow", "help", None))
        self.label.setText(_translate("MainWindow", "help", None))
        self.label_2.setText(_translate("MainWindow", "help", None))
        self.label_3.setText(_translate("MainWindow", "reject", None))
        self.label_4.setText(_translate("MainWindow", "reject", None))
        self.randomname.setText(_translate("MainWindow", "random", None))
        self.yesnoname.setText(_translate("MainWindow", " imitator", None))
        self.yesname.setText(_translate("MainWindow", "HELPman", None))
        self.noname.setText(_translate("MainWindow", "REJECTman", None))
        self.likename.setText(_translate("MainWindow", "revenger", None))
        self.losename.setText(_translate("MainWindow", "lose", None))
        self.winname.setText(_translate("MainWindow", "win", None))
        self.roundname.setText(_translate("MainWindow", "round", None))
        self.mistakename.setText(_translate("MainWindow", "mistake", None))
        self.label_5.setText(_translate("MainWindow", "%", None))

from pyqtgraph.widgets.GraphicsLayoutWidget import GraphicsLayoutWidget

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())