class Warrior:
    name = "warrior"
    def rest_life(self,oponent_attack: int):
        if self.defense == None:
          self.health = self.health - oponent_attack
          if self.health > 0:
            self.is_alive = True
          elif self.health <= 0:
            self.is_alive = False
        if self.defense != None:
          if oponent_attack > self.defense:
            self.health -= oponent_attack - self.defense 
          if self.health > 0:
            self.is_alive = True
          elif self.health <= 0:
            self.is_alive = False  
        
    def __init__(self):
        self.health = 50
        self.maximum_health = self.health#
        self.is_alive = True
        self.attack = 5
        self.defense = None
        self.vampirism = None
        self.heal_power = None
    def equip_weapon(self,weapon_name):
      if (self.health + weapon_name.health) >= 0:
        self.maximum_health += weapon_name.health
        self.health += weapon_name.health
      if (self.health + weapon_name.health) < 0:
        self.healh = 0
        self.is_alive = False
      if (self.attack + weapon_name.attack) >= 0:
        self.attack += weapon_name.attack
      if (self.attack + weapon_name.attack) < 0:
        self.attack = 0
      if self.defense != None:
        if (self.defense + weapon_name.defense) >= 0:
          self.defense += weapon_name.defense
        if (self.defense + weapon_name.defense) < 0:
          self.defense = 0
      if self.vampirism != None:
        if (self.vampirism + weapon_name.vampirism) >= 0:
          self.vampirism += weapon_name.vampirism
        if (self.vampirism + weapon_name.vampirism) < 0:
          self.vampirism = 0
      if self.heal_power != None:
        if (self.heal_power + weapon_name.heal_power) >= 0:
          self.heal_power += weapon_name.heal_power
        if (self.heal_power + weapon_name.heal_power) < 0:
          self.heal_power = 0

class Knight(Warrior):
    name = "knight"
    def __init__(self):
        super().__init__()
        self.health = 50
        self.maximum_health = self.health
        self.attack = 7
        
import math
def fight(first: Warrior, second: Warrior,firstArmy = None, secondArmy = None):
    turn = 0
    while first.is_alive and second.is_alive:
        """
        print("                        ")
        print(first.health,second.health)#
        print(first.attack,second.attack)#
        print(first.defense,second.defense)#
        print(first.vampirism,second.vampirism)#
        print(first.heal_power,second.heal_power)#
        """
        if turn == 0:  
            dealt_damage = second.health
            second.rest_life(first.attack)#first attack second
            dealt_damage -= second.health
            if isinstance(first,Vampire):
              if (first.health+(dealt_damage*(first.vampirism/100))>first.maximum_health):
                first.health = first.maximum_health
              else:
                first.health += math.floor(dealt_damage*(first.vampirism/100))
            if isinstance(first,Lancer):
              try:
                secondArmy.units[1].rest_life(dealt_damage*(first.collateral/100))
              except:
                pass
            try:
              if isinstance(firstArmy.units[1],Healer):
                firstArmy.units[1].heal(first)
            except:
              pass
            turn = 1
        elif turn == 1:
            dealt_damage = first.health
            first.rest_life(second.attack)
            dealt_damage -= first.health
            if isinstance(second,Vampire):
              if (second.health+(dealt_damage*(second.vampirism/100))>second.maximum_health):
                second.health = second.maximum_health
              else:
                second.health += math.floor(dealt_damage*(second.vampirism/100))
            if isinstance(second,Lancer):
              try:
                firstArmy.units[1].rest_life(dealt_damage*(second.collateral/100))
              except:
                pass
            try:
              if isinstance(secondArmy.units[1],Healer):
                secondArmy.units[1].heal(second)
            except:
              pass
            turn = 0
    """
    print("                        ")
    print(first.name,second.name)#
    print(first.health,second.health)#
    print(first.attack,second.attack)#
    print(first.defense,second.defense)#
    print(first.vampirism,second.vampirism)#
    print(first.heal_power,second.heal_power)#
    """
    if first.is_alive:
        return True
    return False

