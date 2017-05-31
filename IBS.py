def getItem(player,itemname,amount) :
    if player.hasItem(itemname) :
        if player.getItemAmount(itemname) > 0 :
            player.addItem(itemname,amount)
        else :
            if player.hasInvRoom() :
                player.addItem(itemname,amount)
    else :
        if player.hasInvRoom() :
            player.addItem(itemname,amount)

def Attack(player,enemy) :
    if player.getAttack() == True :
        enemy.setHealth(enemy.getHealth() - player.getDmg())

def Heal(player,health) :
    if player.getHeal() == True :
        player.setHealth(player.getHealth() + player.getRegen())

def Exp(player,lvl,enemy,battle) :
    if enemy.getHealth() <= 0 :
        battle = False
        player.setLvl(player.getLvl() + enemy.getExp())


def UseItem(player,itemname) :
    if player.hasItem(itemname) :
        if player.getItemAmount(itemname) > 0 :
            player.useItem(itemname)
