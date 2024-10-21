import random

print("bienvenue au jeux Heros vs Vilain")


nom = input("entrez le nom de votre hero : ")

print("votre Hero s'appelle : ",nom)

adversaire = input("entrez le nom de votre adversaire : ")

print("votre adversaire s'appelle : ",adversaire)

strength_hero = random.randint(1,20)
intelligence_hero = random.randint(1,20)
endurance_hero = random.randint(1,20)
wisdom_hero = random.randint(1,20)

totalPointHero = strength_hero + intelligence_hero + endurance_hero + wisdom_hero

print("voici vos competences ... ")

print("strength : ",strength_hero)
print("intelligence : ",intelligence_hero)
print("endurance : ",endurance_hero)
print("wisdom : ",wisdom_hero)
print("vos points totals sont : ",totalPointHero)

#les competences de l'adversaire 

strength_vilain = random.randint(1,20)
intelligence_vilain = random.randint(1,20)
endurance_vilain = random.randint(1,20)
wisdom_vilain = random.randint(1,20)
totalPointVilain = strength_vilain + intelligence_vilain + endurance_vilain + wisdom_vilain

print("voici les competences de votre adversaire... ")

print("strength : ",strength_vilain)
print("intelligence : ",intelligence_vilain)
print("endurance : ",endurance_vilain)
print("wisdom : ",wisdom_vilain)
print("le nombre total de points de votre adversaire est : ",totalPointVilain)

#le combat commence 

print("le combat commence !!!")

if totalPointHero > totalPointVilain:
    print(f"le vainqueur est : {nom} avec un total de : {totalPointHero} soit {totalPointHero - totalPointVilain} de plus")
elif totalPointHero < totalPointVilain:
    print(f"le vainqueur est : {adversaire} avec un total de : {totalPointVilain} soit {totalPointVilain - totalPointHero} de plus")
else : 
    print(f"le match est nul aucun vainqueur avec un total de : {totalPointVilain} chacun")
