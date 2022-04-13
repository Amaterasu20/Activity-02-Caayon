import random 

print("""A Lv.100 Pidgeot (Normal/Flying, Sp. Atk: 220) 
attacks a Lv. 110  Marowak (Ground, Sp. Def: 250) with Brave Bird,
a Flying-type move with a Power of 95 and gains a same-type attack bonus.
It hits the target and deals a very effective damage. The weather on the field is normal.
Given the following conditions, determine how much damage Pidgeot's attack will deal. \n""") 

#damage
Level = 100
Power = 95
A = 220
D = 250

#modifier 
Target = 1 
Weather = 1.5
Badge = 1 
Critical = random.randint(1,2) 
Random_number = round(random.uniform(0.85 , 1.00),2) 
STAB = 1 
Type = 2
other = 1

Modifier = round(Target*Weather*Badge*Critical*Random_number*STAB*Type*other)
Damage = round((((((2*Level)/5)+2)*Power*A/D)/50)+2)*Modifier

print("Target: ",Target)
print("Weather: ", Weather)
print("Badge: ",Badge)
print("Critical: ",Critical)
print("Random: ",Random_number)
print("STAB: ",STAB)
print("Type: ", Type)
print("Other: ",other)
print("\nModifiers: ", Modifier)
print("\nPidgeot deals ",Damage,"to Marowak ")

Recoil_Dam = round(Damage*0.333)
Recoil = random.randint(1,500)
if Recoil >= Recoil_Dam:
	print("As well as Marowak is recoiling.")
else:
	print("However, Marowak is not recoiling..")
