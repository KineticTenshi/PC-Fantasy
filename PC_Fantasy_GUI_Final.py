import random
import math
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from math import *
from functools import partial
import string

class General:
#Stat du personnage ou du boss
	def __init__(self, Name, Max_HP, HP, Shield, Max_MP, MP, R_MP, Atk, Def, CR, C_DMG, Penetration, Sensitivity):
		self.Name = Name
		self.Max_HP = Max_HP
		self.HP = HP
		self.Shield = Shield
		self.Max_MP = Max_MP
		self.MP = MP
		self.R_MP = R_MP
		self.Atk = Atk
		self.Buff_Atk = 1.0
		self.Debuff_Atk = 1.0
		self.Def = Def
		self.Buff_Def = 1.0
		self.Debuff_Def = 1.0
		self.CR = CR
		self.C_DMG = C_DMG
		self.Penetration = Penetration
		self.Sensitivity = Sensitivity
		self.Buff_Sensitivity = 1.0
		self.Debuff_Sensitivity = 1.0
		self.Alive = 1

#Fonction Max_HP Modifier
	def Max_HP_Modifier(self, Modifier):
		if self.Alive ==1:
			self.Max_HP += Modifier
			for n in range(0,N_characters):
				perso_hp_bar[n].config(max = slots_personnages[n].get_Max_HP())
			boss_hp_bar.config(max = boss.get_Max_HP())

#Fonction HP Modifier
	def HP_Modifier(self, Modifier):
		if self.Alive ==1:
			if Modifier > 0 :
				self.HP += Modifier
				print("\n",self.Name,"'s HP healed by", Modifier,"!")
				if self.HP > self.Max_HP:
					self.HP = self.Max_HP
			if Modifier < 0 :
				F_DMG = self.Shield + Modifier
				self.Shield_Modifier(Modifier)
				if F_DMG < 0 :
					self.Shield = 0
					self.HP += F_DMG
					print("\n",self.Name,"'s HP damaged by", -F_DMG,"!")
				if self.HP <= 0:
					self.HP = 0
					self.Alive = 0
					print("\n",self.Name,"has fallen !")
			boss_hp_bar['value'] = boss.get_HP()
			for n in range(0,N_characters):
				perso_hp_bar[n]['value'] = slots_personnages[n].get_HP()

#Fonction Shield Modifier
	def Shield_Modifier(self, Modifier):
		if self.Alive ==1:
			if Modifier > 0:
				self.Shield += Modifier * self.Sensitivity * self.Buff_Sensitivity
			elif Modifier < 0:
				self.Shield += Modifier
				if self.Shield < 0:
					self.Shield = 0
			boss_shield_bar['value'] = boss.get_Shield()
			for n in range(0,N_characters):
				perso_shield_bar[n]['value'] = slots_personnages[n].get_Shield()

#Fonction Max_MP Modifier
	def Max_MP_Modifier(self, Modifier):
		if self.Alive ==1:
			self.Max_MP += Modifier
			for n in range(0,N_characters):
				perso_mp_bar[n].config(max = slots_personnages[n].get_Max_MP())

#Fonction MP Modifier
	def MP_Modifier(self, Modifier):
		if self.Alive ==1:
			self.MP += Modifier
			if self.MP > self.Max_MP:
				self.MP = self.Max_MP
			if self.MP < 0:
				self.MP = 0
			boss_mp_bar['value'] = boss.get_MP()
			for n in range(0,N_characters):
				perso_mp_bar[n]['value'] = slots_personnages[n].get_MP()

#Fonction R_MP Modifier
	def R_MP_Modifier(self, Modifier):
		if self.Alive ==1:
			self.R_MP += Modifier
			if self.R_MP < 0:
				self.R_MP = 0

#Fonction Atk Modifier
	def Atk_Modifier(self, Modifier):
		if self.Alive ==1:
			self.Atk += Modifier
			if Modifier > 0 :
				print("\n",self.Name,"'s Atk increased by", Modifier,"!")
			if Modifier < 0 :
				print("\n",self.Name,"'s Atk decreased by", -Modifier,"!")
			if self.Atk < 0 :
				self.Atk = 0

#Fonction Buff_Atk Modifier
	def Buff_Atk_Modifier(self, Modifier):
		if self.Alive ==1:
			self.Buff_Atk *= Modifier * self.Sensitivity * self.Buff_Sensitivity
			print("\n",self.Name,"'s Atk increased by", (Modifier-1)*100,"%!")

#Fonction Debuff_Atk Modifier
	def Debuff_Atk_Modifier(self, Modifier):
		if self.Alive ==1:
			self.Debuff_Atk *= Modifier * self.Sensitivity * self.Debuff_Sensitivity
			print("\n",self.Name,"'s Atk decreased by", (1 - (1/Modifier))*100,"%!")

#Fonction Def Modifier
	def Def_Modifier(self, Modifier):
		if self.Alive ==1:
			self.Def += Modifier
			if self.Def < 0 :
				self.Def = 0

#Fonction Buff_Def Modifier
	def Buff_Def_Modifier(self, Modifier):
		if self.Alive ==1:
			self.Buff_Def *= Modifier * self.Sensitivity * self.Buff_Sensitivity
			print("\n",self.Name,"'s Def increased by", (Modifier-1)*100,"%!")

#Fonction Debuff_Def Modifier
	def Debuff_Def_Modifier(self, Modifier):
		if self.Alive ==1:
			self.Debuff_Def *= Modifier * self.Sensitivity * self.Debuff_Sensitivity
			print("\n",self.Name,"'s Def decreased by", (1 - (1/Modifier))*100,"%!")

#Fonction CR Modifier
	def CR_Modifier(self, Modifier):
		if self.Alive ==1:
			if Modifier > 0 :
				self.CR += Modifier * self.Sensitivity * self.Buff_Sensitivity
				print("\n",self.Name,"'s Crit Rate increased by", Modifier,"!")
			if Modifier < 0 :
				self.CR += Modifier *self.Sensitivity * self.Debuff_Sensitivity
				print("\n",self.Name,"'s Crit Rate decreased by", -Modifier,"!")
			if self.CR < 0 :
				self.CR = 0

#Fonction C DMG Modifier
	def C_DMG_Modifier(self, Modifier):
		if self.Alive ==1:
			if Modifier > 0:
				self.C_DMG += Modifier *self.Sensitivity * self.Buff_Sensitivity
			if Modifier < 0:
				self.C_DMG += Modifier *self.Sensitivity * self.Debuff_Sensitivity
			if self.C_DMG < 0 :
				self.C_DMG = 0

#Fonction Penetration Modifier
	def Penetration_Modifier(self, Modifier):
		if self.Alive ==1:
			if Modifier > 0 :
				self.Penetration += Modifier * self.Sensitivity * self.Buff_Sensitivity
				print("\n",self.Name,"'s Penetration increased by", Modifier,"!")
			if Modifier < 0 :
				self.Penetration += Modifier * self.Sensitivity * self.Debuff_Sensitivity
				print("\n",self.Name,"'s Penetration decreased by", -Modifier,"!")
			if self.Penetration < 0 :
				self.Penetration = 0
			if self.Penetration > 100 :
				self.Penetration = 100

#Fonction Buff_Sensitivity Modifier
	def Buff_Sensitivity_Modifier(self, Modifier):
		if self.Alive ==1:
			self.Buff_Sensitivity *= Modifier * self.Sensitivity
			if Modifier > 0 :
				print("\n",self.Name,"'s sensitivity to buffs increased by", Modifier,"!")
			if Modifier < 0 :
				print("\n",self.Name,"'s sensitivity to buffs decreased by", -Modifier,"!")

#Fonction Buff_Sensitivity Modifier
	def Debuff_Sensitivity_Modifier(self, Modifier):
		if self.Alive ==1:
			self.Debuff_Sensitivity *= Modifier * self.Sensitivity
			if Modifier > 0 :
				print("\n",self.Name,"'s sensitivity to debuffs increased by", Modifier,"!")
			if Modifier < 0 :
				print("\n",self.Name,"'s sensitivity to debuffs decreased by", -Modifier,"!")

#Fonction Damage Formula
	def Damage_Formula(self, target):
		F_Atk = self.get_Atk()*(self.get_Buff_Atk()/self.get_Debuff_Atk())
		F_Def = target.get_Def()*target.get_Buff_Def()/target.get_Debuff_Def()
		DMG = math.floor((F_Atk)*(1-((F_Def/(F_Def+12000))*(1-(self.Penetration/100)))))
		if random.randint(1,100) <= self.CR:
			DMG += math.floor(DMG*self.C_DMG)
		return DMG

#Fonction Heal amount
	def Heal_Amount(self):
		if self.Alive ==1:
			Heal = self.Atk*self.Buff_Atk/self.Debuff_Atk
			if random.randint(1,100) <= self.CR :
				Heal += Heal*self.C_DMG
			return Heal

	def get_Name(self):
		return str(self.Name)

	def get_Max_HP(self):
		return int(self.Max_HP)

	def get_HP(self):
		return int(self.HP)

	def get_Shield(self):
		return int(self.Shield)

	def get_Max_MP(self):
		return int(self.Max_MP)

	def get_MP(self):
		return int(self.MP)

	def get_R_MP(self):
		return int(self.R_MP)

	def get_Atk(self):
		return float(self.Atk)

	def get_Buff_Atk(self):
		return float(self.Buff_Atk)
		
	def get_Debuff_Atk(self):
		return float(self.Debuff_Atk)

	def get_Def(self):
		return float(self.Def)

	def get_Buff_Def(self):
		return float(self.Buff_Def)
		
	def get_Debuff_Def(self):
		return float(self.Debuff_Def)

	def get_CR(self):
		return float(self.CR)

	def get_C_DMG(self):
		return float(self.C_DMG)

	def get_Penetration(self):
		return float(self.Penetration)

	def get_Sensitivity(self):
		return float(self.Sensitivity)

	def get_Buff_Sensitivity(self):
		return float(self.Buff_Sensitivity)

	def get_Debuff_Sensitivity(self):
		return float(self.Debuff_Sensitivity)

	def get_skill_list(self):
		return self.skill_list
	
	def get_Status(self):
		return self.Alive

#Fonction d'affichage de stats
	def affichage_stat(self):
		print("\n", self.Name,"'s HP =", self.HP, ":\n Shield =", self.Shield, ";\n MP =", self.MP, ";\n Atk =", self.Atk*(self.Buff_Atk/self.Debuff_Atk), ";\n Def =", self.Def*(self.Buff_Def/self.Debuff_Def), ";\n C DMG =", self.C_DMG)

#Fonction de demande d'action
	def demande_action(self):
		print("\nChoose", self.Name,"'s action : 1 = Auto-attack, 2 = Skill, 3 = Block\n")
		return int(input())

class Skill(General):
	def __init__(self, Name, Duration, Current_Duration, Cooldown, Current_Cooldown, MP_Cost, Storage_List, Counter_List):
		self.Name = Name
		self.Duration = Duration
		self.Current_Duration = Current_Duration
		self.Cooldown = Cooldown
		self.Current_Cooldown = Current_Cooldown
		self.MP_Cost = MP_Cost
		self.Activation = 0
		self.Storage_List = Storage_List
		self.Counter_List = Counter_List

	def Duration_Modifier(self, Modifier):
		self.Current_Duration += Modifier

	def Cooldown_Modifier(self, Modifier):
		self.Current_Cooldown += Modifier
		if self.Current_Cooldown < 0:
			self.Current_Cooldown = 0
		for i in range(N_characters*3):
			button_skills_perso[i].config(text=slots_skills_totaux[i].get_Name() + " (" + str(slots_skills_totaux[i].get_Current_Cooldown()) + ")")

	def Duration_Equalizer(self):
		self.Current_Duration = self.Duration

	def Cooldown_Equalizer(self):
		self.Current_Cooldown = self.Cooldown
		for i in range(N_characters*3):
			button_skills_perso[i].config(text=slots_skills_totaux[i].get_Name() + " (" + str(slots_skills_totaux[i].get_Current_Cooldown()) + ")")
	
	def Activation_Modifier(self, Modifier):
		self.Activation += Modifier
		
	def Activation_Canceler(self):
		self.Activation = 0

	def Counter_Modifer(self, indice, Modifier):
		self.Counter_List[indice] += Modifier

	def get_Duration(self):
		return int(self.Duration)

	def get_Current_Duration(self):
		return int(self.Current_Duration)

	def get_Cooldown(self):
		return int(self.Cooldown)

	def get_Current_Cooldown(self):
		return int(self.Current_Cooldown)

	def get_MP_Cost(self):
		return int(self.MP_Cost)

	def get_Activation(self):
		return int(self.Activation)
	
	def get_Storage_List(self):
		return self.Storage_List
	
	def get_Counter_List(self):
		return self.Counter_List
		
	def get_skill_description(self):
		return self.skill_description

