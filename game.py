####################################
# One liter americano with 4 shots #
####################################

import random
import networkx as nx
import matplotlib.pyplot as plt

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
            self.G.node[j]['draw'] = nx.draw_networkx_nodes(self.G,self.pos,nodelist=[j],with_labels=False,node_size=20,node_color=self.color_dict[type(self.gameInstance.Playerlist[j]).__name__])
    
class Verifier: #for Test-driven development
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
            print("..")
            counter+=int(sorted(g.monitor(),key=lambda x: x[1], reverse=True)[0][0] ==testResult[i])
        print("verify result:"+str((counter*100)/len(testSet))+"%")

gameInstance = Game(
    PlayerTypes=[5, 5, 5, 5, 5],
        Option=Game.Option(
            reward={
                'BothBetray': 0,
                'BothHelp': 2,
                'BetrayBenefit': 3,
                'HelpPenalty': -1},
            rounds=10,
            leagueLoop=30,
            mutationWeight=5,
            mistake=0))
#Verifier.verify()
gameInstance.leagueStart() 
#gameInstance.monitor() ##shows instance name