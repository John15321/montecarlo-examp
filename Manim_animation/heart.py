from turtle import dot

from manim import *
import math
n=1
box=18
rand_intX = np.array([1])#18*np.random.random_sample(n)-9
rand_intY = np.array([1])#18*np.random.random_sample(n)-9

rand_intX=rand_intX#*(box/1000000)
rand_intY=rand_intY#*(box/1000000)
print(rand_intX)
print(rand_intY)
t=np.arctan2(rand_intX,rand_intY)%(2*PI)
heartX=(16*(np.sin(t))**3)
heartY=(13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t))
print("t= ",t)

randXY_mod=np.sqrt(np.power(rand_intX,2)+np.power(rand_intY,2))
heartXY_mod=np.sqrt(np.power(heartX,2)+np.power(heartY,2))
dotcolor =(randXY_mod<heartXY_mod)

class heart(MovingCameraScene):


    def construct(self):        
        self.add(NumberPlane())
        curve = ParametricFunction(lambda t: np.array([
            (16*(np.sin(t))**3),
            (13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)), 0
            ]),color=PINK,t_range = np.array([0, t[0]]))
        
        square=Square(box)
        
        ax = Axes(
            x_range=[-12, 12, 1],
            y_range=[-12, 12, 1],
            tips=False,
            axis_config={"include_numbers": True},
        )
        #self.add(ax)
        dots=VGroup()
        for i in range(n):
            dots+=(Dot(point=[rand_intX[i],rand_intY[i],0],color=('Green' if dotcolor[i] else 'Red')))
        for i in range(n):
            dots+=(Dot(point=[heartX[i],heartY[i],0],color="White"))
        
        self.add(square)
        #self.play(self.camera.auto_zoom(square),run_time=1)
        myTitle = MarkupText("<u>Pole serca</u>").to_corner(UP+LEFT)
        inHeart_counter=MarkupText("Test=2").to_corner(UP+RIGHT)
        outHeart_counter=MarkupText("Test=2").next_to(inHeart_counter,DOWN)
        self.add(outHeart_counter)
        self.add(inHeart_counter)
        self.add((myTitle))#,run_time=1)
        self.add((curve))#,run_time=3)
        self.add((dots))#,run_time=3)
        #self.wait(3)




