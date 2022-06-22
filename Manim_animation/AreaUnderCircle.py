from shutil import move
from typing_extensions import runtime
from manim import *
from scipy.fftpack import shift

n=1000
rand_intX = np.random.randint(100,500,(n))
rand_intY = np.random.randint(200,600,(n))

rand_intX=rand_intX/100
rand_intY=rand_intY/100
t=np.arctan2(rand_intX-3,rand_intY-4)

heartX=2*np.cos(t)
heartY=2*np.sin(t)

randXY_mod=np.sqrt(np.power(rand_intX-3,2)+np.power(rand_intY-4,2))
heartXY_mod=np.sqrt(np.power(heartX,2)+np.power(heartY,2))
dotcolor =(randXY_mod<heartXY_mod)


class AreaUnderLine(MovingCameraScene):
    def construct(self):
        ax = Axes(
            x_range=[0, 7],
            y_range=[0, 7],
            x_length=6,
            y_length=6,
            x_axis_config={"numbers_to_include": range(8)},
            y_axis_config={"numbers_to_include": range(8)},
            tips=False,
        )

        labels = ax.get_axis_labels()
        p = ValueTracker(1)

        line_1 = ax.plot(lambda x: p.get_value()*(x-1)+2, x_range=[1, 5], color=BLUE_C)
        line_1.add_updater(
            lambda m: m.become(
                ax.plot(lambda x: p.get_value()*(x-1)+2, x_range=[1, 5], color=BLUE_C
                )
            )
        )

        dotsCounter=ValueTracker(0)
        dotsInText=Tex("Punkty w $P_1$: ").next_to(ax,RIGHT).shift(DOWN*3)
        dotsOutText=Tex("Punkty w $P_2$: ").next_to(ax,RIGHT).shift(DOWN*4)
        
        dotsInTextNumber = always_redraw(
            lambda: DecimalNumber(num_decimal_places=0)
            .set_value(np.sum(dotcolor[:int(dotsCounter.get_value())]))
            .next_to(dotsInText, RIGHT, buff=0.1)
            .set_color(YELLOW)
        ).add_background_rectangle()
        dotsOutTextNumber = always_redraw(
            lambda: DecimalNumber(num_decimal_places=0)
            .set_value(np.sum(dotcolor[:int(dotsCounter.get_value())]==0))
            .next_to(dotsOutText, RIGHT, buff=0.1)
            .set_color(YELLOW)
        ).add_background_rectangle()

        def get_dot_group():
            dots=VGroup()
            for i in range(int(dotsCounter.get_value())):
                dots+=(Dot(ax.coords_to_point(rand_intX[i], rand_intY[i]),radius=0.05,color=('Green' if dotcolor[i] else 'Red')))
            return dots

        
        dots=always_redraw(get_dot_group)
        
        line_2 = ax.plot(lambda x: 2, x_range=[1, 5], color=BLUE_C)
        #for i in range(dotsCounter.get_value()):
        #    dots+=(Dot(ax.coords_to_point(rand_intX[i], rand_intY[i]),radius=0.01,color=('Green' if dotcolor[i] else 'Red')))
        #dots2=always_redraw(lambda: VGroup(Dot(ax.coords_to_point(rand_intX[:int(dotsCounter.get_value())], rand_intY[:int(dotsCounter.get_value())]),radius=0.01,color=('Green' if dotcolor[:int(dotsCounter.get_value())] else 'Red'))))
        squareDots=VGroup(Dot(ax.coords_to_point(1, 2), color=BLUE),Dot(ax.coords_to_point(5,2), color=BLUE),Dot(ax.coords_to_point(5, 6), color=BLUE),Dot(ax.coords_to_point(1, 6), color=BLUE),Dot(ax.coords_to_point(5, 6), color=BLUE))
        square=VGroup(Line(squareDots[0],squareDots[1],color=BLUE),Line(squareDots[1],squareDots[2],color=BLUE),Line(squareDots[2],squareDots[3],color=BLUE),Line(squareDots[3],squareDots[0],color=BLUE))
        
        braceA = Brace(square[0], sharpness=1)
        braceB = Brace(square[1],sharpness=1)
        braceB = Brace(square[1], direction=square[1].copy().rotate(-PI / 2).get_unit_vector())
        
        braceAtext = braceA.get_tex("a")
        braceBtext = braceB.get_tex("b")
        
        area = ax.get_area(line_1, [1, 5], bounded_graph=line_2, color=GREY, opacity=0.5)
        
        p1Label=Tex("$P_1$")
        p2Label=Tex("$P_2$").shift(1.8*LEFT,UP*1.8)
        PLabels=VGroup(p1Label,p2Label)

        areaEquation1=Tex("$P_2=k\cdot P_1$")
        areaEquation1_1=Tex("$P_c=a\cdot b=16$")
        areaEquation2=Tex(r"$k=\frac{P_2}{P_1}$")
        areaEquation2_1=Tex(r"$k=\frac{P_2}{P_1}=$")
        areaEquation2_1Value = always_redraw(
            lambda: DecimalNumber(num_decimal_places=2)
            .set_value(max(0,np.sum(dotcolor[:int(dotsCounter.get_value())]==0)/np.sum(dotcolor[:int(dotsCounter.get_value())])))
            .next_to(areaEquation2_1, RIGHT, buff=0.1)
            .set_color(YELLOW)
        ).add_background_rectangle()

        areaEquation3=Tex("$P_c=P_1+P_2$")
        areaEquation3_1=Tex("$P_c=P_1+k\cdot P_1$")
        areaEquation3_2=Tex("$P_c=P_1(1+k)$")
        areaEquation4=Tex(r'$P_1=\frac{P_c}{k+1}=$')
        areaEquation4Value = always_redraw(
            lambda: DecimalNumber(num_decimal_places=2)
            .set_value(16/(1+max(0,np.sum(dotcolor[:int(dotsCounter.get_value())]==0)/np.sum(dotcolor[:int(dotsCounter.get_value())]))))
            .next_to(areaEquation4, RIGHT, buff=0.1)
            .set_color(YELLOW)
        ).add_background_rectangle()

        
        self.add(ax,labels)
        title = Title(f"Monte Carlo - obliczanie pola figury")
        self.play(FadeIn(title))
        self.play(Create(squareDots),runtime=5)
        self.play(Create(square),runtime=5)
        circle=Circle.from_three_points(ax.coords_to_point(3, 6), ax.coords_to_point(5, 4) , ax.coords_to_point(3, 2), color=RED)
        self.play(Create(circle),run_time=1)
        #self.play(Create(line_1),runtime=5)
        #self.add(area)
        self.play(Create(braceA),Create(braceAtext),runtime=1)
        self.play(Create(braceB),Create(braceBtext),runtime=1)
        self.play(FadeIn(PLabels),runTime=1)
        image=VGroup(ax,labels,squareDots,square,braceA,braceB,braceAtext,braceBtext,PLabels,circle)
        self.play(ApplyMethod(p.increment_value,-0.3),run_time=5)
        self.play(image.animate().to_edge(LEFT))
        areaEquations=VGroup(areaEquation1,areaEquation2,areaEquation3,areaEquation3_1,areaEquation3_2).arrange(DOWN, center=False, aligned_edge=LEFT).next_to(ax,RIGHT).shift(2*RIGHT)
        
        
        self.play(Transform(PLabels,areaEquation1),runtime=2)
        self.play(FadeIn(areaEquation2),runtime=1)
        self.play(FadeIn(areaEquation3),runtime=1)
        self.play(FadeIn(areaEquation3_1),runtime=1)
        self.play(FadeIn(areaEquation3_2),runtime=1)
        
        areaEquations2=VGroup(areaEquation1_1,areaEquation2_1,areaEquation4).arrange(DOWN, center=False, aligned_edge=LEFT).next_to(ax,RIGHT).shift(2*RIGHT)
        self.play(Transform(VGroup(PLabels,areaEquations),areaEquations2),FadeIn(dotsInText),FadeIn(dotsOutText),FadeIn(dotsInTextNumber),FadeIn(dotsOutTextNumber),FadeIn(areaEquation2_1Value.next_to(areaEquation2_1,RIGHT,buff=0.1)),FadeIn(areaEquation4Value.next_to(areaEquation4,RIGHT,buff=0.1)),runtime=1)
        self.wait(2)
        self.play(Create(dots),runtime=4)
        self.wait(1)
        self.play(dotsCounter.animate.set_value(n),run_time=4)

        self.wait(3)
        #, curve_1, line_1, line_2, riemann_area