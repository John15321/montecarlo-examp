from manim import *
class OpeningManim(Scene):
    def construct(self):
        title = Tex(r"Metoda Monte Carlo",font_size=144)
        subtitle = Tex(r"Denis Firat\\Jan Bronicki\\Paweł Szczepaniak",font_size=40)
        VGroup(title, subtitle).arrange(DOWN)
        self.play(
            Write(title),
            FadeIn(subtitle, shift=DOWN),
        )
        self.wait(3)
        circle=Circle()
        transform_title = Tex("Prezentacja metody Monte Carlo")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*(FadeOut(obj, shift=DOWN) for obj in subtitle)),
        )
        self.wait()

        grid = NumberPlane()

        self.play(
            Create(grid, run_time=3, lag_ratio=0.1),
        )
        self.wait()

        grid_transform_title = Tex(
            r"That was a non-linear function \\ applied to the grid",
        )

        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.animate.apply_function(
                lambda p: p
                + np.array(
                    [
                        np.sin(p[1]),
                        np.sin(p[0]),
                        0,
                    ],
                ),
            ),
            run_time=3,
        )
        self.wait()
        self.wait()

from manim import *

class SinAndCosFunctionPlot(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-10, 10.3, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=10,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(-10, 10.01, 2),
                "numbers_with_elongated_ticks": np.arange(-10, 10.01, 2),
            },
            tips=False,
        )
        axes_labels = axes.get_axis_labels()
        sin_graph = axes.plot(lambda x: (np.sin(x)*np.sqrt(np.abs(np.cos(x))))/(np.sin(x)+7/5)-2*np.sin(x) +2, color=BLUE)
        cos_graph = axes.plot(lambda x: np.cos(x), color=RED)

        sin_label = axes.get_graph_label(
            sin_graph, "\\sin(x)", x_val=-10, direction=UP / 2
        )
        cos_label = axes.get_graph_label(cos_graph, label="\\cos(x)")

        vert_line = axes.get_vertical_line(
            axes.i2gp(TAU, cos_graph), color=YELLOW, line_func=Line
        )
        line_label = axes.get_graph_label(
            cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
        )

        plot = VGroup(axes, sin_graph, cos_graph, vert_line)
        labels = VGroup(axes_labels, sin_label, cos_label, line_label)
        self.add(plot, labels)

        #sin_graph = axes.plot(lambda x: np.sin(x), color=BLUE)
        #sin_grap  =	axes.plot(lambda x: (h-l)H(x+1)+(r-h)H(x-1)+(l-w)H(x+3)+(w-r)H(x-3)+w, color=BLUE)

from manim import *

class PlotParametricFunction(Scene):
    def func(self, t):
        return np.array(((16*(np.sin(t))**3)/2,(13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t))/2+2, 0))

    def construct(self):
        func = ParametricFunction(self.func, t_range = np.array([0, 7]), fill_opacity=0).set_color(RED)
        self.add(func.scale(0.1))
	