#Hiro's Skills
class Acid_Demonstration(Skill):
	def __init__(self):
		super(Acid_Demonstration, self).__init__("Acid Demonstration", 0, 0, 5, 0, 5, Storage_List = [0.0]*N_characters, Counter_List = [0])

	def casting(self, target):
		if self.Activation ==1:
			self.Storage_List[0] = target.get_C_DMG()
			self.Storage_List[1] = boss.get_Max_HP()/25

			target.C_DMG_Modifier(1.5)
			target.Atk += self.Storage_List[1]

			self.Storage_List[0] = target.get_C_DMG() - self.Storage_List[0]
			boss.HP_Modifier(-target.Damage_Formula(boss))
			target.C_DMG += - self.Storage_List[0]
			target.Atk += -self.Storage_List[1]
	
	skill_description = ("MP Cost = 5 ; Duration = 0 turn ; Cooldown = 5 turns \n\nIncreases Hiro's Critical Damage by 150% \nDeals damage scaling with enemies's Max HP")

class Cocktail_Overdrive(Skill):
	def __init__(self):
		super(Cocktail_Overdrive, self).__init__("Cocktail Overdrive", 4, 0, 4, 0, 4, Storage_List = [0.0]*(2*N_characters), Counter_List = [0])

	def casting(self, target):
		if self.Activation == 1:
			if self.Current_Duration == 0 :
				for n in range(0,N_characters):
					self.Storage_List[n] = slots_personnages[n].get_CR()
					slots_personnages[n].CR_Modifier(35)
					self.Storage_List[n] = slots_personnages[n].get_CR() - self.Storage_List[n]
				for n in range(N_characters, 2*N_characters):
					self.Storage_List[n] = slots_personnages[n-N_characters].get_C_DMG()
					slots_personnages[n-N_characters].C_DMG_Modifier(0.4)
					self.Storage_List[n] = slots_personnages[n-N_characters].get_C_DMG() - self.Storage_List[n]

			if self.Current_Duration > 0:
				self.Current_Duration = self.Duration
				print("\nDuration has been refreshed !")

		if self.Current_Duration ==1:
			for n in range(0,N_characters):
				slots_personnages[n].CR += -self.Storage_List[n]
			for n in range(N_characters, 2*N_characters):
				slots_personnages[n-N_characters].C_DMG += -self.Storage_List[n]
			self.Current_Duration += -1
	
	skill_description = ("MP Cost = 4 ; Duration = 3 turns ; Cooldown = 4 turns \n\nIncreases party Critical Rate by 35% \nIncreases party Critical Damage by 40%")

class Sulfuric_Bomb(Skill):
	def __init__(self):
		super(Sulfuric_Bomb, self).__init__("Sulfuric Bomb", 3, 0, 4, 0, 2, Storage_List = [0.0], Counter_List = [0])

	def casting(self, target):
		if self.Current_Duration != 1:
			boss.HP_Modifier(-boss.get_Max_HP()/10)
		
		if self.Activation ==1:
			if self.Current_Duration == 0:
				self.Storage_List[0] = boss.get_Debuff_Def()
				boss.Debuff_Def_Modifier(2)
				self.Storage_List[0] =  self.Storage_List[0] - boss.get_Debuff_Def()
			elif self.Current_Duration > 0:
				self.Current_Duration = self.Duration

		if self.Current_Duration == 1:
			boss.Debuff_Def += self.Storage_List[0]
			self.Current_Duration += -1
			
	skill_description = ("MP Cost = 2 ; Duration = 2 turns ; Cooldown = 4 turns \n\nDecreases enemies' Defense by 50% \nEach turn, burns 10% of enemies' Max HP")

#Seyren's Skills
class Ignition_Break(Skill):
	def __init__(self):
		super(Ignition_Break, self).__init__("Ignition Break", 0, 0, 3, 0, 3, Storage_List = [0.0]*N_characters, Counter_List = [0])

	def casting(self, target):
		if self.Activation ==1:
			target.Atk += 5000
			self.Storage_List[1] = target.get_C_DMG()
			target.C_DMG_Modifier(1)
			self.Storage_List[1] = target.get_C_DMG() - self.Storage_List[1]

			self.Storage_List[0] = target.get_Penetration()
			target.Penetration_Modifier(20)
			self.Storage_List[0] = target.get_Penetration() - self.Storage_List[0]

			boss.HP_Modifier(-target.Damage_Formula(boss)*2)
			#target.affichage_stat()
			target.Atk -= 5000
			target.C_DMG += -self.Storage_List[1]
			target.Penetration += -self.Storage_List[0]
	
	skill_description = ("MP Cost = 3 ; Duration = 0 turns ; Cooldown = 3 turns \n\nIncreases Seyren's base Attack by 5 000 \nIncreases Seyren's Critical Damage by 100% \nIncreases Seyren's Penetration by 20% \nDeals damage to enemies")

class Target_Weakness(Skill):
	def __init__(self):
		super(Target_Weakness, self).__init__("Target Weakness", 5, 0, 6, 0, 3, Storage_List = [0.0]*3, Counter_List = [0])

	def casting(self, target):
		if self.Activation == 1:
			if self.Current_Duration == 0:
				self.Storage_List[0] = target.get_Penetration()
				target.Penetration_Modifier(30)
				self.Storage_List[0] = target.get_Penetration() - self.Storage_List[0]
				
				self.Storage_List[1] = target.get_Buff_Atk()
				target.Buff_Atk_Modifier(1.3)
				self.Storage_List[1] = target.get_Buff_Atk() - self.Storage_List[1]
				
				self.Storage_List[2] = target.get_Buff_Atk()
				target.CR_Modifier(30)
				self.Storage_List[2] = target.get_Buff_Atk() - self.Storage_List[2]
			
			elif self.Current_Duration > 0:
				self.Current_Duration = self.Duration

		if self.Current_Duration ==1:
			target.Penetration += -self.Storage_List[0]
			target.Buff_Atk += - self.Storage_List[1]
			target.CR += - self.Storage_List[2]

			self.Current_Duration += -1
	
	skill_description = ("MP Cost = 2 ; Duration = 4 turns ; Cooldown = 6 turns \n\nIncreases Seyren's Penetration by 30%\nIncreases Seyren's Attack by 30%\nIncreases Seyren's Critical Rate by 30%")

class Acute_Senses(Skill):
	def __init__(self):
		super(Acute_Senses, self).__init__("Acute Senses", 5, 0, 6, 0, 2, Storage_List = [0.0], Counter_List = [0])

	def casting(self, target):
		if self.Activation == 1:
			if self.Current_Duration == 0:
				self.Storage_List[0] = target.get_Buff_Sensitivity()
				target.Buff_Sensitivity_Modifier(1.3)
				self.Storage_List[0] = target.get_Buff_Sensitivity() - self.Storage_List[0]
			
			elif self.Current_Duration > 0:
				self.Current_Duration = self.Duration

		if self.Current_Duration ==1:
			target.Buff_Sensitivity += - self.Storage_List[0]
			self.Current_Duration += -1
			
	skill_description = ("MP Cost = 2 ; Duration = 4 turns ; Cooldown = 6 turns \n\nIncreases Seyren's Buff Sensitivity by 30%")

#Raphaela's Skills
class Revitalize(Skill):
	def __init__(self):
		super(Revitalize, self).__init__("Revitalize", 5, 0, 6, 0, 3, Storage_List = [0.0]*N_characters, Counter_List = [0]*N_characters)

	def casting(self, target):
		if self.Activation == 1:
			if self.Current_Duration == 0 :
				target.Max_HP_Modifier(20000)
				target.HP_Modifier(20000)
				for n in range(0,N_characters):
					slots_personnages[n].Max_HP_Modifier(2000)
					slots_personnages[n].HP_Modifier(2000)

			if self.Current_Duration > 0:
				self.Current_Duration = self.Duration
				print("\nDuration has been refreshed !")

		if self.Current_Duration ==1:
			target.Max_HP_Modifier(-20000)
			target.HP += -20000
			for n in range(0,N_characters):
				slots_personnages[n].Max_HP_Modifier(-2000)
				slots_personnages[n].HP += -2000
			self.Current_Duration += -1
	
	skill_description = ("MP Cost = 3 ; Duration = 4 turns ; Cooldown = 6 turns \n\nIncreases Raphaela's Max HP by 20 000 \nIncreases party Max HP by 2 000")

class Fortress(Skill):
	def __init__(self):
		super(Fortress, self).__init__("Fortress", 3, 0, 4, 0, 1, Storage_List = [0.0], Counter_List = [0])

	def casting(self, target):
		
		if self.Activation == 1:
			if self.Current_Duration == 0 :
				target.Shield_Modifier(15000)

			if self.Current_Duration > 0:
				self.Current_Duration = self.Duration
				print("\nDuration has been refreshed !")

		if self.Current_Duration ==1:
			target.Shield_Modifier(-15000)
			self.Current_Duration += -1
	
	skill_description = ("MP Cost = 1 ; Duration = 2 turns ; Cooldown = 4 turns \n\nIncreases Raphaela's Shield by 15 000")

class Coercion(Skill):
	def __init__(self):
		super(Coercion, self).__init__("Coercion", 3, 0, 3, 0, 1, Storage_List = [0.0], Counter_List = [0])

	def casting(self, target):
		if self.Current_Duration !=1:
			for n in range(0, len(boss_skills)):
				boss_skills[n].Activation_Modifier(2)

		if self.Activation == 1 :
			if self.Current_Duration == 0:
				self.Storage_List[0] = boss.get_Debuff_Atk()
				boss.Debuff_Atk_Modifier(1/0.7)
				self.Storage_List[0] =  boss.get_Debuff_Atk() - self.Storage_List[0]
			
			elif self.Current_Duration > 0:
				self.Current_Duration = self.Duration

		if self.Current_Duration ==1:
			boss.Debuff_Atk += self.Storage_List[0]
			self.Current_Duration += -1
	
	skill_description = ("MP Cost = 1 ; Duration = 2 turns ; Cooldown = 3 turns \n\nSilences ennemies \nDecreases enemies' Attack by 30%")

#Jibril' Skills
class Path_Of_Light(Skill):
	def __init__(self):
		super(Path_Of_Light, self).__init__("Path Of Light", 0, 0, 2, 0, 2, Storage_List = [0.0]*N_characters, Counter_List = [0]*N_characters)

	def casting(self,target):
		slots_personnages[global_target].HP_Modifier(target.Heal_Amount() + slots_personnages[global_target].get_Max_HP()*0.35)

	skill_description = ("MP Cost = 2 ; Duration = 0 turn ; Cooldown = 2 turns \n\nHeals one target \nAdditionally heals target's by 35% of their Max HP")
	
class Sanctuary(Skill):
	def __init__(self):
		super(Sanctuary, self).__init__("Sanctuary", 4, 0, 5, 0, 4, Storage_List = [0.0]*N_characters, Counter_List = [0]*N_characters)

	def casting(self,target):
		if self.Current_Duration != 1:
			for n in range(0,N_characters):
				slots_personnages[n].HP_Modifier(target.Heal_Amount() + 1000)

		if self.Activation == 1:

			if self.Counter_List[global_target] == 0:
				self.Counter_List[global_target] = self.Duration
				self.Storage_List[global_target] = slots_personnages[global_target].get_Buff_Atk()
				slots_personnages[global_target].Buff_Atk_Modifier(1.5)
				self.Storage_List[global_target] = slots_personnages[global_target].get_Buff_Atk()-self.Storage_List[global_target]

			elif self.Counter_List[global_target] > 0:
				self.Counter_List[global_target] = self.Duration
				print("\nDuration has been refreshed !")

		for n in range (0,N_characters) :
			if self.Counter_List[n] == 1:
				slots_personnages[n].Buff_Atk += - self.Storage_List[n]
				self.Counter_List[n] += -1

		if self.Current_Duration == 1:
			self.Current_Duration += -1

	skill_description = ("MP Cost = 4 ; Duration = 3 turns ; Cooldown = 5 turns \n\nIncreases one target's Attack by 50% \nHeals party every turn")

