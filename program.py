import subprocess
import time
import sys


def imprimir(string):
        
        arrayString = list(string)
        subprocess.call("clear")
        print("\n")
        for s in range (len(arrayString)):
                
                sys.stdout.write(arrayString[s])
                sys.stdout.flush()
                
                time.sleep(0.05)
        
                
        


'''
class Animal:
        name = ""
        Atype = ""
        heigth = 0
        weigth = 0
        sound = ""
        color = ""
        
        def __init__(self, name, _type, heigth, weigth, sound, color):
                self.name = name
                self.Atype = _type
                self.heigth = heigth
                self.weigth = weigth
                self.sound = sound
                self.color = color
                
        def setName(self, name):
                self.name = name
                
        def getName(self):
                return self.name
        
        def setType(self, _type):
                self.type = _type
        
        def getType(self):
                return self.Atype
        
        def toString(self):
                return 'This is {}, the {}. \nColor: {} , and makes: {}'.format(self.name, self.Atype, self.color, self.sound)
        
                                
animalsArray = []

for count in range(0,2):
        animName = raw_input("Digite o nome do animal: ")
        animTipo = raw_input("o que ele eh? ")
        animAltura = raw_input("qual a altura dele? ")
        animPeso = raw_input("peso? " )
        animCor = raw_input("Qual a cor? ")
        animSom = raw_input("Que barulho ele faz? ")
        print "\n"
        animalsArray.append(Animal(animName, animTipo, animAltura, animPeso, animSom, animCor)) 

                
for count in range(0, len(animalsArray)):
        print(animalsArray[count].toString())
        print ("\n")

'''

class Enemy:
        
        posX = 0
        posY = 0
        attack = 0
        defense = 0
        agility = 0
        enemyType = ""
        hp = 0
        
        def __init__(self, tipo):
                
                self.enemyType = tipo
                
                
                if(self.enemyType == "Goblin"):
                        
                        self.attack = 2
                        self.defense = 1
                        self.agility = 2
                        self.hp = 5
                        
                elif(self.enemyType == "Troll"):        
                        
                        self.attack = 3
                        self.defense = 3
                        self.agility = 1
                        self.hp = 10
                
                elif(self.enemyType == "Soldier"):      
                        
                        self.attack = 2
                        self.defense = 2
                        self.agility = 2
                        self.hp = 6
                
                elif(self.enemyType == "Commander"):    
                        
                        self.attack = 4
                        self.defense = 3
                        self.agility = 1
                        self.hp = 12
                
        
                elif(self.enemyType == "Beast"):        
                        
                        self.attack = 4
                        self.defense = 1
                        self.agility = 3
                        self.hp = 6
                
                elif(self.enemyType == "Wyvern"):       
                        
                        self.attack = 6
                        self.defense = 5
                        self.agility = 5
                        self.hp = 25
                
                else:
                        
                        self.attack = 3
                        self.defense = 2
                        self.agility = 2
                        self.hp = 5
        
        def getEnemyType(self):
                return self.enemyType
        
        def getAttack(self):
                return (self.attack)
                         
        def getDefense(self):
                return (self.defense)
                         
        def getAgility(self):
                return self.agility
        
        def setAttack(self, attack):
                self.attack = attack
                
        def setDefense(self, defense):
                self.defense = defense
        
        def setAgility(self, agility):
                self.agility = agility
        
        def setPosition(self, x, y):
                self.posX = x
                self.posY = y
                
        def getPositionX(self):
                return self.posX
        
        def getPositionY(self):
                return self.posY
        
        def getHp(self):
                return self.hp
        
        def setHp(self, hp):
                self.hp = hp
        
        
        
        


class Weapon:
        name = ""
        attack = 0
        attackAll = 0
        
        def __init__(self, name, attack, All):
                self.name = name
                self.attack = attack
                if(All == 1):
                        self.attackAll = 1
                else:
                        self.attackAll = 0
        
        def getAttack(self):
                return self.attack
        
        def setAttack(self, attack):
                self.attack = attack
        
        def toString(self):
                return "Weapon: "+ self.name + ", Attack: " + str(self.attack) + "..."
                
class Armor:
        name = ""
        defense = 0
        modAgility = 0
        
        def __init__(self, name, defense, modAgility):
                self.name = name
                self.defense = defense
                self.modAgility = modAgility
                
        def getDefense(self):
                return self.defense
        
        def getModAgility(self):
                return self.modAgility
        
        def setDefense(self, defense):
                self.defense = defense
                
        def setModAgility(self, modAgility):
                self.modAgility = modAgility
        
        def toString(self):
                return "Armor: " + self.name + ", Defense: " + str(self.defense) + "..... Mod: " + str(self.modAgility)


        
