# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import random
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


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

class MplCanvas(FigureCanvas):
        def __init__(self,Game):
            self.gameInstance = Game
            self.fig = Figure()
            self.ax = self.fig.add_subplot(111)
            FigureCanvas.__init__(self,self.fig)
            FigureCanvas.setSizePolicy(self,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
            self.fig.add_axes((0,0,1,1))
            self.G = nx.cycle_graph(len(self.gameInstance.Playerlist))
            self.pos = nx.circular_layout(self.G)
            FigureCanvas.updateGeometry(self)
            
class matplotlibWidget(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.canvas = MplCanvas()
        self.vbl = QtGui.QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)

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
        self.spinBoxloop = QtGui.QSpinBox(self.centralwidget)
        self.spinBoxloop.setProperty("value", 5)
        self.spinBoxloop.setObjectName(_fromUtf8("spinBoxloop"))
        self.gridLayout_5.addWidget(self.spinBoxloop, 1, 2, 1, 1)
        self.loopname = QtGui.QLabel(self.centralwidget)
        self.loopname.setObjectName(_fromUtf8("loopname"))
        self.gridLayout_5.addWidget(self.loopname, 1, 3, 1, 1)
        self.spinBoxmutate = QtGui.QSpinBox(self.centralwidget)
        self.spinBoxmutate.setProperty("value", 5)
        self.spinBoxmutate.setObjectName(_fromUtf8("spinBoxmutate"))
        self.gridLayout_5.addWidget(self.spinBoxmutate, 1, 0, 1, 1)
        self.mutatename = QtGui.QLabel(self.centralwidget)
        self.mutatename.setObjectName(_fromUtf8("mutatename"))
        self.gridLayout_5.addWidget(self.mutatename, 1, 1, 1, 1)
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
        self.picturename = matplotlibWidget(self.centralwidget)
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

        self.endname.clicked.connect(self.ending)
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
        QtCore.QObject.connect(self.horizontalSlider_5, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBox.setValue)
        QtCore.QObject.connect(self.spinBoxyy2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBoxyy1.setValue)
        QtCore.QObject.connect(self.spinBoxyn3, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBoxyn2.setValue)
        QtCore.QObject.connect(self.spinBoxyn4, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBoxyn1.setValue)
        QtCore.QObject.connect(self.spinBoxnn2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBoxnn1.setValue)
        QtCore.QObject.connect(self.spinBoxyes, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.horizontalSlider.setValue)
        QtCore.QObject.connect(self.spinBoxno, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.horizontalSlider_2.setValue)
        QtCore.QObject.connect(self.spinBoxyesno, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.horizontalSlider_3.setValue)
        QtCore.QObject.connect(self.spinBoxlike, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.horizontalSlider_4.setValue)
        QtCore.QObject.connect(self.spinBox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.horizontalSlider_5.setValue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def ending(self):
        sys.exit()


    def playing(self):
        ####################################
        # One liter americano with 4 shots #
        #  and bunch of lambda sandwiches  #
        ####################################

        class Player(object):
            def __init__(self):
                self.score = 0
                self.friendKey = None

            def algorithm(self):
                raise NotImplementedError  ###If not implemented, return Error

            def scoreReset(self):
                self.score = 0
            @staticmethod
            def setFriends(PlayerA,PlayerB):
                PlayerA.friendKey=PlayerB.friendKey=str(hash(PlayerA))+str(hash(PlayerB)) ### Nice code : friends implemented, never used.

            @staticmethod
            def areTheyFriends(match):
                return (match[0].friendKey==match[1].friendKey) and (match[0].friendKey!=None) ### Nice code : friends implemented, never used.

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

        class ReactPlayer(Player):  ### Players who react
            def __init__(self):
                Player.__init__(self)
                self.prevEnemyAction = True

            def resetPrevEnemyAction(self):
                self.prevEnemyAction = True

            def update(self, input):
                raise NotImplementedError

        class Mirror(ReactPlayer):
            def __init__(self):
                ReactPlayer.__init__(self)

            def update(self, input):
                self.prevEnemyAction = input

            def algorithm(self):
                return self.prevEnemyAction  ### prevEnemyAction = my turn action

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
                return random.choice([True, False])  ### Do you know random?

        class Game(object):
            def __init__(self, PlayerTypes, Option):
                self.Playerlist = []
                self.option = Option
                self.PlayerClass = [OnlyHelper, OnlyBetrayer, Mirror, Revenger, Randomer]
                for i in range(5):
                    for j in range(PlayerTypes[i]):
                        self.Playerlist.append(self.PlayerClass[i]()) ### Type() = instance
                self.lineUp = [] ## making league = graph data structure
                for i in range(len(self.Playerlist)):
                    for j in range(i + 1, len(self.Playerlist)): ### Core of league
                        self.lineUp.append((i, j))
                self.visualizer = Visualizer(self)

            class Option(object):
                def __init__(self, reward, rounds, leagueLoop,mutationWeight,mistake):
                    self.rounds = rounds
                    self.reward = [(reward['BothBetray'],reward['BothBetray']),
                        (reward['HelpPenalty'],reward['BetrayBenefit']),
                        (reward['BetrayBenefit'],reward['HelpPenalty']),  ### list(tuple(dict))
                        (reward['BothHelp'],reward['BothHelp'])]
                    self.leagueLoop = leagueLoop
                    self.mutationWeight=mutationWeight
                    self.mistake = mistake/100.0

            @staticmethod
            def mistakeActions(resultOfAlgorithm,missRate):
                return not (resultOfAlgorithm ^ (random.uniform(0,1)>missRate))  # Alogrithm XNOR { Pr(True) = (1-missRate) }
                
            @staticmethod  #methods that are bound to a class rather than its object
            def Validate(match,mistake):
                if Player.areTheyFriends(match): # match = league tuples of instances
                    return 3
                result = map(lambda x: Game.mistakeActions(x.algorithm(),mistake), match) # result of [A.algorithm, B.algorithm] + one more thing(error)
                for i in range(2):
                    if isinstance(match[i],ReactPlayer):
                        match[i].update(result[(i + 1) % 2])
                return int(result[0])+(int(result[1])*2)

            def Battle(self, match):
                result = Game.Validate(match,self.option.mistake)
                for i in range(2):
                    match[i].score+= self.option.reward[result][i]

            @staticmethod
            def getNRandomIndexesOfItemsFromList(inputList,targetValue,pickAmount):
                return random.sample(map(lambda y:inputList.index(y),filter(lambda x:x.score==targetValue,inputList)),pickAmount)            

            def mutation(self):
                self.Playerlist.sort(key=lambda x: x.score, reverse=True)  ### random elimination of identical scorers
                valueCounter = (lambda fromList,targetValue:sum(x.score==targetValue for x in fromList))

                minValue = min(map(lambda x:x.score,self.Playerlist))
                minCount = valueCounter(self.Playerlist,minValue)

                maxValue = max(map(lambda x:x.score,self.Playerlist))
                maxCount = valueCounter(self.Playerlist,maxValue)
                
                if minCount>self.option.mutationWeight:
                    minlist = Game.getNRandomIndexesOfItemsFromList(self.Playerlist,minValue,self.option.mutationWeight)
                    minlist.sort(key=lambda x:x, reverse=True)
                    for i in minlist:
                        self.Playerlist.pop(i-minlist.index(i))
                else:
                    for i in range(self.option.mutationWeight):
                        self.Playerlist.pop()
                if maxCount>self.option.mutationWeight:
                    maxlist = Game.getNRandomIndexesOfItemsFromList(self.Playerlist,maxValue,self.option.mutationWeight)
                    for i in maxlist:
                        self.Playerlist.append(type(self.Playerlist[i])())
                else:
                    for i in range(self.option.mutationWeight):
                        self.Playerlist.append(type(self.Playerlist[i])())
                
            def printPlayerScores(self):
                print '\n'.join(str(s) for s in map(lambda x:(type(x).__name__,x.score),self.Playerlist))
            #don't touch, it's magic
            def monitor(self):
                #print('\n'.join(str(p) for p in  map(lambda x:(x.__name__,sum(isinstance(y,x) for y in self.Playerlist)),self.PlayerClass)))
                return map(lambda x:(x.__name__,sum(isinstance(y,x) for y in self.Playerlist)),self.PlayerClass)

            def league(self):
                for i in self.lineUp:
                    for n in range(self.option.rounds):
                        self.Battle(map(lambda x:self.Playerlist[x],i))
                    for j in range(2):
                        if isinstance(self.Playerlist[i[j]],ReactPlayer):
                            self.Playerlist[i[j]].resetPrevEnemyAction()
                self.mutation()
                #self.printPlayerScores()
                map(lambda x: x.scoreReset(), self.Playerlist)

            def leagueStart(self):
                for i in range(self.option.leagueLoop):
                    plt.pause(0.1)
                    self.league()
                    self.visualizer.updateData()
                    plt.draw()

        class Visualizer:
            def __init__(self,Game):
                self.gameInstance = Game
                self.G = nx.cycle_graph(len(self.gameInstance.Playerlist))
                self.pos = nx.circular_layout(self.G)
                cf = plt.figure(figsize=(1,1),dpi=512)
                cf.add_axes((0,0,1,1))
                self.color_dict = {
                    "Mirror": "green",
                    "Randomer": "pink",
                    "Revenger":"yellow",
                    "OnlyBetrayer":"red",
                    "OnlyHelper":"blue"}
                for i in self.G.edges():
                    self.G[i[0]][i[1]]['draw'] = nx.draw_networkx_edges(self.G,self.pos,edgelist=[i],alpha=0.5,arrows=False,width=1)
                self.updateData()

            def updateData(self):
                for j in range(len(self.gameInstance.Playerlist)):
                    self.G.node[j]['draw'] = nx.draw_networkx_nodes(self.G,self.pos,nodelist=[j],with_labels=False,node_size=10,node_color=self.color_dict[type(self.gameInstance.Playerlist[j]).__name__])
            
        gameInstance = Game(
            PlayerTypes=[self.spinBoxyes.value(), self.spinBoxno.value(), self.spinBoxyesno.value(), self.spinBoxlike.value(), self.spinBox.value()],
                Option=Game.Option(
                    reward={
                        'BothBetray': self.spinBoxnn1.value(),
                        'BothHelp': self.spinBoxyy1.value(),
                        'BetrayBenefit': self.spinBoxyn1.value(),
                        'HelpPenalty': self.spinBoxyn2.value()},
                    rounds=self.spinBoxround.value(),
                    leagueLoop=self.spinBoxloop.value(),
                    mutationWeight=self.spinBoxmutate.value(),
                    mistake=self.spinBoxmistake.value()))
        #Verifier.verify()
        gameInstance.leagueStart()
        #gameInstance.monitor() ##shows instance name
        self.textEdit.setText(str(gameInstance.monitor()))  ###??

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
        self.spinBox.setProperty("value", 20)
        self.horizontalSlider_4.setProperty("value", 20)
        self.spinBoxlike.setProperty("value", 20)
        self.spinBoxround.setProperty("value", 5)
        self.spinBoxloop.setProperty("value", 5)
        self.spinBoxmutate.setProperty("value", 5)
        self.spinBoxmistake.setProperty("value",0)




    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.refreshname.setText(_translate("MainWindow", "initialization", None))
        self.playname.setText(_translate("MainWindow", "play", None))
        self.endname.setText(_translate("MainWindow", "end", None))
        self.nnname.setText(_translate("MainWindow", "betray", None))
        self.yn2name.setText(_translate("MainWindow", "help", None))
        self.yn1name.setText(_translate("MainWindow", "betray", None))
        self.yyname.setText(_translate("MainWindow", "help", None))
        self.label.setText(_translate("MainWindow", "help", None))
        self.label_2.setText(_translate("MainWindow", "help", None))
        self.label_3.setText(_translate("MainWindow", "betray", None))
        self.label_4.setText(_translate("MainWindow", "betary", None))
        self.randomname.setText(_translate("MainWindow", "Randomer", None))
        self.yesnoname.setText(_translate("MainWindow", "Mirror", None))
        self.yesname.setText(_translate("MainWindow", "OnlyHelper", None))
        self.noname.setText(_translate("MainWindow", "OnlyBetrayer", None))
        self.likename.setText(_translate("MainWindow", "Revenger", None))
        self.loopname.setText(_translate("MainWindow", "loop", None))
        self.mutatename.setText(_translate("MainWindow", "mutation", None))
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