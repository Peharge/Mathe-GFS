from manim import *

class TensorRepresentation(Scene):
    def construct(self):
        # Farben definieren
        scalar_color = BLUE
        vector_color = GREEN
        matrix_color = ORANGE
        tensor_color = PURPLE

        # Scalar
        scalar = MathTex(r"s = 5", color=scalar_color).scale(0.5).shift(LEFT * 5.5 + UP * 1.5)
        scalar_label = Text("Scalar (rank 0)", font_size=15, color=scalar_color).next_to(scalar, DOWN)
        self.play(Write(scalar), FadeIn(scalar_label))
        self.wait(1)

        # Vector
        vector = MobjectTable(
            [[MathTex("v_1", color=vector_color)], [MathTex("v_2", color=vector_color)],
             [MathTex(r"\vdots", color=vector_color)], [MathTex("v_n", color=vector_color)]],
            include_outer_lines=True
        ).scale(0.4).shift(LEFT * 2.5 + UP * 1.5)
        vector_label = Text("Vector (rank 1)", font_size=15, color=vector_color).next_to(vector, DOWN)
        self.play(Create(vector), Write(vector_label))
        self.wait(1)

        # Matrix
        matrix = MobjectTable(
            [
                [MathTex("m_{11}", color=matrix_color), MathTex("m_{12}", color=matrix_color), MathTex(r"\cdots", color=matrix_color), MathTex("m_{1n}", color=matrix_color)],
                [MathTex("m_{21}", color=matrix_color), MathTex("m_{22}", color=matrix_color), MathTex(r"\cdots", color=matrix_color), MathTex("m_{2n}", color=matrix_color)],
                [MathTex(r"\vdots", color=matrix_color), MathTex(r"\vdots", color=matrix_color), MathTex(r"\ddots", color=matrix_color), MathTex(r"\vdots", color=matrix_color)],
                [MathTex("m_{n1}", color=matrix_color), MathTex("m_{n2}", color=matrix_color), MathTex(r"\cdots", color=matrix_color), MathTex("m_{nn}", color=matrix_color)]
            ],
            include_outer_lines=True
        ).scale(0.4).shift(RIGHT * 1 + UP * 1.5)
        matrix_label = Text("Matrix (rank 2)", font_size=15, color=matrix_color).next_to(matrix, DOWN)
        self.play(Create(matrix), Write(matrix_label))
        self.wait(1)

        # Rank-3 Tensor
        tensor_planes = VGroup(
            MobjectTable(
                [
                    [MathTex("T_{111}", color=tensor_color), MathTex("T_{112}", color=tensor_color), MathTex(r"\cdots", color=tensor_color), MathTex("T_{11N}", color=tensor_color)],
                    [MathTex("T_{121}", color=tensor_color), MathTex("T_{122}", color=tensor_color), MathTex(r"\cdots", color=tensor_color), MathTex("T_{12N}", color=tensor_color)],
                    [MathTex(r"\vdots", color=tensor_color), MathTex(r"\vdots", color=tensor_color), MathTex(r"\ddots", color=tensor_color), MathTex(r"\vdots", color=tensor_color)],
                    [MathTex("T_{N11}", color=tensor_color), MathTex("T_{N12}", color=tensor_color), MathTex(r"\cdots", color=tensor_color), MathTex("T_{N1N}", color=tensor_color)]
                ],
                include_outer_lines=True
            ).scale(0.3).shift(RIGHT * 4),
            MobjectTable(
                [
                    [MathTex("T_{211}", color=tensor_color), MathTex("T_{212}", color=tensor_color), MathTex(r"\cdots", color=tensor_color), MathTex("T_{21N}", color=tensor_color)],
                    [MathTex("T_{221}", color=tensor_color), MathTex("T_{222}", color=tensor_color), MathTex(r"\cdots", color=tensor_color), MathTex("T_{22N}", color=tensor_color)],
                    [MathTex(r"\vdots", color=tensor_color), MathTex(r"\vdots", color=tensor_color), MathTex(r"\ddots", color=tensor_color), MathTex(r"\vdots", color=tensor_color)],
                    [MathTex("T_{N21}", color=tensor_color), MathTex("T_{N22}", color=tensor_color), MathTex(r"\cdots", color=tensor_color), MathTex("T_{N2N}", color=tensor_color)]
                ],
                include_outer_lines=True
            ).scale(0.3).shift(RIGHT * 5),
            MobjectTable(
                [
                    [MathTex("T_{311}", color=tensor_color), MathTex("T_{312}", color=tensor_color), MathTex(r"\cdots", color=tensor_color), MathTex("T_{31N}", color=tensor_color)],
                    [MathTex("T_{321}", color=tensor_color), MathTex("T_{322}", color=tensor_color), MathTex(r"\cdots", color=tensor_color), MathTex("T_{32N}", color=tensor_color)],
                    [MathTex(r"\vdots", color=tensor_color), MathTex(r"\vdots", color=tensor_color), MathTex(r"\ddots", color=tensor_color), MathTex(r"\vdots", color=tensor_color)],
                    [MathTex("T_{N31}", color=tensor_color), MathTex("T_{N32}", color=tensor_color), MathTex(r"\cdots", color=tensor_color), MathTex("T_{N3N}", color=tensor_color)]
                ],
                include_outer_lines=True
            ).scale(0.3).shift(RIGHT * 6)
        )

        # Position des Tensors unter den anderen Objekten verschieben
        tensor_planes.shift(DOWN * 3)  # Verschiebt den Tensor weiter nach unten

        tensor_label = Text("Rank-3 Tensor (rank 3)", font_size=15, color=tensor_color).next_to(tensor_planes, DOWN)
        self.play(Create(tensor_planes), Write(tensor_label))
        self.wait(2)

        # Abschluss
        self.play(
            FadeOut(scalar, scalar_label),
            FadeOut(vector, vector_label),
            FadeOut(matrix, matrix_label),
            FadeOut(tensor_planes, tensor_label)
        )
        final_text = Text("Scalar, Vector, Matrix, and Tensor", font_size=24, color=WHITE)
        self.play(Write(final_text))
        self.wait(3)
