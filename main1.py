from manim import *


class ContinuousMotion(Scene):
    def construct(self):
        # Definieren der Strömungslinien (StreamLines)
        func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
        stream_lines = StreamLines(func, stroke_width=2, max_anchors_per_line=30)
        self.add(stream_lines)
        stream_lines.start_animation(warm_up=False, flow_speed=1.5)

        # Erstellen und Anzeigen des Textes "Mathe-GFS: Matrizen" in der Mitte
        title = Text("Mathe-GFS: Matrizen", font_size=48, color=YELLOW)

        # Hinzufügen einer Schreibe-Animation für den Text
        self.play(Write(title))

        # Kurze Wartezeit, damit der Text nach dem Schreiben sichtbar bleibt
        self.wait(2)

        # Entfernen des Textes (optional)
        self.play(FadeOut(title))

        # Feste Wartezeit für die Animationslänge der Strömungslinien
        self.wait(5)  # Anpassen je nach gewünschter Dauer der Animation
