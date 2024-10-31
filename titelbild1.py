from manim import *


class EnhancedStreamlines(Scene):
    def construct(self):
        # Funktion für die Streamlines
        func = lambda pos: ((pos[0] * UR + pos[1] * LEFT) - pos) / 3

        # Erstelle die Streamlines mit einer Farbe
        streamlines = StreamLines(func, stroke_color=BLUE, stroke_width=2)

        # Füge den erklärenden Text hinzu
        title = Text("Matrizen", font_size=72)
        description = Text("Mathe GFS Julian Kropff TGM-J2", font_size=36)

        # Positioniere den Text in die Mitte
        title.move_to(ORIGIN + UP)
        description.next_to(title, DOWN)

        # Füge die Streamlines und den Text zur Szene hinzu
        self.add(streamlines)
        self.add(title)
        self.add(description)

        # Animationen hinzufügen, um die Streamlines und den Text erscheinen zu lassen
        self.play(Create(streamlines), Write(title), Write(description))
        self.wait(2)

        # Optional: Lasse die Streamlines verschwinden
        self.play(FadeOut(streamlines), FadeOut(title), FadeOut(description))
