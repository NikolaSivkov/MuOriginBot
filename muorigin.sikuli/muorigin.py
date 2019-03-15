# pylint: disable=undefined-variable
Debug.on(3)
# focus MeMu
#memu = App("MEmu.exe")
# memu.focus()
#print memu
# exit()


def participateInBC(event):
    click("bloodCastleBanner.png")
    click("enterGreenButton.png")
    sleep(5)
    turnOnAutoBattle()
    wait("acceptGreenButton.png", 500)
    click("acceptGreenButton.png")


def participateInDS(event):
    click("dsBanner.png")
    click("enterGreenButton.png")
    sleep(5)
    turnOnAutoBattle()
    wait("DevilSquareBattleWin.png", 600)
    click("acceptButton.png")


def turnOnAutoBattle():
    click("autoBattleButton.png")


def doExpDungeon():
    DungeonIcon = has("dungeonIcon.png")
    if DungeonIcon == False:
        click("heroIcon.png")
        sleep(1)
        DungeonIcon = has("dungeonIcon.png")
        if DungeonIcon == False:
            return

    click("dungeonIcon.png")
    click("DallyDungeon.png")
    click("expDungeonBanner.png")
    click("enterGreenButton.png")
    wait("expDungeonGreyRewardBanner.png", 120)
    click("expDungeonGreyRewardBanner.png")
    sleep(1)
    click("expDungeonClaimButton.png")
    click("quitButton.png")
    sleep(5)

# DiceHunt


def doDiceHunt():
    DiceIcon = has("diceHunterIcon.png")
    if DiceIcon == False:
        click("heroIcon.png")
        sleep(1)

    click("diceHunterIcon.png")
    for diceNum in range(5):
        click("normalDiceButton.png")
        sleep(5)
        nextLevel = has("diceHuntConfirmGreenButton.png")
        # bossFight = has("fightButton.png")
        if nextLevel:
            click("diceHuntConfirmGreenButton.png")
            sleep(3)

        # if bossFight:
        #     click("fightButton.png")
        #     sleep(2)
        #     turnOnAutoBattle()
        #     wait("confirmGreenButton.png", 120)
        #     click("confirmGreenButton.png")
    click("closeButton.png")


def doExperienceExchange():
    ExchangeIcon = has("exchangeIcon.png")
    if ExchangeIcon == False:
        return
    click("exchangeIcon.png")
    click(Pattern("exchangeWithZenBanner.png").similar(0.90))
    for exchangeNum in range(8):
        click("exchangeGreenButton.png")
    click("closeButton.png")


def autoProcessDailyQuest(event):
    click("autoProcessButton.png")


def claimExp(event):
    click("claimButtonOrange.png")
    click("claimX2RadioButton.png")
    click("claimButton.png")


def exitSikuli(event):
    exit(1)


def doJournalRetrieveEssence():
    JournalIcon = has("journalIcon.png")

    if JournalIcon == False:
        click("heroIcon.png")
        sleep(1)

    click("journalIcon.png")
    click("retrieveEssence.png")
    # the loading of essence takes about 3 seconds, if prematurely clicked it only retrieves however much essence is loaded
    sleep(3)
    click("dissasembleGreenButton.png")
    if has("confirmGreenButton.png"):
        click("confirmGreenButton.png")

    click("cancelGreenButton.png")
    click("closeButton.png")


def doDonateToGuild():
    guildIcon = has("guildIcon.png")
    if guildIcon == False:
        click("heroIcon.png")
        sleep(1)
    click("guildIcon.png")
    click("GuildDonationButton.png")
    click("stormStoneIcon.png")
    for stormStoneIcon in range(20):
        click("guildDonationButton-2.png")
    click("earthStoneIcon.png")
    for earthStoneIcon in range(20):
        click("guildDonationButton-2.png")
    click("waveStoneIcon.png")
    for waveStoneIcon in range(20):
        click("guildDonationButton-2.png")
    click("lavaStoneIcon.png")
    for lightBlueRockNum in range(20):
        click("guildDonationButton-2.png")

    click("closeButton.png")
    click("closeButton.png")


#onAppear("bcBanner.png", participateInBC)
#onAppear("dsBanner.png", participateInDS)

#onAppear("claimButtonOrange.png", claimExp)
#onAppear("autoProcessButton.png", autoProcessDailyQuest)
#onAppear("exitButton.png", exitSikuli)

#Settings.ObserveScanRate = 1

# observe(300)
# doExperienceExchange()
# doDonateToGuild()
# doDiceHunt()
# doExpDungeon()
sleep(30)
# doExperienceExchange()
