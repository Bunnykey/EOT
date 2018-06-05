#-*- coding: utf-8 -*-

####################################
# Please! Do not try this at home. #
####################################

import hashlib
import random
import networkx as nx

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

class ReactPlayer(Player):          ### 상대의 행동에 영향받는 플레이어의 클래스
    def __init__(self):
        Player.__init__(self)
        self.prevEnemyAction = True
    def update(self,input):
        raise NotImplementedError
        
class Mirror(ReactPlayer):
    def __init__(self):
        ReactPlayer.__init__(self)
    def update(self,input):
        self.prevEnemyAction = input ### 상대의 전번선택을 input 변수로 받아와서 prevEnemyAction에 저장
    def algorithm(self):
        return self.prevEnemyAction  ### prevEnemyAction을 따라서 행동함

class Revenger(ReactPlayer):
    def __init__(self):
        ReactPlayer.__init__(self)
    def update(self,input):
        self.prevEnemyAction &= input ### A &= B : only when A and B is True, A is True
    def algorithm(self):
        return self.prevEnemyAction

class Randomer(Player):
    def __init__(self):
        Player.__init__(self)
    def algorithm(self):
        return bool(random.randint(0,1)) ### bool타입 활용 (bool(1) = True, bool(0)= False))

class Game(object):
    def __init__(self, PlayerTypes, Option):
        self.Playerlist = []
        self.option = Option
        self.PlayerClass = [OnlyHelper, OnlyBetrayer, Mirror, Revenger, Randomer]
        for i in range(0, 5):
            for j in range(0, PlayerTypes[i]):
                self.Playerlist.append(self.PlayerClass[i]())
        #data setted
        #
        lineUp = []        
        for i in range(0,self.Playerlist.__len__()):
            for j in range(i+1,self.Playerlist.__len__()):
                lineUp.append((i,j))
        # self.G = nx.Graph()
        #self.g = Graph(lineUp)
        

    class Option(object):
        def __init__(self,reward,rounds,leagueLoop):
            self.rounds = rounds
            self.reward = reward
            self.leagueLoop = leagueLoop

    @staticmethod                #호출된 클래스나 인스턴스에 대해 모르는 메소드
    def validate(A, B):
        params=[A,B]
        res= list(map(lambda x:x.algorithm(),params))
        for i in range(0,2):
            if type(params[i]) is ReactPlayer:
                params[i].update(res[(i+1)%2])
                
        if res[0] and res[1]:        # 둘 다 협력
            return 0
        elif not(res[0] or res[1]):  # 둘 다 배신
            return 1
        elif res[1]:                 # A 가  배신
            return 2
        else:                        # B 가  배신
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
        self.Playerlist.sort(key=lambda x: x.score,reverse=True)
        for i in range(0,5):
            self.Playerlist.pop()
        for i in range(0,5):
            self.Playerlist.append(type(self.Playerlist[i])())
            
    def monitor(self):
        winnerList = []
        winnerCount = []
        for i in self.Playerlist:
            print(i.score , type(i).__name__)
        for i in range(0,len(self.Playerlist)):
            winnerList.append(str(type(self.Playerlist[i])))
        for i in self.PlayerClass:
            winnerCount.append(winnerList.count(str(i)))
        print winnerCount

    def scoreResetter(self):
        for i in self.Playerlist:
            i.score=0
            
    def league(self):
        playerlength = self.Playerlist.__len__()
        for i in range(0, playerlength):
            for j in range(i+1, playerlength):
                for k in range(0,self.option.rounds):
                    self.Battle(self.Playerlist[i],self.Playerlist[j])
                    if(type(self.Playerlist[i]) is ReactPlayer):
                        self.Playerlist[i].update(True)
                    if(type(self.Playerlist[j]) is ReactPlayer):
                        self.Playerlist[j].update(True)
        self.mutation()
        self.scoreResetter()
            
    def leagueStart(self):
        for i in range(0,self.option.leagueLoop):
            self.league()
            Visualizer.visualize(self)

#######################################################################################
#CONSTRUCTION AREA
#######################################################################################    
    # def graphSetter(self):
    #     self.g.vs["player"] = list(map(lambda x:type(x).__name__,self.Playerlist))

    # def visualize(self):
    #     gameInstance.graphSetter()
    #     myGraph = self.g
    #     layout = myGraph.layout_circle() ## dim=2
    #     color_dict = {"Mirror": "green", "Randomer": "pink", "Revenger":"yellow","OnlyBetrayer":"red", "OnlyHelper":"blue" }                
    #     graphic = plot(myGraph,
    #         layout = layout,
    #         bbox = (512,512),
    #         margin = 16,
    #         vertex_color = [color_dict[player] for player in myGraph.vs["player"]],
    #         vertex_size = 16)

class Visualizer:
    @staticmethod
    def visualize(Game):
        return 0
#######################################################################################
#CONSTRUCTION AREA
#######################################################################################        
gameInstance = Game(PlayerTypes=[20,20,20,20,20],
                    Option=Game.Option(
                        reward={'BothBetray':0,'BothHelp':2,'BetrayBenefit':3,'HelpPenalty':-1},
                        rounds =1,
                        leagueLoop=5))

# gameInstance.leagueStart() #시작 버튼을 누르면 실행
# gameInstance.monitor() #결과를 보고 싶습니다