class Piety(Skill):
	def __init__(self):
		super(Piety, self).__init__("Piety", 4, 0, 5, 0, 3, Storage_List = [0.0]*(N_characters+1), Counter_List = [0])

	def casting(self,target):
		if self.Activation == 1:
			if self.Current_Duration == 0:
				for n in range(0,N_characters):
					self.Storage_List[n] = slots_personnages[n].get_CR()
					slots_personnages[n].CR_Modifier(25)
					self.Storage_List[n] = slots_personnages[n].get_CR() - self.Storage_List[n]
				self.Storage_List[N_characters] = boss.get_CR()
				boss.CR_Modifier(-25)
				self.Storage_List[N_characters] = boss.get_CR() - self.Storage_List[N_characters]

			elif self.Current_Duration > 0:
				self.Current_Duration = self.Duration
				print("\nDuration has been refreshed !")

		if self.Current_Duration == 1:
			for n in range(0,N_characters):
				slots_personnages[n].CR += -self.Storage_List[n]
			boss.CR += -self.Storage_List[N_characters]
			self.Current_Duration += -1

	skill_description = ("MP Cost = 3 ; Duration = 3 turns ; Cooldown = 5 turns \n\nIncreases party Critical Rate by 25% \nDecreases enemies' Critical Rate by 25%")
	
#Lucias' Skills
class Renovatio(Skill):
	def __init__(self):
		super(Renovatio, self).__init__("Renovatio", 4, 0, 5, 0, 4, Storage_List = [0.0]*N_characters, Counter_List = [0])

	def casting(self,target):
		if self.Current_Duration != 1:
			for n in range(0,N_characters):
				slots_personnages[n].HP_Modifier(target.Heal_Amount() + 1000)
		
		if self.Activation == 1 :
			if self.Current_Duration == 0:
				for n in range(0,N_characters):
					self.Storage_List[n] = slots_personnages[n].get_Buff_Def()
					slots_personnages[n].Buff_Def_Modifier(1.4)
					self.Storage_List[n] = slots_personnages[n].get_Buff_Def() - self.Storage_List[n]

			elif self.Current_Duration > 0:
				self.Current_Duration = self.Duration
				print("\nDuration has been refreshed !")

		if self.Current_Duration ==1:
			for n in range(0,N_characters):
				slots_personnages[n].Buff_Def += -self.Storage_List[n]
			self.Current_Duration += -1

	skill_description = ("MP Cost = 4 ; Duration = 3 turns ; Cooldown = 5 turns \n\nIncreases party Defense by 40% \nHeals party every turn")

class Curatio(Skill):
	def __init__(self):
		super(Curatio, self).__init__("Curatio", 4, 0, 5, 0, 2, Storage_List = [0.0]*N_characters, Counter_List = [0]*N_characters)

	def casting(self,target):
		if self.Activation == 1:
			
			slots_personnages[global_target].HP_Modifier(slots_personnages[global_target].get_Max_HP()/2)

			if self.Counter_List[global_target] == 0:
				self.Counter_List[global_target] = self.Duration
				self.Storage_List[global_target] = slots_personnages[global_target].get_Buff_Sensitivity()
				slots_personnages[global_target].Buff_Sensitivity_Modifier(1.35)
				self.Storage_List[global_target] = slots_personnages[global_target].get_Buff_Sensitivity()-self.Storage_List[global_target]

			elif self.Counter_List[global_target] > 0:
				self.Counter_List[global_target] = self.Duration
				print("\nDuration has been refreshed !")

		for n in range (0,N_characters) :
			if self.Counter_List[n] == 1:
				slots_personnages[n].Buff_Sensitivity += - self.Storage_List[n]
				self.Counter_List[n] += -1

		if self.Current_Duration == 1:
			self.Current_Duration += -1

	skill_description = ("MP Cost = 2 ; Duration = 3 turns ; Cooldown = 5 turns \n\nHeals one target by 50% of their Max HP \nIncreases target's Buff Sensitivity by 35%")

class Expiatio(Skill):
	def __init__(self):
		super(Expiatio, self).__init__("Expiatio", 0, 0, 4, 0, 5, Storage_List = [0.0], Counter_List = [0])

	def casting(self,target):
		for n in range(0,N_characters):
			slots_personnages[n].MP_Modifier(3)
			slots_personnages[n].Debuff_Atk = 1
			slots_personnages[n].Debuff_Def = 1
			slots_personnages[n].Debuff_Sensitivity = 1
		
		for n in range(0, len(boss_skills)): #reset du storage des effets négatifs pour éviter la contre variation
			boss_storage = boss_skills[n].get_Storage_List()
			for m in range(0, len(boss_storage)):
				if boss_storage[m] < 0:
					boss_storage[m] = 0
					boss_skills[n].Current_Duration = 0 #annulation du skill du boss
		
		print("\nLucias has blessed the ally team !")
		champs.delete(0, END)
		champs.insert(0, "Lucias has blessed the ally team !")

	skill_description = ("MP Cost = 5 ; Duration = 0 turn ; Cooldown = 4 turns \n\nIncreases party MP by 3 points \nCleanses party \nDispells enemies")

#Clause's Skills
class Endure(Skill):
	def __init__(self):
		super(Endure, self).__init__("Endure", 5, 0, 6, 0, 3, Storage_List = [0.0]*(N_characters+1), Counter_List = [0])

	def casting(self,target):

		if self.Activation == 1 :

			if self.Current_Duration == 0:

				self.Storage_List[N_characters] = target.get_Buff_Def()
				target.Buff_Def_Modifier(1.6)
				self.Storage_List[N_characters] = target.get_Buff_Def() - self.Storage_List[N_characters]

				for n in range(0,N_characters):
					self.Storage_List[n] = slots_personnages[n].get_Buff_Def()
					slots_personnages[n].Buff_Def_Modifier(1.2)
					self.Storage_List[n] = slots_personnages[n].get_Buff_Def() - self.Storage_List[n]

			elif self.Current_Duration > 0:
				self.Current_Duration = self.Duration
				print("\nDuration has been refreshed !")

		if self.Current_Duration ==1:
			target.Buff_Def += -self.Storage_List[N_characters]
			for n in range(0,N_characters):
					slots_personnages[n].Buff_Def += -self.Storage_List[n]
			self.Current_Duration += -1

	skill_description = ("MP Cost = 3 ; Duration = 4 turns ; Cooldown = 6 turns \n\nIncreases Clause's' Defense by 60% \nIncreases party Defense by 20%")

class Pierce(Skill):
	def __init__(self):
		super(Pierce, self).__init__("Pierce", 5, 0, 6, 0, 2, Storage_List = [0.0]*N_characters, Counter_List = [0]*N_characters)

	def casting(self,target):
		if self.Activation == 1:

			if self.Counter_List[global_target] == 0:
				self.Counter_List[global_target] = self.Duration
				self.Storage_List[global_target] = slots_personnages[global_target].get_Penetration()
				slots_personnages[global_target].Penetration_Modifier(25)
				self.Storage_List[global_target] = slots_personnages[global_target].get_Penetration() - self.Storage_List[global_target]

			elif self.Counter_List[global_target] > 0:
				self.Counter_List[global_target] = self.Duration
				print("\nDuration has been refreshed !")

		if self.Current_Duration ==1:
			self.Current_Duration += -1

		for n in range (0,N_characters) :
			if self.Counter_List[n] == 1:
				slots_personnages[n].Penetration_Modifier(-self.Storage_List[n])
				self.Counter_List[n] += -1

	skill_description = ("MP Cost = 2 ; Duration = 4 turns ; Cooldown = 6 turns \n\nIncreases one target's Penetration by 25%")

class Hide_Weakness(Skill):
	def __init__(self):
		super(Hide_Weakness, self).__init__("Hide Weakness", 5, 0, 6, 0, 2, Storage_List = [0.0], Counter_List = [0])

	def casting(self,target):
		if self.Activation == 1:
			if self.Current_Cooldown == self.Cooldown :
				self.Storage_List[0] = boss.get_Penetration()
				boss.Penetration_Modifier(-25)
				self.Storage_List[0] = boss.get_Penetration() - self.Storage_List[0]

		if self.Current_Duration ==1:
			boss.Penetration_Modifier(-self.Storage_List[0])
			self.Current_Duration += -1

	skill_description = ("MP Cost = 2 ; Duration = 4 turns ; Cooldown = 6 turns \n\nDecreases enemies Penetration by 25%")

#Cassius' Skills
class Light_Domain(Skill):
	def __init__(self):
		super(Light_Domain, self).__init__("Light Domain", 4, 0, 5, 0, 5, Storage_List = [0.0]*N_characters, Counter_List = [0])

	def casting(self,target):
		if self.Current_Duration != 1:
			for n in range(0,N_characters):
				slots_personnages[n].HP_Modifier(target.Heal_Amount())

		if self.Activation == 1:
			if self.Current_Duration ==0:
				for n in range(0,N_characters):
					self.Storage_List[n] = slots_personnages[n].get_CR()
					slots_personnages[n].CR_Modifier(20)
					self.Storage_List[n] = slots_personnages[n].get_CR() - self.Storage_List[n]

			elif self.Current_Duration >0:
				self.Current_Duration = self.Duration

		if self.Current_Duration ==1:
			for n in range(0,N_characters):
				slots_personnages[n].CR_Modifier(-self.Storage_List[n])
			self.Current_Duration += -1

	skill_description = ("MP Cost = 5 ; Duration = 3 turns ; Cooldown = 5 turns \n\nHeals party every turn \nIncreases party Critical Rate by 20%")

class Empower(Skill):
	def __init__(self):
		super(Empower, self).__init__("Empower", 2, 0, 3, 0, 3, Storage_List = [0.0]*N_characters, Counter_List = [0]*N_characters)

	def casting(self,target):
		if self.Activation == 1:

			if self.Counter_List[global_target] == 0:
				self.Counter_List[global_target] = self.Duration
				self.Storage_List[global_target] = slots_personnages[global_target].get_C_DMG()
				slots_personnages[global_target].C_DMG_Modifier(2)
				self.Storage_List[global_target] = slots_personnages[global_target].get_C_DMG() - self.Storage_List[global_target]

			elif self.Counter_List[global_target] > 0:
				self.Counter_List[global_target] = self.Duration
				print("\nDuration has been refreshed !")

		for n in range (0,N_characters) :
			if self.Counter_List[n] == 1:
				slots_personnages[n].C_DMG += - self.Storage_List[n]
				self.Counter_List[n] += -1

		if self.Current_Duration ==1:
			self.Current_Duration += -1

	skill_description = ("MP Cost = 3 ; Duration = 0 turn ; Cooldown = 3 turns \n\nIncreases one target's Critical Damage by 200%")

