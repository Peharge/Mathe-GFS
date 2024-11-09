from manim import *
import numpy as np


class function(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(zoom=0.6)

        axes = ThreeDAxes()
        cos_graph = axes.plot(lambda x: np.cos(x), color=RED)
        curve = ParametricFunction(lambda x: np.array([np.sin(x), np.cos(x), x / 2]), color=BLUE, t_range=(-TAU, TAU))

        t = Text("Example").to_edge(UL)
        self.add_fixed_in_frame_mobjects(t)

        self.play(Write(axes), Write(t))
        self.play(Write(cos_graph))
        self.move_camera(phi=60 * DEGREES, theta=-45 * DEGREES)
        self.play(Write(curve))
        self.move_camera(phi=30 * DEGREES, theta=-45 * DEGREES)
        self.wait(2)

        g = VGroup(curve, cos_graph, t, axes)
        self.play(Unwrite(g), run_time=1.5)
        self.wait()