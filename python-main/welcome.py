from manim import *


class BasicUsage(Scene):
    def construct(self):
        func = lambda pos: ((pos[0] * UR + pos[1] * LEFT) - pos) / 3

        # Erstelle die Streamlines
        streamlines = StreamLines(func)

        # Füge den Text hinzu
        text = Text("Streamlines Visualization", font_size=36)

        # Positioniere den Text
        text.move_to(UP * 3)  # Bewege den Text nach oben

        # Füge die Streamlines und den Text zur Szene hinzu
        self.add(streamlines)
        self.add(text)

        # Optional: Animationen hinzufügen, z.B. erscheinen lassen
        self.play(ShowCreation(streamlines), Write(text))
        self.wait(2)
