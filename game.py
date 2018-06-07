#-*- coding: utf-8 -*-

####################################
# One liter americano with 4 shots #
####################################
#something file changed here
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

    def resetPrevEnemyAction(self):
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
        self.visualizer = Visualizer(self)
        #print(self.lineUp)

    class Option(object):
        def __init__(self, reward, rounds, leagueLoop,mutationWeight,mistake):
            self.rounds = rounds
            self.reward = [(reward['BothBetray'],reward['BothBetray']),
                (reward['HelpPenalty'],reward['BetrayBenefit']),
                (reward['BetrayBenefit'],reward['HelpPenalty']),
                (reward['BothHelp'],reward['BothHelp'])]
            self.leagueLoop = leagueLoop
            self.mutationWeight=mutationWeight
            self.mistake = mistake/100.0

    @staticmethod
    def mistakeActions(input,missRate):
        return input and (random.random()>missRate)
        
    @staticmethod  #호출된 클래스나 인스턴스에 대해 모르는 메소드
    def Validate(match,mistake):
        if Player.areTheyFriends(match):
            return 3

        params = [match[0], match[1]]
        res = list(map(lambda x: Game.mistakeActions(x.algorithm(),mistake), params))
        for i in range(2):
            if isinstance(params[i],ReactPlayer):
                params[i].update(res[(i + 1) % 2])
        return int(res[0])+(int(res[1])*2)

    def Battle(self, match):
        result = Game.Validate(match,self.option.mistake)
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

    def league(self):
        for i in self.lineUp:
            for n in range(self.option.rounds):
                self.Battle(map(lambda x:self.Playerlist[x],i))
            for j in range(2):
                if isinstance(self.Playerlist[i[j]],ReactPlayer):
                    self.Playerlist[i[j]].resetPrevEnemyAction()
        self.mutation()
        map(lambda x: x.scoreReset(), self.Playerlist)

    def leagueStart(self):
        for i in range(self.option.leagueLoop):
            plt.pause(0.5)
            self.league()
            self.visualizer.updateData()
            self.visualizer.Visualize()

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
            self.G.node[j]['draw'] = nx.draw_networkx_nodes(self.G,self.pos,nodelist=[j],with_labels=False,node_size=20,node_color=self.color_dict[type(self.gameInstance.Playerlist[j]).__name__])
        
    
    def Visualize(self):
        plt.draw()

class Verifier:
    @staticmethod
    def verify():
        testSet = [[2,10,2,11,0],[2,10,11,2,0],[2,2,11,10,0],[1,20,3,1,0],[10,6,9,0,0],[8,0,9,8,0]]
        testResult = ["Revenger","Mirror","Revenger","Mirror","Mirror","OnlyHelper"]
        counter = 0
        for i in range(len(testSet)):
            
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
                    mutationWeight=5,
                    mistake=0))
            g.leagueStart()
            simResult = sorted(g.monitor(),key=lambda x: x[1], reverse=True)
            print("----------------------")
            print(simResult[0][0] ==testResult[i])
            counter+=int(simResult[0][0] ==testResult[i])
        print("verify result:"+str((counter*100)/len(testSet))+"%")
        return True


gameInstance = Game(
    PlayerTypes=[2, 2, 2, 2, 2],
        Option=Game.Option(
            reward={
                'BothBetray': 0,
                'BothHelp': 2,
                'BetrayBenefit': 3,
                'HelpPenalty': -1},
            rounds=10,
            leagueLoop=30,
            mutationWeight=5,
            mistake=0
            ))
            
Verifier.verify()
# gameInstance.leagueStart() 
# gameInstance.monitor() 
