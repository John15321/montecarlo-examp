#105-Manim Example | How to Show Bar Chart in Manim
from shutil import move
from typing_extensions import runtime
from manim import *
from scipy.fftpack import shift

class MeleeWeapon:
    def __init__(self,name,S,AP,D):
        self.name = name
        self.S =S 
        self.AP =AP 
        self.D =D 

class Model:
    def __init__(self, name, WS, BS, S, T, W, A, SV, ISV):
        self.name = name
        self.WS = WS
        self.BS = BS
        self.S = S
        self.T = T
        self.W = W
        self.A = A
        self.SV = SV
        self.ISV = ISV
        self.Mweapon = MeleeWeapon("Power klaw",self.S*2,-3,2)
    def makeMeleeAtack(self,T,SV,ISV):
        attacks=np.random.randint(1,7,self.A)
        attacks_hited = np.count_nonzero(attacks>=self.WS)
        wounding_attacks = np.random.randint(1,7,attacks_hited)
        attacks_wound = (self.Mweapon.S>=2*T)*np.count_nonzero(wounding_attacks>=2)+(self.Mweapon.S>=T)*(self.Mweapon.S<2*T)*np.count_nonzero(wounding_attacks>=3)+(self.Mweapon.S==T)*np.count_nonzero(wounding_attacks==4)+(self.Mweapon.S<T)*(self.Mweapon.S>T/2)*np.count_nonzero(wounding_attacks>=5) +(self.Mweapon.S<=T/2)*6
        saving_rolls=np.random.randint(1,7,attacks_wound)
        unsaved_attacks=np.count_nonzero(saving_rolls<min((SV-self.Mweapon.AP),ISV))
        damage=unsaved_attacks*self.Mweapon.D
        results = {
            "attack_roll":attacks,
            "attacks_hitted":attacks_hited,
            "wound_rolls":wounding_attacks,
            "attacks_wounded":attacks_wound,
            "save_roll":saving_rolls,
            "unsaved_attacks":unsaved_attacks,
            "total_damage":damage


        }
        return results

warboss = Model("Warboss",2,5,6,6,6,6,4,5)
dreadnought = Model("Dreadnought",3,3,6,7,8,4,3,7)
n = 1000
sim=np.array([])
for i in range(n):
    sim=np.append(sim,warboss.makeMeleeAtack(dreadnought.T,dreadnought.SV,dreadnought.ISV))

class ShowBarChart(Scene):
    CONFIG ={
        "y_range":[0, 1, 0.1],
        "bar_names":np.array(range(max(sim, key=lambda x:x['attacks_hitted'])["attacks_hitted"]+1))
    }
    def construct(self):
        def update_composition(p_value):
            composition=np.array(range(max(sim, key=lambda x:x['attacks_hitted'])["attacks_hitted"]+1))
            for i in range(int(np.round(p_value))):
                composition[sim[i]['attacks_hitted']]=composition[sim[i]['attacks_hitted']]+1
            composition=composition/max(int(np.round(p_value)),1)
            return composition
        p = ValueTracker(1)

        composition=update_composition(1)
        chartHitting=BarChart(values=composition,**self.CONFIG).scale(0.8)
        chartHitting.add_updater(
            lambda m:
            m.become( 
                BarChart(values=update_composition(p.get_value()),**self.CONFIG).scale(0.8)
                )
            )
        
        text_top=Text("Composition of Lunar Soil").scale(0.9).next_to(
        chartHitting,UP,buff=0.1)
        text_left=Text("Relative Concentration").rotate(
        angle=TAU/4,axis=OUT).scale(0.6).next_to(chartHitting,LEFT,buff=0.5)
       
        self.play(Write(chartHitting),Write(text_top),Write(text_left),run_time=10)    
        
        self.play(ApplyMethod(p.increment_value,100),run_time=10)

        self.wait(2)