class Serenity(Skill):
	def __init__(self):
		super(Serenity, self).__init__("Serenity", 3, 0, 3, 0, 2, Storage_List = [0.0]*(2*N_characters+1), Counter_List = [0])

	def casting(self,target):

		if self.Activation == 1 :

			if self.Current_Duration == 0:
				for n in range(0,N_characters):
					self.Storage_List[n] = slots_personnages[n].get_Buff_Atk()
					slots_personnages[n].Buff_Atk_Modifier(1.3)
					self.Storage_List[n] = slots_personnages[n].get_Buff_Atk() - self.Storage_List[n]

				for n in range(N_characters, 2*N_characters):
					self.Storage_List[n] = slots_personnages[n-N_characters].get_Shield()
					slots_personnages[n-N_characters].Shield_Modifier(4000 + target.get_Atk()*target.get_Buff_Atk()/target.get_Debuff_Atk()/2)
					self.Storage_List[n] = slots_personnages[n-N_characters].get_Shield() - self.Storage_List[n]

				self.Storage_List[2*N_characters] = target.get_Shield()
				target.Shield_Modifier(10000 + target.get_Atk()*target.get_Buff_Atk()/target.get_Debuff_Atk()*2)
				self.Storage_List[2*N_characters] = target.get_Shield() - self.Storage_List[2*N_characters]

			if self.Current_Duration > 0:
				self.Current_Duration = self.Duration
				for n in range(0, N_characters):
					slots_personnages[n].Shield_Modifier(4000 + target.get_Atk()/2)
				print("\nDuration has been refreshed !")

		if self.Current_Duration ==1:
			target.Shield_Modifier(-self.Storage_List[2*N_characters])
			for n in range(0,N_characters):
				slots_personnages[n].Buff_Atk += -self.Storage_List[n]
			for n in range(N_characters, 2*N_characters):
				slots_personnages[n-N_characters].Shield_Modifier(-self.Storage_List[n])
			self.Current_Duration += -1

	skill_description = ("MP Cost = 2 ; Duration = 2 turns ; Cooldown = 3 turns \n\nIncreases party Attack by 30% \nIncreases party Shield \nIncreases Cassius' Shield")

#Elise's Skills
class Hunter_Instinct(Skill):
	def __init__(self):
		super(Hunter_Instinct, self).__init__("Hunter Instinct", 5, 0, 6, 0, 3, Storage_List = [0.0]*N_characters, Counter_List = [0])

	def casting(self,target):
		if self.Current_Duration != 1:
			target.HP -= target.get_Max_HP()*0.35

		if self.Activation == 1:
			if self.Current_Duration == 0:
				
				self.Storage_List[1] = target.get_Buff_Sensitivity()
				target.Buff_Sensitivity_Modifier(1.3)
				self.Storage_List[1] = target.get_Buff_Sensitivity() - self.Storage_List[1]
				
				self.Storage_List[0] = target.get_Penetration()
				target.Penetration_Modifier(30)
				self.Storage_List[0] = target.get_Penetration() - self.Storage_List[0]
				
				self.Storage_List[2] = target.get_CR()
				target.CR_Modifier(35)
				self.Storage_List[2] = target.get_CR() - self.Storage_List[2]

				self.Storage_List[3] = target.get_Buff_Atk()
				target.Buff_Atk_Modifier(1.45)
				self.Storage_List[3] = target.get_Buff_Atk() - self.Storage_List[3]

			elif self.Current_Duration > 0:
				self.Current_Duration = self.Duration

		if self.Current_Duration == 1:
			target.Buff_Sensitivity += - self.Storage_List[1]
			target.Penetration +=-self.Storage_List[0]
			target.CR += -self.Storage_List[2]
			target.Buff_Atk += -self.Storage_List[3]
			self.Current_Duration += -1

	skill_description = ("MP Cost = 3 ; Duration = 4 turns ; Cooldown = 6 turns \n\nIncreases Elise's Buff Sensitivity by 30% \nIncreases Elise's Penetration by 30% \nIncreases Elise's Critical Rate by 35% \nIncreases Elise's Attack by 45%")

class Sweet_Tooth(Skill):
	def __init__(self):
		super(Sweet_Tooth, self).__init__("Sweet Tooth", 4, 0, 6, 0, 3, Storage_List = [0.0], Counter_List = [0])

	def casting(self,target):
		if self.Current_Duration > 0:
			self.Storage_List[0] = boss.get_HP()
			elise_atk = target.get_Atk()*(target.get_Buff_Atk()/target.get_Debuff_Atk())
			boss.HP_Modifier( - boss.get_Max_HP()*(0.05 + math.log( 1 + (math.exp(0.95) - 1) * (1 - math.exp(-0.001*(elise_atk**(1/2.5)))))))
			self.Storage_List[0] = boss.get_HP() - self.Storage_List[0]
			target.HP_Modifier(-self.Storage_List[0])

	skill_description = ("MP Cost = 3 ; Duration = 3 turns ; Cooldown = 6 turns \n\nSteals enemies' HP by (5% + % of Elise's Attack) of their Max HP every turn")

class Vampire_Rampage(Skill):
	def __init__(self):
		super(Vampire_Rampage, self).__init__("Vampire Rampage", 4, 0, 6, 0, 4, Storage_List = [0.0]*(N_characters), Counter_List = [0])

	def casting(self,target):
		if self.Current_Duration != 1:
			for n in range(0,N_characters):
				slots_personnages[n].HP += -slots_personnages[n].get_Max_HP()*0.12
			boss.HP_Modifier(-boss.get_Max_HP()*0.08)

		if self.Activation == 1 :
			if self.Current_Duration == 0:
				for n in range(0,N_characters):
					self.Storage_List[n] = slots_personnages[n].get_Buff_Atk()
					slots_personnages[n].Buff_Atk_Modifier(1.4)
					self.Storage_List[n] = slots_personnages[n].get_Buff_Atk() - self.Storage_List[n]

			elif self.Current_Duration > 0:
				self.Current_Duration = self.Duration

		if self.Current_Duration ==1:
			for n in range(0,N_characters):
					slots_personnages[n].Buff_Atk += -self.Storage_List[n]
			self.Current_Duration += -1

	skill_description = ("MP Cost = 4 ; Duration = 3 turns ; Cooldown = 6 turns \n\nDeals damage to party by 12% of their Max HP every turn \nDeals damage to enemies by 8% of their Max HP every turn \nIncreases party Attack by 40%")

#Alice's Skills
class Time_Acceleration(Skill):
	def __init__(self):
		super(Time_Acceleration, self).__init__("Time Acceleration", 0, 0, 5, 0, 4, Storage_List = [0.0], Counter_List = [0])

	def casting(self,target):
		for n in range(0,N_characters*3):
			if slots_skills_totaux[n].get_Current_Cooldown() > 0:
				slots_skills_totaux[n].Cooldown_Modifier(-2)

	skill_description = ("MP Cost = 4 ; Duration = 0 turn ; Cooldown = 5 turns \n\nDecreases party skill Cooldowns by 2 turns")

class Limit_Extend(Skill):
	def __init__(self):
		super(Limit_Extend, self).__init__("Limit Extend", 0, 0, 5, 0, 4, Storage_List = [0.0], Counter_List = [0])

	def casting(self,target):
		for n in range(0,N_characters*3):
			if slots_skills_totaux[n].get_Current_Duration() > 0:
				slots_skills_totaux[n].Duration_Modifier(2)
			for m in range(0, len(slots_skills_totaux[n].get_Counter_List())):
				if slots_skills_totaux[n].get_Counter_List()[m] > 0:
					slots_skills_totaux[n].Counter_Modifer(m, 2)

	skill_description = ("MP Cost = 4 ; Duration = 0 turn ; Cooldown = 5 turns \n\nIncreases party skill Durations by 2 turns")

class Clockwork_Protection(Skill):
	def __init__(self):
		super(Clockwork_Protection, self).__init__("Clockwork Protection", 4, 0, 5, 0, 2, Storage_List = [0.0]*(2*N_characters), Counter_List = [0])

	def casting(self,target):
		if self.Activation == 1 :

			if self.Current_Duration == 0:
				for n in range(0,N_characters):
					self.Storage_List[n] = slots_personnages[n].get_Buff_Def()
					slots_personnages[n].Buff_Def_Modifier(1.25)
					self.Storage_List[n] = slots_personnages[n].get_Buff_Def() - self.Storage_List[n]
				for n in range(N_characters, 2*N_characters):
					self.Storage_List[n] = slots_personnages[n-N_characters].get_Shield()
					slots_personnages[n-N_characters].Shield_Modifier(2000)
					self.Storage_List[n] = slots_personnages[n-N_characters].get_Shield() - self.Storage_List[n]

			elif self.Current_Duration > 0:
				self.Current_Duration = self.Duration

		if self.Current_Duration ==1:
			for n in range(0,N_characters):
					slots_personnages[n].Buff_Def += -self.Storage_List[n]
			for n in range(N_characters, 2*N_characters):
					slots_personnages[n-N_characters].Shield_Modifier(-self.Storage_List[n])
			self.Current_Duration += -1

	skill_description = ("MP Cost = 2 ; Duration = 3 turns ; Cooldown = 5 turns \n\nIncreases party Defense by 25% \nIncreases party Shield by 2 000")

#Hanae's Skills
class Soul_Conversion(Skill):
	def __init__(self):
		super(Soul_Conversion, self).__init__("Soul Conversion", 4, 0, 7, 0, 4, Storage_List = [0], Counter_List = [0])

	def casting(self,target):
		if self.Current_Duration > 0:
			self.Storage_List[0] = boss.get_MP()
			boss.MP_Modifier(-2)
			self.Storage_List[0] = self.Storage_List[0] - boss.get_MP()
			slots_personnages[random.randint(0, N_characters-1)].MP_Modifier(self.Storage_List[0])

	skill_description = ("MP Cost = 4 ; Duration = 3 turns ; Cooldown = 7 turns \n\nSteals up to 2 MP from enemies and randomly distribute them to one ally")
	
class Soul_Regeneration(Skill):
	def __init__(self):
		super(Soul_Regeneration, self).__init__("Soul Regeneration", 5, 0, 7, 0, 0, Storage_List = [0.0], Counter_List = [0])

	def casting(self,target):
		if self.Activation ==1:
			for n in range(0, N_characters):
				slots_personnages[n].R_MP_Modifier(1)
				slots_personnages[n].MP_Modifier(3)
			if self.Current_Duration > 0:
				self.Current_Duration = self.Duration

		if self.Current_Duration ==1:
			for n in range(0, N_characters):
				slots_personnages[n].R_MP_Modifier(-1)
			self.Current_Duration += -1

	skill_description = ("MP Cost = 0 ; Duration = 4 turns ; Cooldown = 7 turns \n\nIncreases party MP Regeneration by 1 \nIncreases party MP by 3 every turn")
	
class Soul_Expansion(Skill):
	def __init__(self):
		super(Soul_Expansion, self).__init__("Soul Expansion", 5, 0, 7, 0, 5, Storage_List = [0.0]*N_characters, Counter_List = [0])

	def casting(self,target):
		if self.Activation ==1:
			if self.Current_Duration == 0:
				for n in range(0, N_characters):
					slots_personnages[n].Max_HP_Modifier(3000)
					slots_personnages[n].Max_MP_Modifier(5)

					self.Storage_List[n] = slots_personnages[n].get_Shield()
					slots_personnages[n].Shield_Modifier(1000)
					self.Storage_List[n] = slots_personnages[n].get_Shield() - self.Storage_List[n]
					
			elif self.Current_Duration > 0:
				self.Current_Duration = self.Duration
		
		if self.Current_Duration ==1:
			for n in range(0, N_characters):
				slots_personnages[n].Max_HP_Modifier(-3000)
				slots_personnages[n].Max_MP_Modifier(-5)
				slots_personnages[n].Shield_Modifier(-self.Storage_List[n])
			self.Current_Duration += -1

	skill_description = ("MP Cost = 5 ; Duration = 4 turns ; Cooldown = 7 turns \n\nIncreases party Max HP by 3 000 \nIncreases party Max MP by 5 \nIncreases party Shield by 1 000")