class Army:
  def __init__(self):
    self.amount = 0
    self.units = []
    self.withWarlord = False

  def add_units(self,typeS: Warrior,number: int):
    self.amount = number
    for i in range(self.amount):
      if self.withWarlord and (str(typeS) == "<class '__main__.Warlord'>"):
        continue
      elif (self.withWarlord == False) and (str(typeS) == "<class '__main__.Warlord'>"):
        self.withWarlord = True
      self.units.append(typeS())
  
  def move_units(self):#no toca arrancar del comienzo, sino del final
    if self.withWarlord:
      unitsRearranged = []
      unitsWithAttack = False
      posHealer = 1
      for i in self.units:
        if isinstance(i,Lancer)  and i.is_alive:
          unitsWithAttack = True
          unitsRearranged.append(i)
      for i in self.units:
        if (not isinstance(i, Warlord)) and (not isinstance(i,Healer)) and (not isinstance(i,Lancer))  and i.is_alive:
          unitsWithAttack = True
          unitsRearranged.append(i) 
      for i in self.units:
        if isinstance(i,Healer)  and i.is_alive:
          if unitsWithAttack:
            unitsRearranged.insert(posHealer,i)
            posHealer += 1
          else:
            unitsRearranged.append(i)
      for i in self.units:
        if isinstance(i,Warlord) and i.is_alive:
          unitsRearranged.append(i)
        elif isinstance(i,Warlord) and (not i.is_alive):
          self.withWarlord = False
      self.units = unitsRearranged


      

class Battle:
  def __init__(self):
    pass
  def fight(self,firstArmy: Army,secondArmy: Army):
    firstArmy.move_units()
    secondArmy.move_units()
    
    while (len(firstArmy.units) != 0) & (len(secondArmy.units) != 0):
      print(len(firstArmy.units),len(secondArmy.units))
      print(firstArmy.units[0].name,secondArmy.units[0].name)
      print(firstArmy.units[0].health,secondArmy.units[0].health)
      print("                      ")
      if fight(firstArmy.units[0],secondArmy.units[0],firstArmy,secondArmy):
        
        secondArmy.units.pop(0)
        secondArmy.move_units()
      else:
        firstArmy.units.pop(0)
        firstArmy.move_units()
    if len(firstArmy.units) > 0:
      return True
    return False

  def straight_fight(self,army_1, army_2):
    newArmy_1 = []
    newArmy_2 = []
    if isinstance(army_1,Army) and isinstance(army_2,Army):
      army_1 = army_1.units
      army_2 = army_2.units
    for i in range(max(len(army_1),len(army_2))):
      try:
        soldier_1 = army_1[i]
      except:
        newArmy_2.append(army_2[i])
        continue
      try:
        soldier_2 = army_2[i]
      except:
        newArmy_1.append(army_1[i])
        continue
      if fight(soldier_1,soldier_2):
        newArmy_1.append(soldier_1)
      else:
        newArmy_2.append(soldier_2)
    if newArmy_1 == []:
      return False
    elif newArmy_2 == []:
      return True
    else:
      return self.straight_fight(newArmy_1,newArmy_2)

class Defender(Warrior):
  name = "defender"
  def __init__(self):
    super().__init__()
    self.health = 60
    self.maximum_health = self.health
    self.attack = 3
    self.defense = 2

class Vampire(Warrior):
  name = "vampire"
  def __init__(self):
    super().__init__()
    self.health = 40
    self.maximum_health = self.health
    self.attack = 4
    self.vampirism = 50

class Lancer(Warrior):
  name = "lancer"
  def __init__(self):
    super().__init__()
    self.health = 50
    self.maximum_health = self.health
    self.attack = 6
    self.collateral = 50

class Healer(Warrior):
  name = "healer"
  def __init__(self):
    super().__init__()
    self.health = 60
    self.maximum_health = self.health
    self.attack = 0
    self.heal_power = 2
  def heal(self,warrior: Warrior):
    if (warrior.health + self.heal_power) > warrior.maximum_health:
        warrior.health = warrior.maximum_health
    else:
        warrior.health = warrior.health + self.heal_power

class Weapon:
  def __init__(self,health, attack, defense, vampirism, heal_power):
    self.health = health
    self.attack = attack
    self.defense = defense
    self.vampirism = vampirism
    self.heal_power = heal_power

class Sword(Weapon):
  def __init__(self):
    super().__init__(5,2,0,0,0)

class Shield(Weapon):
  def __init__(self):
    super().__init__(20,-1,2,0,0)

class GreatAxe(Weapon):
  def __init__(self):
    super().__init__(-15,5,-2,10,0)

class Katana(Weapon):
  def __init__(self):
    super().__init__(-20,6,-5,50,0)

class MagicWand(Weapon):
  def __init__(self):
    super().__init__(30,3,0,0,3)

class Warlord(Warrior):
  name = "Warlord"
  def __init__(self):
    super().__init__()
    self.health = 100
    self.attack = 4
    self.defense = 2
#test 24
army_1 = Army()
army_2 = Army()
army_1.add_units(Warrior, 2)
army_1.add_units(Lancer, 2)
army_1.add_units(Defender, 1)
army_1.add_units(Warlord, 3)
army_2.add_units(Warlord, 2)
army_2.add_units(Vampire, 1)
army_2.add_units(Healer, 5)
army_2.add_units(Knight, 2)
army_1.move_units()
army_2.move_units()
battle = Battle()
print(battle.fight(army_1, army_2))
