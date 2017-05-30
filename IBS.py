def getItem(player,itemname) :
    if not player.hasItem(itemname) :
        player.giveItem(itemname)
        return "{0} has been given to {1}".format(itemname,player.getName())
    else :
        return "{1} already has {0}".format(itemname,player.getName())

def Attack(player,enemy) :
    if player.getAttack() == True :
        enemy.setHealth(, enemy.getHealth() - player.getDmg())

def Heal(player,health) :
    if player.getHeal() == True :
        player.setHealth(, player.getHealth() + player.getRegen())

def Exp(player,lvl,enemy,battle) :
    if enemy.getHealth() <= 0 :
        battle = False
        player.setLvl(, player.getLvl() + enemy.getExp())


def UseItem(player,itemname) :
    if player.