#Junyoung's Skills
class Conqueror(Skill):
	def __init__(self):
		super(Conqueror, self).__init__("Conqueror", 6, 0, 15, 0, 7, Storage_List = [0.0]*5*N_characters, Counter_List = [0])

	def casting(self,target):
		if self.Current_Duration !=1:
			for n in range(0,N_characters*3):
				if slots_skills_totaux[n].get_Current_Cooldown() > 0:
					slots_skills_totaux[n].Cooldown_Modifier(-1)

			for n in range(0, N_characters):
				slots_personnages[n].HP_Modifier(target.get_Atk()*1.5)
				slots_personnages[n].MP_Modifier(1)
			boss.MP_Modifier(-1)

		if self.Activation ==1:
			if self.Current_Duration == 0:
				for n in range(0, N_characters):
					self.Storage_List[n] = slots_personnages[n].get_Shield()
					slots_personnages[n].Shield_Modifier(target.get_Atk()*4)
					self.Storage_List[n] = slots_personnages[n].get_Shield() - self.Storage_List[n]

				for n in range(N_characters, 2*N_characters):
					self.Storage_List[n] = slots_personnages[n-N_characters].get_Buff_Atk()
					slots_personnages[n-N_characters].Buff_Atk_Modifier(1.45)
					self.Storage_List[n] = slots_personnages[n-N_characters].get_Buff_Atk() - self.Storage_List[n]

				for n in range(2*N_characters, 3*N_characters):
					self.Storage_List[n] = slots_personnages[n-2*N_characters].get_Buff_Def()
					slots_personnages[n-2*N_characters].Buff_Def_Modifier(1.45)
					self.Storage_List[n] = slots_personnages[n-2*N_characters].get_Buff_Def() - self.Storage_List[n]

				for n in range(3*N_characters, 4*N_characters):
					self.Storage_List[n] = slots_personnages[n-3*N_characters].get_CR()
					slots_personnages[n-3*N_characters].CR_Modifier(30)
					self.Storage_List[n] = slots_personnages[n-3*N_characters].get_CR() - self.Storage_List[n]

				for n in range(4*N_characters, 5*N_characters):
					self.Storage_List[n] = slots_personnages[n-4*N_characters].get_C_DMG()
					slots_personnages[n-4*N_characters].C_DMG_Modifier(2.5)
					self.Storage_List[n] = slots_personnages[n-4*N_characters].get_C_DMG() - self.Storage_List[n]

			elif self.Current_Duration > 0:
				self.Current_Duration = self.Duration

		if self.Current_Duration ==1:
			for n in range(0, N_characters):
				slots_personnages[n].Shield += -self.Storage_List[n]

			for n in range(N_characters, 2*N_characters):
				slots_personnages[n-N_characters].Buff_Atk += -self.Storage_List[n]

			for n in range(2*N_characters, 3*N_characters):
				slots_personnages[n-2*N_characters].Buff_Def += -self.Storage_List[n]

			for n in range(3*N_characters, 4*N_characters):
				slots_personnages[n-3*N_characters].CR += -self.Storage_List[n]
			
			for n in range(4*N_characters, 5*N_characters):
				slots_personnages[n-4*N_characters].C_DMG += -self.Storage_List[n]

			self.Current_Duration += -1

	skill_description = ("MP Cost = 7 ; Duration = 5 turns ; Cooldown = 15 turns \n\nEvery turn, decreases party skill Cooldowns by 1, enemies' MP by 1, heals party and increases party MP by 1 \nIncreases party Shield \nIncreases party Attack by 45% \nIncreases party Defense by 45% \nIncreases party Critical Rate by 30% \nIncreases party Critical Damage by 250%")
	
class Domination(Skill):
	def __init__(self):
		super(Domination, self).__init__("Domination", 6, 0, 10, 0, 5, Storage_List = [0.0]*N_characters, Counter_List = [0])

	def casting(self,target):
		if self.Current_Duration !=1:
			boss.HP_Modifier(-boss.Max_HP*0.07)

		if self.Activation ==1:
			boss.MP_Modifier(-2)
			
			if self.Current_Duration == 0:
				
				self.Storage_List[0] = boss.get_Debuff_Sensitivity()
				boss.Debuff_Sensitivity_Modifier(1.35)
				self.Storage_List[0] = boss.get_Debuff_Sensitivity() - self.Storage_List[0]
				
				self.Storage_List[1] = boss.get_Penetration()
				boss.Penetration_Modifier(-20)
				self.Storage_List[1] = boss.get_Penetration() - self.Storage_List[1]

				self.Storage_List[2] = boss.get_CR()
				boss.CR_Modifier(-40)
				self.Storage_List[2] = boss.get_CR() - self.Storage_List[2]
				
				self.Storage_List[3] = boss.get_Debuff_Atk()
				boss.Debuff_Atk_Modifier(1/0.35)
				self.Storage_List[3] = boss.get_Debuff_Atk() - self.Storage_List[3]
			
			if self.Current_Duration > 0:
				self.Current_Duration = self.Duration
		
		if self.Current_Duration ==1:
			boss.Debuff_Sensitivity += -self.Storage_List[0]
			boss.Penetration += -self.Storage_List[1]
			boss.CR += -self.Storage_List[2]
			boss.Debuff_Atk += -self.Storage_List[3]
			self.Current_Duration += -1
			
	skill_description = ("MP Cost = 5 ; Duration = 5 turns ; Cooldown = 10 turns \n\nDeals damage to enemies by 7% of their Max HP every turn \nOn activation, decreases enemies' MP by 2 \nIncreases enemies' Debuff Sensitivity by 35% \nDecreases enemies' Penetration by 20% \nDecreases enemies' Critical Rate by 40% \nDecreases enemies' Attack by 65%")

class Coup_de_Grace(Skill):
	def __init__(self):
		super(Coup_de_Grace, self).__init__("Coup de Grace", 2, 0, 5, 0, 5, Storage_List = [0.0]*3*N_characters, Counter_List = [0]*N_characters)

	def casting(self,target):
		if self.Activation == 1:

			if self.Counter_List[global_target] == 0:
				self.Counter_List[global_target] = self.Duration
				
				self.Storage_List[global_target] = slots_personnages[global_target].get_Penetration()
				slots_personnages[global_target].Penetration_Modifier(40)
				self.Storage_List[global_target] = slots_personnages[global_target].get_Penetration() - self.Storage_List[global_target]
				
				self.Storage_List[global_target+N_characters] = slots_personnages[global_target].get_C_DMG()
				slots_personnages[global_target].C_DMG_Modifier(3+target.get_C_DMG()*0.3)
				self.Storage_List[global_target+N_characters] = slots_personnages[global_target].get_C_DMG()-self.Storage_List[global_target+N_characters]
				
				self.Storage_List[global_target+2*N_characters] = 0.0
				for i in range(N_characters):
					self.Storage_List[global_target+2*N_characters] += slots_personnages[i].get_Atk()*slots_personnages[i].get_Buff_Atk()/slots_personnages[i].get_Debuff_Atk()
				slots_personnages[global_target].Atk_Modifier(self.Storage_List[global_target+2*N_characters])

				boss.Buff_Atk = 1
				boss.Buff_Def = 1
				boss.Buff_Sensitivity = 1
				boss.Shield = 0
				boss_shield_bar['value'] = boss.get_Shield()
				
				for n in range(0, len(boss_skills)): #reset du storage des effets positifs pour éviter la contre variation
					boss_storage = boss_skills[n].get_Storage_List()
					for m in range(0, len(boss_storage)):
						if boss_storage[m] > 0:
							boss_storage[m] = 0

			elif self.Counter_List[global_target] > 0:
				self.Counter_List[global_target] = self.Duration

		for n in range (0,N_characters):
			if self.Counter_List[n] == 1:
				slots_personnages[n].Penetration += -self.Storage_List[n]
				slots_personnages[n].C_DMG += -self.Storage_List[n+N_characters]
				slots_personnages[n].Atk += -self.Storage_List[n+2*N_characters]
				self.Counter_List[n] += -1

		if self.Current_Duration ==1:
			self.Current_Duration += -1

	skill_description = ("MP Cost = 5 ; Duration = 0 turn ; Cooldown = 5 turns \n\nIncreases one target's Penetration by 40% \nIncreases one target's Critical Damage by 300% + 30% of Junyoung's Critical Damage \nIncreases one target's Attack by the sum of the whole party's attack \nDispells enemies")

#Leïla's Skills
class Clairance(Skill):
	def __init__(self):
		super(Clairance, self).__init__("Clairance", 0, 0, 4, 0, 5, Storage_List = [0.0]*N_characters, Counter_List = [0])

	def casting(self,target):
		if self.Activation ==1:
			if self.Current_Duration == 0:
				boss.Shield = 0
				boss_shield_bar['value'] = boss.get_Shield()
				boss.Buff_Atk = 1
				boss.Buff_Def = 1
				boss.Buff_Sensitivity = 1

				for n in range(0, len(boss_skills)): #reset du storage des effets positifs pour éviter la contre variation
					boss_storage = boss_skills[n].get_Storage_List()
					for m in range(0, len(boss_storage)):
						if boss_storage[m] > 0:
							boss_storage[m] = 0

				self.Storage_List[0] = boss.get_Debuff_Def()
				boss.Debuff_Def_Modifier(2)
				self.Storage_List[0] = self.Storage_List[0] - boss.get_Def()
				self.Storage_List[1] = boss.get_CR()
				boss.CR_Modifier(-30)
				self.Storage_List[1] = boss.get_CR() - self.Storage_List[1]
			elif self.Current_Duration > 0:
				self.Current_Duration = self.Duration

		if self.Current_Duration == 1:
			boss.Debuff_Def += -self.Storage_List[0]
			boss.CR_Modifier += -self.Storage_List[1]
			self.Current_Duration += -1

	skill_description = ("MP Cost = 5 ; Duration = 3 turns ; Cooldown = 4 turns \n\nDispells enemies \nDecreases enemies Defense by 50% \nDecreases enemies Critical Rate by 30%")

class Absorption(Skill):
	def __init__(self):
		super(Absorption, self).__init__("Absorption", 4, 0, 5, 0, 5, Storage_List = [0.0]*2*N_characters, Counter_List = [0]*N_characters)

	def casting(self,target):
		if self.Current_Duration != 1:
			for n in range(0, N_characters):
				slots_personnages[n].HP_Modifier(target.Heal_Amount() + 1000)
		
		if self.Activation == 1:

			if self.Counter_List[global_target] == 0:
				self.Counter_List[global_target] = self.Duration
				
				self.Storage_List[global_target] = boss.get_Debuff_Atk()
				self.Storage_List[global_target+N_characters] = boss.get_Atk()*boss.get_Buff_Atk()/boss.get_Debuff_Atk()

				boss.Debuff_Atk_Modifier(1/0.35)
				
				self.Storage_List[global_target] = boss.get_Debuff_Atk() - self.Storage_List[global_target]
				slots_personnages[global_target].Atk_Modifier(self.Storage_List[global_target+N_characters])

			elif self.Counter_List[global_target] > 0:
				self.Counter_List[global_target] = self.Duration

		for n in range(0, N_characters):
			if self.Counter_List[n] == 1:
				slots_personnages[n].Atk += -self.Storage_List[n+N_characters]
				boss.Debuff_Atk += - self.Storage_List[n]
				self.Counter_List[n] += -1

		if self.Current_Duration ==1:
			self.Current_Duration += -1

	skill_description = ("MP Cost = 5 ; Duration = 3 turns ; Cooldown = 5 turns \n\nSteals 35% of enemies's Attack and distribute them to one target")
	
class Malediction(Skill):
	def __init__(self):
		super(Malediction, self).__init__("Malédiction", 4, 0, 5, 0, 5, Storage_List = [0.0], Counter_List = [0])
	
	def casting(self,target):
		if self.Activation ==1:
			if self.Current_Duration == 0:
				self.Storage_List[0] = boss.get_Debuff_Sensitivity()
				boss.Debuff_Sensitivity_Modifier(1.3)
				self.Storage_List[0] = self.Storage_List[0] - boss.get_Debuff_Sensitivity()
			elif self.Current_Duration > 0:
				self.Current_Duration = self.Current_Duration

		if self.Current_Duration ==1:
			boss.Debuff_Sensitivity += self.Storage_List[0]
			self.Current_Duration += -1

	skill_description = ("MP Cost = 5 ; Duration = 3 turns ; Cooldown = 5 turns \n\nIncreases enemies's Debuff Sensitivity by 30%")

#Boss Skills
class Empty_Skill(Skill):
	def __init__(self):
		super(Empty_Skill, self).__init__("Empty Skill", 10, 10, 10, 10, 0, Storage_List = [0.0], Counter_List = [0])
	
	def casting(self, target):
		pass

