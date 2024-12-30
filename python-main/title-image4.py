from manim import *

class OpeningManim(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        titel = Text(r"Wie bilden Matrizen und ihre grundlegenden Eigenschaften die Basis für", color=BLACK).scale(0.6)
        thema = Text(r"moderne Modelle in der Informatik, insbesondere im Kontext von", color=BLACK).scale(0.6)
        name = Text(r"Hopfield-Netzwerken und welche Rolle spielen Matrizenoperationen bei", color=BLACK).scale(0.6)
        zusatz = Text(r"der Modellierung und Lösung komplexer Probleme?", color=BLACK).scale(0.6)
        VGroup(titel, thema, name, zusatz).arrange(DOWN)
        self.play(
            Write(titel),
        )
        self.play(
            Write(thema, shift=DOWN),
        )
        self.play(
            Write(name, shift=DOWN),
        )
        self.play(
            Write(zusatz, shift=DOWN),
        )
        self.wait()