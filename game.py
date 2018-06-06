#-*- coding: utf-8 -*-

####################################
# Please! Do not try this at home. #
####################################

import random
import networkx as nx
import matplotlib.pyplot as plt

class Player(object):
    def __init__(self):
        self.score = 0
        self.friendKey = None

    def algorithm(self):
        raise NotImplementedError  ###하위 클래스에서 구현이 안되어있을 경우 에러 발생

    def scoreReset(self):
        self.score = 0
    @staticmethod
    def setFriends(PlayerA,PlayerB):
        PlayerA.friendKey=PlayerB.friendKey=str(hash(PlayerA))+str(hash(PlayerB))

    #guarantees NoneCheck
    @staticmethod
    def areTheyFriends(match):
        return (match[0].friendKey==match[1].friendKey) and (match[0].friendKey!=None)

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
        for i in range(5):
            for j in range(PlayerTypes[i]):
                self.Playerlist.append(self.PlayerClass[i]())

        self.lineUp = []
        for i in range(len(self.Playerlist)):
            for j in range(i + 1, len(self.Playerlist)):
                self.lineUp.append((i, j))
        #print(self.lineUp)

    class Option(object):
        def __init__(self, reward, rounds, leagueLoop,mutationWeight):
            self.rounds = rounds
            self.reward = [(reward['BothBetray'],reward['BothBetray']),
                (reward['HelpPenalty'],reward['BetrayBenefit']),
                (reward['BetrayBenefit'],reward['HelpPenalty']),
                (reward['BothHelp'],reward['BothHelp'])]
            self.leagueLoop = leagueLoop
            self.mutationWeight=mutationWeight

    @staticmethod  #호출된 클래스나 인스턴스에 대해 모르는 메소드
    def Validate(match):
        if Player.areTheyFriends(match):
            return 3

        params = [match[0], match[1]]
        res = list(map(lambda x: x.algorithm(), params))
        for i in range(2):
            if isinstance(params[i],ReactPlayer):
                params[i].update(res[(i + 1) % 2])
        return int(res[0])+(int(res[1])*2)

    def Battle(self, match):
        result = Game.Validate(match)
        for i in range(2):
            match[i].score+= self.option.reward[result][i]

    def mutation(self):
        self.Playerlist.sort(key=lambda x: x.score, reverse=True)
        
        for i in range(self.option.mutationWeight):
            self.Playerlist.pop()
        for i in range(self.option.mutationWeight):
            self.Playerlist.append(type(self.Playerlist[i])())
        
    #don't touch, it's magic
    def monitor(self):
        return map(lambda x:(x.__name__,sum(isinstance(y,x) for y in self.Playerlist)),self.PlayerClass)
        # print('\n'.join(str(p) for p in  list(map(lambda x:(x.__name__,sum(isinstance(y,x) for y in self.Playerlist)),self.PlayerClass))))

    """
    league : 
    """
    def league(self):
        for i in self.lineUp:
            for n in range(self.option.rounds):
                self.Battle(map(lambda x:self.Playerlist[x],i))
                for j in range(2):
                    if isinstance(self.Playerlist[i[j]],ReactPlayer):
                        self.Playerlist[i[j]].update(True)
        self.mutation()
        map(lambda x: x.scoreReset(), self.Playerlist)

    def leagueStart(self):
        for i in range(self.option.leagueLoop):
            self.league()
            #Visualizer.Visualize(self)

#######################################################################################
#CONSTRUCTION AREA
#######################################################################################

class Visualizer:
    @staticmethod
    def Visualize(Game):
        G = nx.Graph()
        G.add_nodes_from(Game.Playerlist)
        print(Game.lineUp)
        G.add_edges_from(Game.lineUp)
        nx.draw_circular(G,with_labels=False)
        plt.show()
        return 0

class Verifier:
    @staticmethod
    def verify():
        testSet = [[2,10,2,11,0],[2,10,11,2,0],[2,2,11,10,0],[1,20,3,1,0],[10,6,9,0,0],[8,0,9,8,0]]
        testResult = ["Revenger","Mirror","Revenger","Mirror","Mirror","OnlyHelper"]
        counter = 0
        for i in range(len(testSet)):
            print("----------------------")
            g = Game(
                PlayerTypes=testSet[i],
                Option=Game.Option(
                    reward={
                        'BothBetray': 0,
                        'BothHelp': 2,
                        'BetrayBenefit': 3,
                        'HelpPenalty': -1},
                    rounds=10,
                    leagueLoop=50,
                    mutationWeight=5))
            g.leagueStart()
            simResult = sorted(g.monitor(),key=lambda x: x[1], reverse=True)
            counter+=int(simResult[0][0] ==testResult[i])
        print(str((counter*100)/len(testSet))+"%")
        return True

#######################################################################################
#CONSTRUCTION AREA
#######################################################################################
# gameInstance = Game(
#     PlayerTypes=[2, 2, 2, 2, 2],
#         Option=Game.Option(
#             reward={
#                 'BothBetray': 0,
#                 'BothHelp': 2,
#                 'BetrayBenefit': 3,
#                 'HelpPenalty': -1},
#             rounds=10,
#             leagueLoop=30,
#             mutationWeight=5))

Verifier.verify()

# gameInstance.leagueStart() 
# #시작 버튼을 누르면 실행
# gameInstance.monitor() 
#결과를 보고 싶습니다