class Hell_Flame(Skill):
	def __init__(self):
		super(Hell_Flame, self).__init__("Hell Flame", 0, 0, 5, 0, 5, Storage_List = [0.0], Counter_List = [0])

	def casting(self,target):
		slots_personnages[0].HP_Modifier(-target.Damage_Formula(slots_personnages[0])-2000)
		for n in range(1, N_characters):
			slots_personnages[n].HP_Modifier(-(target.Damage_Formula(slots_personnages[n])+2000)/2)

class Soul_Absorption(Skill):
	def __init__(self):
		super(Soul_Absorption, self).__init__("Soul Absorption", 0, 0, 5, 0, 5, Storage_List = [0.0]*N_characters, Counter_List = [0])

	def casting(self,target):
		total_mp = 0
		for i in range(0, N_characters):
			if slots_personnages[i].get_Status() ==1:
				self.Storage_List[i] = slots_personnages[i].get_MP()
				slots_personnages[i].MP_Modifier(-3)
				self.Storage_List[i] = slots_personnages[i].get_MP() - self.Storage_List[i]
				total_mp += self.Storage_List[i]
		boss.MP_Modifier(floor(-total_mp/3 + 1))

class Life_Absorption(Skill):
	def __init__(self):
		super(Life_Absorption, self).__init__("Life Absorption", 0, 0, 5, 0, 5, Storage_List = [0.0]*N_characters, Counter_List = [0])

	def casting(self,target):
		total_hp = 0
		for i in range(0, N_characters):
			if slots_personnages[i].get_Status() ==1:
				self.Storage_List[i] = slots_personnages[i].get_HP()
				slots_personnages[i].HP_Modifier(-boss.Damage_Formula(slots_personnages[i])/2.5)
				self.Storage_List[i] = slots_personnages[i].get_HP() - self.Storage_List[i]
				total_hp += self.Storage_List[i]
		boss.HP_Modifier(-total_hp*100 + boss.get_Max_HP()*0.07)
		boss.Shield += 2*boss.get_Max_HP()

class Cursed_Land(Skill):
	def __init__(self):
		super(Cursed_Land, self).__init__("Cursed Land", 6, 0, 7, 0, 5, Storage_List = [0.0]*2*N_characters, Counter_List = [0])

	def casting(self,target):
		if self.Current_Duration !=1:
			for i in range(0, N_characters):
				slots_personnages[i].HP += -slots_personnages[i].get_Max_HP()*0.25

		if self.Activation ==1:
			if self.Current_Duration ==0:
				for i in range(0, N_characters):
					if slots_personnages[i].get_Status() ==1:
						self.Storage_List[i] = slots_personnages[i].get_Debuff_Atk()
						self.Storage_List[i+N_characters] = slots_personnages[i].get_Debuff_Def()

						slots_personnages[i].Debuff_Atk_Modifier(3)
						slots_personnages[i].Debuff_Def_Modifier(3)

						self.Storage_List[i] = self.Storage_List[i] - slots_personnages[i].get_Debuff_Atk()
						self.Storage_List[i+N_characters] = self.Storage_List[i+N_characters] - slots_personnages[i].get_Debuff_Def()

		if self.Current_Duration ==1:
			for i in range(0, N_characters):
				if slots_personnages[i].get_Status() ==1:
					slots_personnages[i].Debuff_Atk += self.Storage_List[i]
					slots_personnages[i].Debuff_Def += self.Storage_List[i+N_characters]
			self.Current_Duration += -1

#Liste de personnages
class Hiro(General):
	def __init__(self):
		super(Hiro, self).__init__("Hiro", 3000, 3000, 0, 7, 0, 2, 8000, 2000, 30, 1, 15, 1)

	skill_list = (Acid_Demonstration, Cocktail_Overdrive, Sulfuric_Bomb)

class Seyren(General):
	def __init__(self):
		super(Seyren, self).__init__("Seyren", 4000, 4000, 0, 5, 0, 1, 12000, 3000, 20, 1.5, 20, 1.15)

	skill_list = (Ignition_Break, Target_Weakness, Acute_Senses)

class Raphaela(General):
	def __init__(self):
		super(Raphaela, self).__init__("Raphaela", 20000, 20000, 0, 5, 0, 1, 1000, 3000, 0, 0.5, 0, 1)

	skill_list = (Revitalize, Fortress, Coercion)

class Jibril(General):
	def __init__(self):
		super(Jibril, self).__init__("Jibril", 5000, 5000, 0, 7, 0, 2, 2000, 3000, 20, 1, 0, 1)

	skill_list = (Path_Of_Light, Sanctuary, Piety)

class Lucias(General):
	def __init__(self):
		super(Lucias, self).__init__("Lucias", 6000, 6000, 0, 8, 0, 2, 3000, 3000, 30, 1, 0, 1)

	skill_list = (Renovatio, Curatio, Expiatio)

class Clause(General):
	def __init__(self):
		super(Clause, self).__init__("Clause", 13000, 13000, 0, 5, 0, 1, 2000, 20000, 0, 0.5, 0, 1)

	skill_list = (Endure, Pierce, Hide_Weakness)

class Cassius(General):
	def __init__(self):
		super(Cassius, self).__init__("Cassius", 5000, 5000, 10000, 7, 0, 2, 5000, 7000, 0, 0.5, 0, 1.4)

	skill_list = (Light_Domain, Empower, Serenity)

class Elise(General):
	def __init__(self):
		super(Elise, self).__init__("Elise", 3000, 3000, 0, 7, 0, 2, 6000, 3000, 30, 1.5, 15, 1.15)

	skill_list = (Hunter_Instinct, Sweet_Tooth, Vampire_Rampage)

class Alice(General):
	def __init__(self):
		super(Alice, self).__init__("Alice", 5000, 5000, 0, 7, 0, 2, 1000, 4500, 0, 1, 0, 1)

	skill_list = (Time_Acceleration, Limit_Extend, Clockwork_Protection)

class Hanae(General):
	def __init__(self):
		super(Hanae, self).__init__("Hanae", 5000, 5000, 0, 9, 0, 2, 2000, 4000, 0, 1, 0, 1)

	skill_list = (Soul_Conversion, Soul_Regeneration, Soul_Expansion)

class Junyoung(General):
	def __init__(self):
		super(Junyoung, self).__init__("Junyoung", 6000, 6000, 0, 9, 0, 3, 4000, 4000, 30, 1, 0, 1)

	skill_list = (Conqueror, Domination, Coup_de_Grace)

class Leila(General):
	def __init__(self):
		super(Leila, self).__init__("Leïla", 5000, 5000, 0, 7, 0, 2, 1000, 4000, 30, 1, 0, 1)

	skill_list = (Clairance, Absorption, Malediction)

class Hydra(General):
	def __init__(self):
		super(Hydra, self).__init__("Hydra", 150000000, 150000000, 300000000, 15, 0, 5, 50000, 500000, 60, 3, 45, 1)

	skill_list = (Cursed_Land, Hell_Flame, Soul_Absorption, Life_Absorption)

class Galgoria(General):
	def __init__(self):
		super(Galgoria, self).__init__("Galgoria", 12000000, 12000000, 0, 10, 3, 2, 15000, 40000, 60, 1, 30, 1)

	skill_list = (Hell_Flame, Cursed_Land)

class Lucifer(General):
	def __init__(self):
		super(Lucifer, self).__init__("Lucifer", 2000000, 2000000, 0, 10, 3, 0, 10000, 10000, 20, 2, 15, 1)

	skill_list = (Empty_Skill, Empty_Skill)

class Sac_de_Sable_Man(General):
	def __init__(self):
		super(Sac_de_Sable_Man, self).__init__("Sac de Sable-Man", 139000000000, 139000000000, 0, 10, 0, 0, 0, 0, 0, 0, 0, 1)

	skill_list = (Empty_Skill, Empty_Skill)

char_list = (Hiro, Seyren, Raphaela, Jibril, Lucias, Clause, Cassius, Elise, Alice, Hanae, Junyoung, Leila)
noms_char_list = ("Hiro", "Seyren", "Raphaela", "Jibril", "Lucias", "Clause", "Cassius", "Elise", "Alice", "Hanae", "Junyoung", "Leïla")

boss_list = (Sac_de_Sable_Man, Lucifer, Galgoria, Hydra)              #class liste de boss
noms_boss_list = ("Sac de Sable-Man", "Lucifer", "Galgoria", "Hydra") #tuple des noms des boss
boss_N_list = (8, 4, 6, 8)                                            #on affronte le boss i dans boss_list avec boss_N_list[i] personnages
N_characters = 0 #initialisation de certaines variables
slots_personnages = [0]
current_team = ' '
boss = Hydra()

def fight_bosses():
	main_menu_1.destroy()
	second_menu_11.pack(expand = True)
	second_menu_12.pack(expand = True)
	second_menu_13.pack(expand = True)
	second_menu_14.pack(expand = True)

def boss_choice(n):

	global N_characters       #il faut mettre en global dans la fonction et non dans le corps du texte
	global slots_personnages  #sinon les valeurs ne sont pas correctement sauvegardées parce que python c'est nul
	global boss               #note to self : si besoin d'une variable qui se transmet de bouton en bouton => global dans def du bouton
	global boss_hp_bar, boss_mp_bar, boss_skills, current_team, boss_shield_bar

	N_characters = boss_N_list[n]           #choix du boss
	boss = boss_list[n]()                   #instanciation boss
	slots_personnages = [0]*N_characters    #liste de stockage des slots pour permettre au code de parcourir automatiquement les slots personnages
	boss_skills = [0]*len(boss.get_skill_list()) #liste de skill boss
	for i in range(0, len(boss.get_skill_list())):
		cast = boss.get_skill_list()[i]
		boss_skills[i] = cast()
	second_menu_11.destroy() #destruction des frames précédentes
	second_menu_12.destroy()
	second_menu_13.destroy()
	second_menu_14.destroy()
	third_menu_11.pack(expand =True) #pack() des nouvelles frames
	third_menu_12.pack(expand =True)
	third_menu_111.pack()
	third_menu_112.pack()
	third_menu_121.pack(fill = 'x') #fill x pour ajuster les longueurs en x
	third_menu_122.pack(fill = 'x')
	third_menu_123.pack(fill = 'x')
	third_menu_124.pack(fill = 'x')
	third_menu_125.pack(side = BOTTOM, fill = 'x')
	number_chara_select.config(text=N_characters)
	#création des barres de Shield, HP et MP du Boss
	boss_shield_bar = ttk.Progressbar(battle_frame_1[1], style = "Shield.Horizontal.TProgressbar", orient = HORIZONTAL, length=300, mode='determinate', value = boss.get_Shield(), max = boss.get_Shield())
	boss_shield_bar.pack()
	boss_hp_bar = ttk.Progressbar(battle_frame_1[1], style = "HP.Horizontal.TProgressbar", orient = HORIZONTAL, length=300, mode='determinate', value = boss.get_HP(), max = boss.get_Max_HP())
	boss_hp_bar.pack()
	boss_mp_bar = ttk.Progressbar(battle_frame_1[1], style = "MP.Horizontal.TProgressbar", orient = HORIZONTAL, length=300, mode='determinate', value = boss.get_MP(), max = boss.get_Max_MP())
	boss_mp_bar.pack()

def Chara_Instanciation(Chara):
	global current_team, slots_personnages
	i = 0
	Flag = True
	while Flag : #boucle qui vérifie quel slot est disponible pour accueillir une instance de Chara
		if slots_personnages[i] == 0:
			slots_personnages[i] = Chara()
			Flag = False
		elif slots_personnages[i] != 0:
			i += 1
	current_team += slots_personnages[i].get_Name() + ', ' #création du texte pour le Label qui affiche les personnages sélectionnés
	if i == N_characters-1: #texte final quand i a parcouru tous les slots personnages
		current_team = current_team[:len(current_team)-2]  # ==> on supprime la virgule et l'espace que quand toute la team est réunie
	current_team_select.config(text=current_team) #modification du texte du Label

def redo_team():
	global current_team
	global slots_personnages
	current_team = ' ' #reset du texte du Label
	current_team_select.config(text=current_team)
	slots_personnages = [0]*N_characters

