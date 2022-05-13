from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import math
from PyQt5.QtCore import QTimer, QTime, Qt 

Rocks = 0
Miners = 0
Excavators = 0


ToolPower=1
ExcavPower=1

MinerCost=40
ExcavatorCost=200

tickrate=1000

ToolsCost=150
TimerCost=2500
ExcavUpgradeCost=1000

def window():
    app = QApplication(sys.argv)
    
    win=QMainWindow()
    win.setGeometry(0,0,1920,1080)
    win.setWindowTitle("Rock Miner")


    Rock=QtWidgets.QPushButton(win)
    
    RockCount= QtWidgets.QLabel(win)
    
    MinerCount=QtWidgets.QLabel(win)
    
    MinerButton=QtWidgets.QPushButton(win)

    MinerText=QtWidgets.QLabel(win)
    
    ExcavatorCount=QtWidgets.QLabel(win)
    
    ExcavatorButton=QtWidgets.QPushButton(win)
    
    ExcavatorText=QtWidgets.QLabel(win)
    
    UpgradeTools=QtWidgets.QLabel(win)
    
    UpgradeTimer=QtWidgets.QLabel(win)
    
    UpgradeExcavator=QtWidgets.QLabel(win)
    
    UpgradeToolsButton=QtWidgets.QPushButton(win)

    UpgradeTimerButton=QtWidgets.QPushButton(win)
    
    UpgradeExcavatorButton=QtWidgets.QPushButton(win)


    def ClickRock():
        global Rocks,Miners
        Rocks=Rocks+((Miners+1)*ToolPower)
        RockCount.setText("Rocks: "+ str(Rocks))


    def BuyMiner():
        global Rocks,Miners,MinerCost
        if(Rocks>=MinerCost):
            Rocks=Rocks-MinerCost
            Miners=Miners +1
            MinerCost=math.floor(MinerCost*1.3)
            MinerCount.setText("Miners: "+str(Miners))
            MinerButton.setText("Buy (" +str(MinerCost)+")")
            RockCount.setText("Rocks: "+ str(Rocks))

    def BuyExcavator():
        global Rocks,Excavators,ExcavatorCost
        if(Rocks>=ExcavatorCost):
            Rocks=Rocks-ExcavatorCost
            Excavators=Excavators+1
            ExcavatorCost=math.floor(ExcavatorCost*1.4)
            ExcavatorButton.setText("Buy (" +str(ExcavatorCost)+")")
            ExcavatorCount.setText("Excavators: "+str(Excavators))
            RockCount.setText("Rocks: "+ str(Rocks))
    def BuyTools():
        global Rocks,ToolsCost,ToolPower
        if(Rocks>=ToolsCost):
            if(ToolPower==1):
                ToolPower=2
                UpgradeToolsButton.setText("Bought!")
                Rocks=Rocks-ToolsCost
    
    def BuyTimer():
        global Rocks,TimerCost,tickrate
        if(Rocks>=TimerCost):
            Rocks=Rocks-TimerCost
            TimerCost=TimerCost*10
            tickrate=math.floor(tickrate/2)
            UpgradeTimerButton.setText("Buy ("+str(TimerCost)+")")
    
    
    def BuyExcavUpgrade():
        global Rocks,ExcavatorCost,ExcavPower,ExcavUpgradeCost
        if(Rocks>=ExcavUpgradeCost):
            Rocks=Rocks-ExcavatorCost
            ExcavPower=ExcavPower*2
            ExcavUpgradeCost=ExcavUpgradeCost*5
            UpgradeExcavatorButton.setText("Buy ("+str(ExcavUpgradeCost)+")")
    def Update():
        global Rocks,Excavators
        Rocks=Rocks+(Excavators*ExcavPower)
        RockCount.setText("Rocks: "+ str(Rocks))

    


    RockCount.setGeometry(0,0,200,30)
    RockCount.setText("Rocks: "+ str(Rocks))
    RockCount.setFont(QFont("Arial",20))

    Rock.setText("Rocks")
    Rock.setGeometry(0,200,400,400)
    Rock.setFont(QFont("Arial",30))
    Rock.clicked.connect(ClickRock)
    #Buildings
        
    MinerCount.setGeometry(1000,10,200,20)
    MinerCount.setText("Miners: "+str(Miners))
    MinerCount.setFont(QFont("Arial",20))

        
    MinerButton.setGeometry(1000,30,150,40)
    MinerButton.setText("Buy (" +str(MinerCost)+")")
    MinerButton.clicked.connect(BuyMiner)


        
    MinerText.setText("Miners help you mine more rock with each click.")
    MinerText.setGeometry(1150,30,450,40)
    MinerText.setFont(QFont('Arial',10))
    
        
    ExcavatorCount.setGeometry(1000,100,200,20)
    ExcavatorCount.setText("Excavators: "+str(Excavators))
    ExcavatorCount.setFont(QFont("Arial",20))

        
    ExcavatorButton.setGeometry(1000,120,150,40)
    ExcavatorButton.setText("Buy (" +str(ExcavatorCost)+")")
    ExcavatorButton.clicked.connect(BuyExcavator)

    
    
    ExcavatorText.setText("Excavators mine rock automatically.")
    ExcavatorText.setGeometry(1150,120,450,40)
    ExcavatorText.setFont(QFont('Arial',10))
    

    #Upgrades
    UpgradeTools.setGeometry(1000,420,250,20)
    UpgradeTools.setText("Better Tools(2x click)")
    UpgradeTools.setFont(QFont('Arial',15))
    
    UpgradeToolsButton.setGeometry(1000,440,150,40)
    UpgradeToolsButton.setText("Buy ("+str(ToolsCost)+")")
    UpgradeToolsButton.clicked.connect(BuyTools)   
    
    UpgradeTimer.setGeometry(1350,420,250,20)
    UpgradeTimer.setText("Double mining speed.")
    UpgradeTimer.setFont(QFont('Arial',15))    
    
    UpgradeTimerButton.setGeometry(1350,440,150,40)
    UpgradeTimerButton.setText("Buy ("+str(TimerCost)+")")
    UpgradeTimerButton.clicked.connect(BuyTimer)
    
    UpgradeExcavator.setGeometry(1000,550,250,20)
    UpgradeExcavator.setText("Better Excavators(2x)")
    UpgradeExcavator.setFont(QFont('Arial',15))
    
    UpgradeExcavatorButton.setGeometry(1000,570,150,40)
    UpgradeExcavatorButton.setText("Buy ("+str(ExcavUpgradeCost)+")")
    UpgradeExcavatorButton.clicked.connect(BuyExcavUpgrade)    
    
    
    timer = QTimer(win) 
  
   
  
     
    timer.start(tickrate) 

    timer.timeout.connect(Update)

    
    win.show()
    sys.exit(app.exec_())



window()

