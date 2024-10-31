from manim import *

class MatrixNotation(Scene):
    def construct(self):
        # Einführung
        self.introduction()
        self.wait(2)

        # Notation
        self.notation()
        self.wait(2)

        # Elemente der Matrix
        self.elements()
        self.wait(2)

        # Typen von Matrizen
        self.types()
        self.wait(2)

        # Formale Darstellung
        self.formal_representation()
        self.wait(2)

    def introduction(self):
        title = Text("Was sind Matrizen?", color=BLUE).shift(UP)  # Titel nach oben verschieben
        explanation = Text("Matrizen sind rechteckige \nAnordnungen von Zahlen.", color=WHITE).next_to(title, DOWN, buff=0.5)  # Erklärung unter dem Titel positionieren

        self.play(Create(title))
        self.play(Write(explanation))
        self.wait(2)  # Warte eine Sekunde, um die Erklärung anzuzeigen
        self.play(FadeOut(title), FadeOut(explanation))

    def notation(self):
        title = Text("Notation", color=GREEN).shift(3*UP)
        matrix_example = Matrix([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], color=YELLOW).next_to(title, DOWN, buff=0.5)
        matrix_example_label = Text("Matrix A", color=WHITE).next_to(matrix_example, UP).next_to(matrix_example, DOWN, buff=0.5)

        self.play(Create(title))
        self.play(LaggedStart(*[FadeIn(char, shift=LEFT) for char in matrix_example], lag_ratio=0.1))
        self.wait(2)

        self.play(FadeOut(title), FadeOut(matrix_example), FadeOut(matrix_example_label))

    def elements(self):
        title = Text("Elemente der Matrix", color=PURPLE).shift(UP)
        element_example = MathTex(
            "a_{ij} \\text{ bezeichnet das Element in der } i\\text{-ten Zeile und } j\\text{-ten Spalte}", color=WHITE
        ).next_to(title, DOWN, buff=0.5)

        self.play(Create(title))
        self.play(Write(element_example))
        self.wait(2)

        self.play(FadeOut(title), FadeOut(element_example))

    def types(self):
        title = Text("Typen von Matrizen", color=ORANGE).shift(UP)
        square_matrix_example = Matrix([[1, 2], [3, 4]], color=YELLOW).next_to(title, DOWN, buff=0.5)
        square_matrix_label = Text("Quadratische Matrix", color=WHITE).next_to(square_matrix_example, DOWN, buff=1)

        self.play(Create(title))
        self.play(Create(square_matrix_example), Write(square_matrix_label))
        self.wait(2)

        self.play(FadeOut(title), FadeOut(square_matrix_example), FadeOut(square_matrix_label))

    def formal_representation(self):
        title = Text("Formale Darstellung", color=TEAL).shift(UP)
        formal_example = MathTex(
            "A: \\{1,\\ldots,m\\} \\times \\{1,\\ldots,n\\} \\to K, (i,j) \\mapsto a_{ij}", color=WHITE
        ).next_to(title, DOWN, buff=0.5)

        self.play(Create(title))
        self.play(Write(formal_example))
        self.wait(2)

        self.play(FadeOut(title), FadeOut(formal_example))

# Führe das Skript aus, um das Video zu erstellen
# manim -pql matrix_notation.py MatrixNotation
