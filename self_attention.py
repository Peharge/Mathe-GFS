from manim import *


class SelfAttentionTableScene(Scene):
    def construct(self):
        # Erstelle eine Tabelle mit Wörtern
        table = Table(
            [["Wort", "Vektor"]],
            include_outer_lines=True
        )

        # Füge einige Wörter und ihre hypothetischen Vektoren hinzu
        words = [
            ["Katze", "0.2, 0.4, 0.3"],
            ["Hund", "0.1, 0.5, 0.6"],
            ["Maus", "0.3, 0.2, 0.5"]
        ]

        for word, vector in words:
            table.add_row([word, vector])  # Hier die Methode zu add_row geändert

        # Positioniere die Tabelle
        table.scale(0.8)
        self.play(Create(table))
        self.wait(2)

        # Schreibe die Erklärungen zu Q und K
        explanation = Tex("Q und K messen die Ähnlichkeit zwischen Wörtern.").next_to(table, DOWN)
        self.play(Write(explanation))
        self.wait(2)

        # Animation für die Ähnlichkeit zwischen Wörtern
        similarity_text = Tex("Ähnlichkeit (Katze, Hund)").next_to(explanation, DOWN)
        self.play(Write(similarity_text))
        self.wait(2)

        # Zeige eine Animation für das Schreiben von Wörtern
        for word, vector in words:
            word_label = Tex(word).next_to(similarity_text, DOWN).shift(LEFT * 2)
            vector_label = Tex(vector).next_to(word_label, RIGHT)
            self.play(Write(word_label), Write(vector_label))
            self.wait(1)

        # Fade out alles
        self.play(FadeOut(table), FadeOut(explanation), FadeOut(similarity_text))
        self.wait(1)

# Um das Skript auszuführen, speichere es in einer Datei, z.B. "self_attention_table.py" und führe den folgenden Befehl in deinem Terminal aus:
# manim -pql self_attention_table.py SelfAttentionTableScene