class Hero:
        
        name = ""
        hp = 0
        heroClass = ""
        posX = 0
        posY = 0
        attack = 0
        defense = 0
        agility = 0
        weapon = Weapon("Hands",0,0)
        armor = Armor("Shirts",0,0)
        
        
        
        def __init__(self, name, heroClass):
                self.name = name
                self.heroClass = heroClass
                self.hp = 10
                
                if(heroClass == "Warrior"):
                        self.attack = 5
                        self.defense = 3
                        self.agility = 4
                
                elif(heroClass == "Mage"):
                        self.attack = 5
                        self.defense = 2
                        self.agility = 3
                        
                elif(heroClass == "Thief"):
                         self.attack = 3
                         self.defense = 3
                         self.agility = 4
                else:
                         self.attack = 4
                         self.defense = 2
                         self.agility = 4
                
                
        def getHp(self):
                return self.hp
        
        def setHp(self, newhp):
                self.hp = newhp
                        
        def getClass(self):
                return self.heroClass
        
        def getName(self):
                return self.name
                         
        def getAttack(self):
                return (self.attack + self.weapon.getAttack())
                         
        def getDefense(self):
                return (self.defense + self.armor.getDefense())
                         
        def getAgility(self):
                return self.agility - self.armor.getModAgility()
        
        def getWeapon(self):
                return self.weapon
                         
        def getArmor(self):
                return self.armor
                         
        def setAttack(self, attack):
                self.attack = attack
                
        def setDefense(self, defense):
                self.defense = defense
        
        def setAgility(self, agility):
                self.agility = agility
        
        def setPosition(self, x, y):
                self.posX = x
                self.posY = y
                
        def getPositionX(self):
                return self.posX
        
        def getPositionY(self):
                return self.posY
        
        def setWeapon(self, weapon):
                self.weapon = weapon
        
        def setArmor(self, armor):
                self.armor = armor
        
        def toString(self):
                return self.name + ", " + self.heroClass
        
        

def battle(hero, enemy):
        
        imprimir("Um " + enemy.getEnemyType() + " Apareceu!")
        time.sleep(0.025)
        imprimir("A batalha vai comecar!")
        winner = ""

        #verificar o verdadeiro
        while(hero.getHp()>= 0):
                
                if(hero.getAgility()>= enemy.getAgility()):
                        
                        heroAction = raw_input("Atacar, Defender ou usar Item?")
                        
                        if(heroAction == "Atacar"):
                                
                                dano = hero.getAttack() - enemy.getDefense()
                                
                                if(dano <=1):
                                        dano = 1
                                        
                                imprimir(hero.getName() + " Atacou!")
                                imprimir(enemy.getEnemyType() + " Sofreu dano de " + str(dano))
                                enemy.setHp(enemy.getHp() - dano)
                                
                        if(enemy.getHp() <= 0):
                                imprimir("A Batalhar terminou!")
                                winner = hero.getName()
                                break
                        
                        imprimir("O inimigo atacou!")
                        danoEnemy = enemy.getAttack() - hero.getDefense()
                        
                        if(danoEnemy <=1):
                                        danoEnemy = 1
                                        
                        imprimir(hero.getName() + " sofreu dano de " + str(danoEnemy))
                        
                        hero.setHp((hero.getHp() - danoEnemy))
                        
                        if(hero.getHp() <= 0):
                                imprimir("A Batalhar terminou!")
                                winner = enemy.getEnemyType()
                                break
                        
                                         
        if(winner == hero.getName()):
                                        
                imprimir(hero.getName() + " Venceu a batalha!")
                
        else:
                imprimir(enemy.getEnemyType() + " Venceu a batalha!")
                            
                                         
                
                                
                                
                        
                
        
        
        

def initialise():
        imprimir("Criando seu personagem!")
        time.sleep(1)
        imprimir("Nome do personagem")
        varNome = raw_input("\n>>")
        time.sleep(1)
        imprimir("O que ele eh? Opcoes: Motoqueiro, Motociclista, Bundao")
        varClass = raw_input("\n>>")

        return Hero(varNome, varClass)
        
        
'''             
hero1 = Hero("Diogo", "Warrior")
sword = Weapon("Sword", 2, 0)
shirt = Armor("Shirt", 0, 0)
cloth = Armor("Cloth", 1, 1)
hero1.setArmor(shirt)


print hero1.toString()
hands = Weapon("Hands", 0, 0)
hero1.setWeapon(hands)

print hero1.getAttack()
print hero1.getDefense()

hero1.setWeapon(sword)
hero1.setArmor(cloth)
print hero1.getAttack()
print hero1.getWeapon().toString()              
print hero1.getDefense()
print hero1.getArmor().toString()
print hero1.getAgility()
'''

                #main   

mapa = [["*"]*20 for i in range(20)]

def printingMapas(mapas):
        
        for x in range(0,20):
        
                for y in range(0,20):
                        
                        print ( str(mapas[x]) + "\n")
                        break
                        
        
mapa[19][9] = "P"       

subprocess.call("clear")

#printingMapas(mapa)

imprimir("O jogo vai comecar.........\n")
time.sleep(1)
heroi1 = initialise()
print heroi1.heroClass

goblin = Enemy("Goblin")
battle(heroi1, goblin)

print heroi1.toString()
print heroi1.getAttack()
heroi1.setHp(heroi1.getHp() - (goblin.getAttack() - heroi1.getDefense()))

print "Fim do programa"









        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
