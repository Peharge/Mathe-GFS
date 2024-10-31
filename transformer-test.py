from manim import *

class TransformerSelfAttention(Scene):
    def construct(self):
        # Schritt 1: Satz einblenden und in Tokens zerlegen
        sentence = Text("The cat sat on the mat.", font_size=40)
        self.play(Write(sentence))
        self.wait(1)

        # Zerlege den Satz in Tokens
        tokens = ["The", "cat", "sat", "on", "the", "mat"]
        token_group = VGroup(*[Text(tok, font_size=36) for tok in tokens])
        token_group.arrange(RIGHT, buff=0.5)

        self.play(Transform(sentence, token_group))
        self.wait(1)

        # Schritt 2: Embedding und Positional Encoding darstellen
        embedding_label = Text("Embedding", font_size=30).to_edge(UP)
        self.play(Write(embedding_label))

        # Zeige die Embeddings der Token
        embeddings = VGroup(
            *[Matrix([[0.1*i, 0.2*i, 0.3*i]], h_buff=1.5) for i in range(1, 7)]
        )
        embeddings.arrange(RIGHT, buff=1).next_to(token_group, DOWN)

        self.play(FadeIn(embeddings))
        self.wait(2)

        # Schritt 3: Positional Encoding hinzufügen
        positional_label = Text("Positional Encoding", font_size=30).to_edge(DOWN)
        self.play(Write(positional_label))

        pos_encodings = VGroup(
            *[Matrix([[0.01*i, 0.02*i, 0.03*i]], h_buff=1.5) for i in range(1, 7)]
        )
        pos_encodings.arrange(RIGHT, buff=1).next_to(embeddings, DOWN)

        self.play(FadeIn(pos_encodings))
        self.wait(2)

        # Schritt 4: Q, K, V Matrizen darstellen
        qkv_label = Text("Q, K, V Matrices", font_size=30).to_edge(UP)
        self.play(Transform(embedding_label, qkv_label))

        # Erstelle Q, K, V Matrizen für jedes Token
        q_matrices = VGroup(
            *[Matrix([[0.1*i, 0.2*i], [0.3*i, 0.4*i]], h_buff=1.5) for i in range(1, 7)]
        )
        k_matrices = VGroup(
            *[Matrix([[0.15*i, 0.25*i], [0.35*i, 0.45*i]], h_buff=1.5) for i in range(1, 7)]
        )
        v_matrices = VGroup(
            *[Matrix([[0.2*i, 0.3*i], [0.4*i, 0.5*i]], h_buff=1.5) for i in range(1, 7)]
        )

        q_matrices.arrange(RIGHT, buff=1).next_to(token_group, DOWN)
        k_matrices.arrange(RIGHT, buff=1).next_to(q_matrices, DOWN)
        v_matrices.arrange(RIGHT, buff=1).next_to(k_matrices, DOWN)

        self.play(FadeIn(q_matrices), FadeIn(k_matrices), FadeIn(v_matrices))
        self.wait(2)

        # Schritt 5: Berechnung der Self-Attention
        attention_label = Text("Self-Attention", font_size=30).to_edge(UP)
        self.play(Transform(embedding_label, attention_label))

        # Erstelle eine Tabelle zur Visualisierung des Dot-Product und der Gewichtung
        dot_product_table = Matrix([
            [0.8, 0.3, 0.5, 0.2, 0.4, 0.7],  # Token 1 mit allen anderen
            [0.3, 0.9, 0.6, 0.4, 0.2, 0.5],  # Token 2 mit allen anderen
            [0.5, 0.6, 0.7, 0.3, 0.2, 0.8],  # ...
            [0.2, 0.4, 0.3, 0.9, 0.5, 0.7],
            [0.4, 0.2, 0.2, 0.5, 0.8, 0.6],
            [0.7, 0.5, 0.8, 0.7, 0.6, 0.9]
        ], h_buff=1.2).next_to(token_group, DOWN)

        self.play(Write(dot_product_table))
        self.wait(2)

        # Schritt 6: Gewichtung auf die Value-Matrix anwenden
        value_label = Text("Apply Weighting", font_size=30).to_edge(UP)
        self.play(Transform(embedding_label, value_label))

        weighted_values = VGroup(
            *[Matrix([[0.2*i, 0.3*i], [0.4*i, 0.5*i]], h_buff=1.5) for i in range(1, 7)]
        ).next_to(dot_product_table, DOWN)

        self.play(FadeIn(weighted_values))
        self.wait(2)

        # Finale Szene
        final_sentence = Text("Transformed Representation!", font_size=40).to_edge(DOWN)
        self.play(FadeOut(token_group, embeddings, pos_encodings, dot_product_table, q_matrices, k_matrices, v_matrices),
                  Write(final_sentence))
        self.wait(2)

