from manim import *

class OpeningManim(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        titel = Text(r"MATHE GFS", color=BLACK).scale(2)
        thema = Text(r"MATRIZEN - HOPFIELD NETWORK", color=BLACK).scale(0.6)
        name = Text(r"JULIAN KROPFF", color=BLACK).scale(1)
        zusatz = Text(r"TGM-J2 – TG Lörrach – 15.01.2025", color=BLACK).scale(0.5)
        VGroup(titel, thema, name, zusatz).arrange(DOWN)
        self.play(
            Write(titel),
        )
        self.play(Indicate(titel))
        self.play(
            Write(thema, shift=DOWN),
        )
        # self.play(Indicate(thema))
        self.play(
            Write(name, shift=DOWN),
        )
        # self.play(Indicate(name))
        self.play(
            Write(zusatz, shift=DOWN),
        )
        # self.play(Indicate(zusatz))
        self.wait()