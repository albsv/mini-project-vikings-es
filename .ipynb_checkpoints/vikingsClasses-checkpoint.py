import random

# Soldier

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
        
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"

# Davicente

class War():
    def __init__(self):
        vikingArmy = []
        saxonArmy = []

    def addViking(self, viking):
        vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        saxonArmy.append(saxon)
    
    def vikingAttack(self):
       viking = random.choice(vikingArmy)
       saxon = random.choice(saxonArmy)
       result = saxon.receiveDamage(viking.attack())
       if saxon.health <= 0:
        saxonArmy.remove(saxon)
       return result
      
    def saxonAttack(self):
        viking = random.choice(vikingArmy)
        saxon = random.choice(saxonArmy)
        result = viking.receiveDamage(saxon.attack())
        if viking.health <= 0:
            vikingArmy.remove(viking)
        return result

    def showStatus(self):
        if not saxonArmy:
            return "Vikings have won the war of the century!"
        elif not vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
    
    pass

#yop
class War2:

    def __init__(self):
        # your code here

    def addViking(self, Viking):
        # your code here
    
    def addSaxon(self, Saxon):
        # your code here
    
    def vikingAttack(self):
        # your code here

    def saxonAttack(self):
        # your code here

    def showStatus(self):
        # your code here

    pass