def start_battle():
	third_menu_11.destroy() #destruction et pack des frames nécessaires
	third_menu_12.destroy()
	battle_frame_1[0].pack(side = LEFT)
	battle_frame_1[1].pack(side = RIGHT)

	for i in range(0,2):
		battle_frame_11[i].pack(side = RIGHT)
	for i in range(0,5):
		battle_frame_111[i].pack(padx=5, pady=5, side = TOP)
	for i in range(0,N_characters-2):
		battle_frame_1111[i].pack(padx = 5, side = RIGHT)
	for i in range(0,16):
		battle_frame_11111[i].pack(side = TOP, expand = True, fill = X)
	for i in range(0,16):
		battle_frame_6[i].pack(side = TOP, expand = True, fill = X)
	for i in range(0,8):
		battle_frame_7[i].pack(side = LEFT, expand = True, fill = X)
	for i in range(0,8):
		battle_frame_8[i].pack(side = RIGHT)
		
	boss_HP.config(text=boss.get_Name())

	global perso_target_button, perso_shield_bar, perso_hp_bar, perso_mp_bar, button_skills_perso, noms_persos_instanciés, skill_input_list
	global slots_action, Turn #pour tracker les actions des persos
	
	noms_persos_instanciés = ' '                #tuple vide pour acceuillir les noms des persos instanciés
	for i in range(0,N_characters):             #boucle de remplissage du tuple
		noms_persos_instanciés += slots_personnages[i].get_Name() + ', '
	noms_persos_instanciés = noms_persos_instanciés[:len(noms_persos_instanciés)-2] #suppression de l'espace et de la virgule en trops

	Turn = 1 #initialisation de tout plein de variables
	slots_action = [0]*N_characters
	perso_target_button = [0]*N_characters
	perso_shield_bar = [0]*N_characters
	perso_hp_bar = [0]*N_characters
	perso_mp_bar = [0]*N_characters
	button_skills_perso = [0]*3*N_characters
	button_skill_description = [0]*3*N_characters
	button_attack_perso = [0]*N_characters
	button_block_perso = [0]*N_characters

	next_turn_button.pack(pady = 40)
	turn_number.pack()
	champs.pack(pady = 20, fill = X)
	
	#création de toutes les barres de Shield, HP et MP des persos dans les bonnes frames
	for i in range(0,N_characters):
		button_attack_perso[i] = Button(battle_frame_11111[2*i], text="AA", font =("Arial", 18), bg='#fff3f5', fg='black', command=partial(attack_action, i))
		button_block_perso[i] = Button(battle_frame_11111[2*i], text="B", font =("Arial", 18), bg='#fff3f5', fg='black', command=partial(block_action, i))
		perso_target_button[i] = Button(battle_frame_11111[2*i], text=slots_personnages[i].get_Name(), font =("Arial", 18), bg='#fff3f5', fg='black', command=partial(target_button, i))

		perso_shield_bar[i] = ttk.Progressbar(battle_frame_6[2*i], style = "Shield.Horizontal.TProgressbar", orient = HORIZONTAL, length=220, mode='determinate', value = slots_personnages[i].get_Shield(), max = slots_personnages[i].get_Shield())
		perso_hp_bar[i] = ttk.Progressbar(battle_frame_6[2*i], style = "HP.Horizontal.TProgressbar", orient = HORIZONTAL, length=220, mode='determinate', value = slots_personnages[i].get_HP(), max = slots_personnages[i].get_Max_HP())
		perso_mp_bar[i] = ttk.Progressbar(battle_frame_6[2*i], style = "MP.Horizontal.TProgressbar", orient = HORIZONTAL, length=220, mode='determinate', value = slots_personnages[i].get_MP(), max = slots_personnages[i].get_Max_MP())

		perso_target_button[i].pack(side = LEFT, expand = True, fill = 'both')
		button_attack_perso[i].pack(side = LEFT)
		button_block_perso[i].pack(side = LEFT)
		perso_shield_bar[i].pack()
		perso_hp_bar[i].pack()
		perso_mp_bar[i].pack()

		for j in range(3*i,3*i+3):
			button_skills_perso[j] = Button(battle_frame_7[i], text=slots_skills_totaux[j].get_Name(), font =("Arial", 11), bg='#fff3f5', fg='black', command=partial(skill_action, j))
			button_skill_description[j] = Button(battle_frame_8[i], text='', font =("Arial", 11), bg='#fff3f5', fg='black', command=partial(skill_description, j))
			button_skills_perso[j].pack(expand = True, fill = 'both')
			button_skill_description[j].pack(side = TOP, fill = 'both')

def confirm():
	global total_skill_list
	global slots_skills_totaux

	total_skill_list = []*N_characters
	for i in range(0, N_characters):
		total_skill_list += slots_personnages[i].get_skill_list() #dressage de la liste totale de skills

	slots_skills_totaux = [0]*(N_characters*3)                    #liste de stockage des instances

	for i in range(0,N_characters*3):
		cast = total_skill_list[i]              #on prend l'élément i de la liste de skill
		slots_skills_totaux[i] = cast()         #on instancie le skill i et son instance est stocké dans la position i de la liste de stockage

def skill_action(n):
	global compteur_action, slots_action, slots_skills_totaux, slots_personnages, boss, alpha
	alpha = floor(n/3)
	if slots_personnages[alpha].get_Status() ==1:
		if slots_action[alpha] ==0:
			if slots_personnages[alpha].get_MP() >= slots_skills_totaux[n].get_MP_Cost():    #comparaison entre MP du personnage et MP Cost du skill
				if slots_skills_totaux[n].get_Current_Cooldown() == 0:                       #vérification du cooldown
					if slots_skills_totaux[n].get_Activation() == 0:                         #vérification que le perso n'est pas sous silence
						slots_skills_totaux[n].Activation_Modifier(1)                        #première activation du skill = 1 (true)
						slots_skills_totaux[n].Cooldown_Equalizer()                          #activation du cooldown du skill
						slots_skills_totaux[n].casting(slots_personnages[alpha])             #activation des effets du skill
						slots_skills_totaux[n].Duration_Equalizer()                                   #activation de la durée du skill
						slots_personnages[alpha].MP_Modifier(-slots_skills_totaux[n].get_MP_Cost())   #consommation de MP
						slots_action[alpha] = 2
						champs.delete(0, END)
						champs.insert(0, slots_personnages[alpha].get_Name() + " has casted " + slots_skills_totaux[n].get_Name() + " !")
				else:
					print("\nSkill is on cooldown !")            #message d'erreur
					champs.delete(0, END)
					champs.insert(0, "Skill is on cooldown !")
			else:
				print("\nNot enough MP !")                       #message d'erreur
				champs.delete(0, END)
				champs.insert(0, "Not enough MP !")
		else :
			print("\nAction already taken !")
			champs.delete(0, END)
			champs.insert(0, "Action already taken !")

	if boss.get_HP() <= 0:
		battle_frame_1[0].destroy()
		battle_frame_1[1].destroy()
		end_label_2.pack(expand = True)

def skill_description(n):
	global slots_skills_totaux
	messagebox.showinfo(title=slots_skills_totaux[n].get_Name(), message=slots_skills_totaux[n].get_skill_description())

def target_button(n):
	global global_target
	global_target = n
	
def attack_action(n):
	global compteur_action, slots_action, boss
	if slots_personnages[n].get_Status() ==1:
		if slots_action[n] ==0:
			slots_action[n] = 1
			boss.HP_Modifier(-slots_personnages[n].Damage_Formula(boss))
			champs.delete(0, END)
			champs.insert(0, "Boss'HP damaged by " + str(slots_personnages[n].Damage_Formula(boss)))
		else :
			print("\nAction already taken !")
			champs.delete(0, END)
			champs.insert(0, "Action already taken !")

	if boss.get_HP() <= 0:
		battle_frame_1[0].destroy()
		battle_frame_1[1].destroy()
		end_label_2.pack(expand = True)

def block_action(n):
	global compteur_action, slots_action
	if slots_personnages[n].get_Status() ==1:
		if slots_action[n] ==0:
			slots_action[n] = 3
		else :
			print("\nAction already taken !")
			champs.delete(0, END)
			champs.insert(0, "Action already taken !")

def finish_turn():
	global Turn, slots_personnages, boss, N_characters, slots_skills_totaux, slots_action, turn_number, boss_skills

	slots_action = [0]*N_characters #reset des actions personnages

	i = 0
	Flag = True
	while Flag : #boucle pour chercher les personnages en vie et les attaquer
		if slots_personnages[i].get_Status() == 1:
			boss_target = i
			Flag = False
		elif slots_personnages[i].get_Status() == 0:
			i += 1

	dmg = boss.Damage_Formula(slots_personnages[boss_target]) #précalcul des dégâts du boss pour le block

	boss_action = 0
	if boss.get_HP() > 0 :
		if boss.get_MP() >= 5:
			i = 0
			Flag = True
			while Flag : #boucle pour chercher les skills utilisables
				if boss_skills[i].get_Current_Cooldown() == 0:
					if boss_skills[i].get_Activation() == 0:
						boss_skills[i].Activation_Modifier(1)
						boss_skills[i].casting(boss)
						boss_skills[i].Cooldown_Equalizer()
						boss_skills[i].Duration_Equalizer()
						boss_action = 1
						boss.MP_Modifier(-5)
						champs.delete(0, END)
						champs.insert(0, boss.get_Name() + " has casted " + boss_skills[i].get_Name() + " !")
						Flag = False
					elif boss_skills[i].get_Activation() != 0:
						i += 1
						if i == len(boss_skills): #si le compteur i est égal au nombre de skills du Boss, on a parcouru tous les skills
							Flag = False          #et aucun n'est utilisable donc sortie de boucle : vive les drapeaux
				elif boss_skills[i].get_Current_Cooldown() != 0:
					i += 1 #on passe au skill suivant si le skill est sous cooldown
					if i == len(boss_skills): #idem si on a fait le tour des skills
						Flag = False

		#calcul des dégats reçu en fonction de block ou non
		if slots_action[boss_target] == 3:
			if boss_action == 0:
				slots_personnages[boss_target].HP_Modifier(-0.7*dmg) #block

		elif slots_action[boss_target] != 3:
			if boss_action == 0:
				slots_personnages[boss_target].HP_Modifier(-dmg) #pas block

	#régénération des MP en fin de tour
	for n in range(0,N_characters):
		slots_personnages[n].MP_Modifier(slots_personnages[n].get_R_MP())
	boss.MP_Modifier(boss.get_R_MP())

	#décrémentation des cooldowns et des durées des skills activés, set de la première activation à 0 (false)
	for n in range(0,N_characters*3):
		if slots_skills_totaux[n].get_Current_Cooldown() > 0: #décrémentation des cooldowns
			slots_skills_totaux[n].Cooldown_Modifier(-1)

		if slots_skills_totaux[n].get_Current_Duration() > 0: #décrémentation des durées
			slots_skills_totaux[n].Duration_Modifier(-1)

		if slots_skills_totaux[n].get_Activation() != 0: #set de la première activation à 0 (false)
			slots_skills_totaux[n].Activation_Canceler()

		for m in range(0, len(slots_skills_totaux[n].get_Counter_List())): #décrémentation des durées propres
			if slots_skills_totaux[n].get_Counter_List()[m] > 0:
				slots_skills_totaux[n].Counter_Modifer(m, -1)

	for n in range(0, len(boss_skills)):
		if boss_skills[n].get_Current_Cooldown() > 0: #décrémentation des cd du boss
			boss_skills[n].Cooldown_Modifier(-1)
		if boss_skills[n].get_Current_Duration() > 0: #décrémentation des durées du boss
			boss_skills[n].Duration_Modifier(-1)
		if boss_skills[n].get_Activation() != 0:      #set de la première activation à 0 (false)
			boss_skills[n].Activation_Canceler()
	#début du nouveau tour : incrémentation du nombre de tour
	Turn += 1
	turn_number.config(text = ("Turn n° :", Turn))
	
	#Réactivation des effets des skills actifs sur la durée
	for n in range(0,N_characters):
		for m in range(3*n, 3*n+3):
			if slots_skills_totaux[m].get_Current_Duration() > 0:
				slots_skills_totaux[m].casting(slots_personnages[n])

	for n in range(0, len(boss_skills)):
		if boss_skills[n].get_Current_Duration() > 0:
			boss_skills[n].casting(boss)

	compteur_alive = 0
	#affichage des stats de tous les persos et du boss
	for n in range(0,N_characters):
		slots_personnages[n].affichage_stat()
		#boucle pour compter les personnages en vie => si compteur = 0 : Game Over !
		if slots_personnages[n].get_Status() == 1: 
			compteur_alive += 1
		elif slots_personnages[n].get_Status() == 0:
			compteur_alive += 0

	boss.affichage_stat()

	if compteur_alive == 0: #vérification s'il reste des persos en vie
		battle_frame_1[0].destroy()
		battle_frame_1[1].destroy()
		end_label_1.pack(expand = True)
	if boss.get_HP() <= 0: #vérification si le boss est mort
		battle_frame_1[0].destroy()
		battle_frame_1[1].destroy()
		end_label_2.pack(expand = True)

