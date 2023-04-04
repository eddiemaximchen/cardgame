import random
from card import *

class Deck():
    SUIT_TUPLE=('Diamonds','Clubs','Hearts','Spades')
    STANDARD_DICT={'Ace':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'Jack':11,'Queen':12,'King':13}

    def __init__(self,window,rankValueDict=STANDARD_DICT):
        self.startingDeckList=[]
        self.playingDecklist=[]
        for suit in Deck.SUIT_TUPLE:
            for rank,value in rankValueDict.items():
                objCard=card(window,rank,suit,value)
                self.startingDeckList.append(objCard)
        self.shuffle()

    def shuffle(self):
        #複製起始牌組並將其儲存在要玩的排組list中
        self.playingDecklist=self.startingDeckList.copy()
        for objCard in self.playingDecklist:
            objCard.conceal()
        random.shuffle(self.playingDecklist)

    def getCard(self):
        if len(self.playingDecklist) ==0:
            raise IndexError('No match cards')
        #抽牌
        objCard=self.playingDecklist.pop()
        return objCard
    
        #回收出過的牌
    def returnCardToDeck(self,objCard):
        self.playingDecklist.insert(0,objCard)
        
