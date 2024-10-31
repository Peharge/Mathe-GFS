from manim import *
from manim import ThreeDScene, Surface, ThreeDAxes, DEGREES, TAU



class My3DScene(ThreeDScene):
    def construct(self):
        axes_3d = ThreeDAxes(
            x_range=(-6, 6, 1),
            x_length=12,
            y_range=(-5, 5, 1),
            y_length=10,
            z_range=(-3, 3, 1),
            z_length=6,
        )
        self.set_camera_orientation(phi=70 * DEGREES, theta=240 * DEGREES)

        surface = Surface(
            lambda u, v: np.array([
                np.cos(TAU * v),
                np.sin(TAU * v),
                2 * (1 - u)
            ]),
        ).fade(0.5)

        paraboloid = Surface(
            lambda u, v: np.array([
                np.cos(v) * u,
                np.sin(v) * u,
                u ** 2
            ]),
            v_range=(0, TAU),
        ).fade(0.5)

        para_hyp = Surface(
            lambda u, v: np.array([
                u,
                v,
                u ** 2 - v ** 2
            ]),
            u_range=(-2, 2),
            v_range=(-2, 2),
        ).fade(0.5)

        cone = Surface(
            lambda u, v: np.array([
                u * np.cos(v),
                u * np.sin(v),
                u
            ]),
            u_range=(-2, 2),
            v_range=(0, TAU),
        )
        sphere = Surface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u)
            ]),
            # Resolution of the surfaces
            u_range=(-PI / 2, PI / 2),
            v_range=(0, TAU),
        )

        self.add(axes_3d, surface)
        self.play(Transform(surface, paraboloid))
        self.wait(0.5)
        self.play(Transform(surface, para_hyp))
        self.wait(0.5)
        self.play(Transform(surface, cone))
        self.wait(0.5)
        self.play(Transform(surface, sphere))
        self.wait(0.5)
