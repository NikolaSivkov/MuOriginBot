
#pylint: disable=undefined-variable

def participateInBC(event):
    click("bcBanner.png")
    click("enterButton.png")
    sleep(5)
    turnOnAutoBattle()

def participateInDS(event):
    click("bcBanner.png")
    click("enterButton.png")
    sleep(5)
    turnOnAutoBattle()


def turnOnAutoBattle():
     click("autoBattleIcon.png")

def doExpDungeon():
    DungeonIcon = exists("doExpDungeon.png")
    if DungeonIcon.score < 0.5:
        return
    click("doExpDungeon.png")
    click("dailyDungeonButton.png")
    click("expDungeonBanner.png")
    click("enterButton.png")
    wait("expDungeonRewardBaner.png",120)
    click("expDungeonRewardBaner.png")
    click("claimButton.png")


#DiceHunt
def doDiceHunt():
    DiceIcon = exists("diceHunterIcon.png")
    if DiceIcon.score  < 0.5:
        click("heroIcon.png")

    click("diceHunterIcon.png")
    for diceNum in range(5):
        click("normalDiceButton.png")
        sleep(5)
        nextLevel = exists("confirmGreenButton.png")
        bossFight = exists("fightButton.png")
        if nextLevel.score  > 0.4:
            click("confirmGreenButton.png")
            sleep(1)
            
        if bossFight.score  > 0.4:
            click("fightButton.png")
            sleep(2)
            turnOnAutoBattle()
            wait("confirmGreenButton.png",120)
            click("confirmGreenButton.png")

def doExperienceExchange():
    ExchangeIcon = exists("expExchangeIcon.png")
    if ExchangeIcon.score  < 0.3:
        return
    click("expExchangeIcon.png")
    click("zenExchangeIcon.png")
    for exchangeNum in range(8):
        click("exchangeButton.png")
    click("closeButton.png")




#define Observables
onAppear("bcBanner.png", participateInBC)
onAppear("1552049198793.png", participateInDS)

doExperienceExchange()