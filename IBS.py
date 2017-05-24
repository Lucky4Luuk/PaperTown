def getItem(player,itemname) :
    if not player.hasItem(itemname) :
        player.giveItem(itemname)
        return "{0} has been given to {1}".format(itemname,player.getName())
    else :
        return "{1} already has {0}".format(itemname,player.getName())

def Attack(player,enemy) :
    if player.getVar("attack") == True :
        enemy.setVar("health", enemy.getVar("health") - player.getVar("dmg"))