def Start():
	pass
	# for widget in window.winfo_children():
	# 	widget.destroy()
	# 	execute = Initialization()

window = Tk() #création de la fenêtre du code

window.title("PC Fantasy") #titre de la fenêtre
window.minsize(1080,600)   #dimensions min |
#window.maxsize(1080,600)  #dimensions max | bloquer la taille de la fenêtre
window.config(background='#fff3f5') #couleur de fond

top_menu = Menu(window, bg='#fff3f5')                    #création menu déroulant
menu_option = Menu(top_menu, bg='#fff3f5', tearoff=0)    #création option dans le menu
menu_option.add_command(label="Start", command=Start)    #commande de l'option + label
top_menu.add_cascade(label="Menu", menu=menu_option)     #menu en cascade

#style des barres de Shield, HP et MP
Shield_color = ttk.Style()
Shield_color.theme_use('alt')
Shield_color.configure("Shield.Horizontal.TProgressbar", foreground='#f5f5f5', background='#f5f5f5')

HP_color = ttk.Style()
HP_color.configure("HP.Horizontal.TProgressbar", foreground='#cbffc0', background='#cbffc0')

MP_color = ttk.Style()
MP_color.configure("MP.Horizontal.TProgressbar", foreground='#c0cbff', background='#c0cbff')

#frame premier menu
main_menu_1 = Frame(window, bg='#fff3f5')
main_menu_2 = Frame(window, bg='#fff3f5')
#frames du deuxième : choix du boss
second_menu_11 = Frame(window, bg='#fff3f5')
second_menu_12 = Frame(window, bg='#fff3f5')
second_menu_13 = Frame(window, bg='#fff3f5')
second_menu_14 = Frame(window, bg='#fff3f5')
#frames du troisième : choix équipe
third_menu_11 = Frame(window, bg='#fff3f5') #division écran en haut/bas
third_menu_12 = Frame(window, bg='#fff3f5')

third_menu_111 = Frame(third_menu_11, bg='#fff3f5') #subdivision de la moitié haute : message de choix équipe
third_menu_112 = Frame(third_menu_11, bg='#fff3f5') #subdivision de la moitié haute : composition actuelle de l'équipe

third_menu_121 = Frame(third_menu_12, bg='#fff3f5') #subidivions de la moitié basse montrant les persos à sélectionner
third_menu_122 = Frame(third_menu_12, bg='#fff3f5')
third_menu_123 = Frame(third_menu_12, bg='#fff3f5')
third_menu_124 = Frame(third_menu_12, bg='#fff3f5')
third_menu_125 = Frame(third_menu_12, bg='#fff3f5')

#battle frame
battle_frame_1 = [0]*2
for i in range(0,2):
	battle_frame_1[i] = Frame(window, bg='#fff3f5') #subdivision écran en droite/gauche

battle_frame_11 = [0]*2
for i in range(0,2):
	battle_frame_11[i] = Frame(battle_frame_1[0], bg='#fff3f5') # deux frames côté personnage

battle_frame_111 = [0]*5
for i in range(0,2):
	battle_frame_111[i] = Frame(battle_frame_11[0], bg='#fff3f5') #                        (4   3)  /  1 (frame 11[0])
for i in range(2,5):                                              # matrice de perso :     (6   5)  /  2 (frame 11[1])
	battle_frame_111[i] = Frame(battle_frame_11[1], bg='#fff3f5') #                        (8   7)

battle_frame_1111 = [0]*6
n = 2
for i in range(2,5):                                                    #                             4  /  3
	for j in range(i-n,i-n+2):                                          # division des sous groupes : 6  /  5
		battle_frame_1111[j] = Frame(battle_frame_111[i], bg='#fff3f5') #                             8  /  7
	n += -1

battle_frame_11111 = [0]*16
for i in range(0,2):
	for j in range(2*i,2*i+2):                                            #                       ( Perso / AA / B )
		battle_frame_11111[j] = Frame(battle_frame_111[i], bg='#fff3f5')  #                       |     Shield     |
for i in range(0,6):													  # séparation en :       |       HP       |
	for j in range(2*i+4,2*i+6):										  #						  |       MP       |
		battle_frame_11111[j] = Frame(battle_frame_1111[i], bg='#fff3f5') #						  |  Skills + ...  |

battle_frame_6 = [0]*16                                                    # séparation des boutons skills et boutons
for i in range(0,8):                                                       # de description des skills
	for j in range(2*i,2*i+2):                                             #
		battle_frame_6[j] = Frame(battle_frame_11111[2*i+1], bg='#fff3f5') #

battle_frame_7 = [0]*8
for i in range(0,8):
	battle_frame_7[i] = Frame(battle_frame_6[2*i+1], bg='#fff3f5')

battle_frame_8 = [0]*8
for i in range(0,8):
	battle_frame_8[i] = Frame(battle_frame_6[2*i+1], bg='#fff3f5')

fight_button = Button(main_menu_1, text="Fight Bosses", font =("Arial", 30), bg='#fff3f5', fg='black', command=fight_bosses)
fight_button.pack() #affichage du bouton pour accéder au choix du boss

Sac_de_Sable_Man_button = Button(second_menu_11, text="Fight Sac de Sable-Man", font =("Arial", 30), bg='#fff3f5', fg='black', command=lambda:boss_choice(0))
Sac_de_Sable_Man_button.pack()

Lucifer_button = Button(second_menu_12, text="Fight Lucifer", font =("Arial", 30), bg='#ff1a1a', fg='black', command=lambda:boss_choice(1))
Lucifer_button.pack()

Galgoria_button = Button(second_menu_13, text="Fight Galgoria", font =("Arial", 30), bg='#e60000', fg='black', command=lambda:boss_choice(2))
Galgoria_button.pack()

Hydra_Boss_button = Button(second_menu_14, text="Fight Hydra", font =("Arial", 30), bg='#b30000', fg='black', command=lambda:boss_choice(3))
Hydra_Boss_button.pack()

character_select_message = Label(third_menu_111, text="Choose characters to make your team ! Number allowed :", font=("Arial", 18), bg='#fff3f5', fg='black')
character_select_message.pack(side = LEFT)

number_chara_select = Label(third_menu_111, text=N_characters, font=("Arial", 18), bg='#fff3f5', fg='black')
number_chara_select.pack(side = LEFT)

current_team_select = Label(third_menu_112, text=current_team, font=("Arial", 18), bg='#fff3f5', fg='black')
current_team_select.pack(side = BOTTOM)
#boutons de sélection de personnages
Hiro_select_button = Button(third_menu_121, text="Hiro", font=("Arial", 18), bg='#fff3f5', fg='black', command=lambda:Chara_Instanciation(Hiro))
Hiro_select_button.pack(expand = 1, side = LEFT, fill = 'both')
Seyren_select_button = Button(third_menu_121, text="Seyren", font=("Arial", 18), bg='#fff3f5', fg='black', command=lambda:Chara_Instanciation(Seyren))
Seyren_select_button.pack(expand = 1, side = LEFT, fill = 'both')
Raphaela_select_button = Button(third_menu_121, text="Raphaela", font=("Arial", 18), bg='#fff3f5', fg='black', command=lambda:Chara_Instanciation(Raphaela))
Raphaela_select_button.pack(expand = 1, side = LEFT, fill = 'both')
Jibril_select_button = Button(third_menu_121, text="Jibril", font=("Arial", 18), bg='#fff3f5', fg='black', command=lambda:Chara_Instanciation(Jibril))
Jibril_select_button.pack(expand = 1, side = LEFT, fill = 'both')
Lucias_select_button = Button(third_menu_122, text="Lucias", font=("Arial", 18), bg='#fff3f5', fg='black', command=lambda:Chara_Instanciation(Lucias))
Lucias_select_button.pack(expand = 1, side = LEFT, fill = 'both')
Clause_select_button = Button(third_menu_122, text="Clause", font=("Arial", 18), bg='#fff3f5', fg='black', command=lambda:Chara_Instanciation(Clause))
Clause_select_button.pack(expand = 1, side = LEFT, fill = 'both')
Cassius_select_button = Button(third_menu_122, text="Cassius", font=("Arial", 18), bg='#fff3f5', fg='black', command=lambda:Chara_Instanciation(Cassius))
Cassius_select_button.pack(expand = 1, side = LEFT, fill = 'both')
Elise_select_button = Button(third_menu_122, text="Elise", font=("Arial", 18), bg='#fff3f5', fg='black', command=lambda:Chara_Instanciation(Elise))
Elise_select_button.pack(expand = 1, side = LEFT, fill = 'both')
Alice_select_button = Button(third_menu_123, text="Alice", font=("Arial", 18), bg='#fff3f5', fg='black', command=lambda:Chara_Instanciation(Alice))
Alice_select_button.pack(expand = 1, side = LEFT, fill = 'both')
Hanae_select_button = Button(third_menu_123, text="Hanae", font=("Arial", 18), bg='#fff3f5', fg='black', command=lambda:Chara_Instanciation(Hanae))
Hanae_select_button.pack(expand = 1, side = LEFT, fill = 'both')
Junyoung_select_button = Button(third_menu_123, text="Junyoung", font=("Arial", 18), bg='#fff3f5', fg='black', command=lambda:Chara_Instanciation(Junyoung))
Junyoung_select_button.pack(expand = 1, side = LEFT, fill = 'both')
Leïla_select_button = Button(third_menu_123, text="Leïla", font=("Arial", 18), bg='#fff3f5', fg='black', command=lambda:Chara_Instanciation(Leila))
Leïla_select_button.pack(expand = 1, side = LEFT, fill = 'both')

Redo_button = Button(third_menu_125, text="Redo team", font=("Arial", 18), bg='#fff3f5', fg='black', command=redo_team)
Redo_button.pack(expand = 1, side = LEFT, fill = 'both')

Confirm_button = Button(third_menu_125, text="Confirm", font=("Arial", 18), bg='#fff3f5', fg='black', command=confirm)
Confirm_button.pack(expand = 1, side = LEFT, fill = 'both')

Start_button = Button(third_menu_125, text="Start battle", font=("Arial", 18), bg='#fff3f5', fg='black', command=start_battle)
Start_button.pack(expand = 1, side = RIGHT, fill = 'both')

boss_HP = Label(battle_frame_1[1], text=boss.get_Name(), font=("Arial", 18), bg='#fff3f5', fg='black')
boss_HP.pack()

next_turn_button = Button(battle_frame_1[1], text="Finish turn", font=("Arial", 18), bg='#fff3f5', fg='black', command=finish_turn)
Turn = 1
turn_number = Label(battle_frame_1[1], text=("Turn n° :", Turn), font=("Arial", 18), bg='#fff3f5', fg='black')
champs = Entry(battle_frame_1[1], font=("Arial", 12), bg = '#fff3f5', fg='black')
#label de fin de jeu
end_label_1 = Label(window, text="Game Over : You Lost !!", font=("Arial", 30), bg='#fff3f5', fg='black')
end_label_2 = Label(window, text="Congratulation : You Won !!", font=("Arial", 30), bg='#fff3f5', fg='black')

main_menu_1.pack(expand = True)

window.config(menu=top_menu) #affichage du menu
window.mainloop()
