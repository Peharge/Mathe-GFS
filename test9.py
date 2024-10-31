from manim import *
import numpy as np

def gauss(matrix):
    """Eine einfache Implementierung des Gauß-Eliminationsverfahrens."""
    # Das Gauß-Verfahren wird hier implementiert
    rows, cols = matrix.shape
    steps = []

    for i in range(min(rows, cols)):
        # Pivotisierung
        max_row_index = np.argmax(np.abs(matrix[i:, i])) + i
        if matrix[max_row_index, i] == 0:
            continue  # Wenn der Pivot 0 ist, überspringen

        # Zeilen tauschen
        matrix[[i, max_row_index]] = matrix[[max_row_index, i]]
        steps.append(matrix.copy())

        # Elimination
        for j in range(i + 1, rows):
            factor = matrix[j, i] / matrix[i, i]
            matrix[j] -= factor * matrix[i]
            steps.append(matrix.copy())

    return steps

class Gauss3D(ThreeDScene):

    def create_matrix(self, np_matrix):
        m = Matrix(np_matrix)
        m.scale(0.5)
        m.set_column_colors(GREEN, RED, GOLD)  # Die Farben direkt übergeben
        m.to_corner(UP + LEFT)
        return m

    def construct(self):

        M = np.array([
            [-1.0, 1.0, -2.0],
            [-4.0, -2.0, 1.0],
            [-2.0, 2.0, 3.0]
        ])

        # Achsen erstellen
        axes = ThreeDAxes()
        axes.set_color(GRAY)
        axes.add(axes.get_axis_labels(x_label="x", y_label="y", z_label="z"))

        self.set_camera_orientation(phi=55 * DEGREES, theta=-45 * DEGREES)

        # Basisvektoren i,j,k
        basis_vector_helper = MathTex("i", ",", "j", ",", "k")
        basis_vector_helper[0].set_color(GREEN)
        basis_vector_helper[2].set_color(RED)
        basis_vector_helper[4].set_color(GOLD)

        basis_vector_helper.to_corner(UP + RIGHT)
        self.add_fixed_in_frame_mobjects(basis_vector_helper)

        # Matrix erstellen
        matrix = self.create_matrix(M)
        self.add_fixed_in_frame_mobjects(matrix)

        # Achsen & Kamera
        self.add(axes)
        self.begin_ambient_camera_rotation(rate=0.15)

        # Würfel erstellen
        cube = Cube(side_length=1, fill_color=BLUE, stroke_width=2, fill_opacity=0.1)
        cube.set_stroke(BLUE_E)

        # Vektoren erstellen
        i_vec = Vector([1, 0, 0], color=GREEN)
        j_vec = Vector([0, 1, 0], color=RED)
        k_vec = Vector([0, 0, 1], color=GOLD)

        i_vec_new = Vector(M @ np.array([1, 0, 0]), color=GREEN)
        j_vec_new = Vector(M @ np.array([0, 1, 0]), color=RED)
        k_vec_new = Vector(M @ np.array([0, 0, 1]), color=GOLD)

        self.play(
            Create(cube),
            GrowArrow(i_vec),
            GrowArrow(j_vec),
            GrowArrow(k_vec),
            Write(basis_vector_helper)
        )

        self.wait()

        matrix_anim = ApplyMatrix(M, cube)

        self.play(
            matrix_anim,
            ReplacementTransform(i_vec, i_vec_new),
            ReplacementTransform(j_vec, j_vec_new),
            ReplacementTransform(k_vec, k_vec_new)
        )

        self.wait()

        i_vec, j_vec, k_vec = i_vec_new, j_vec_new, k_vec_new
        self.wait(2)

        for a in gauss(M):
            a_rounded = np.round(a.copy(), 2)

            self.remove(matrix)
            matrix = self.create_matrix(a_rounded)
            self.add_fixed_in_frame_mobjects(matrix)

            # Transformierten Würfel erstellen
            new_cube = Cube(side_length=1, fill_color=BLUE, stroke_width=2, fill_opacity=0.1)
            new_cube.set_stroke(BLUE_E)
            new_cube.apply_matrix(a)

            # Neue Vektoren erstellen
            i_vec_new = Vector(a @ np.array([1, 0, 0]), color=GREEN)
            j_vec_new = Vector(a @ np.array([0, 1, 0]), color=RED)
            k_vec_new = Vector(a @ np.array([0, 0, 1]), color=GOLD)

            # Vorbereitung und Ausführung der Animation
            cube_anim = ReplacementTransform(cube, new_cube)

            self.play(
                cube_anim,
                ReplacementTransform(i_vec, i_vec_new),
                ReplacementTransform(j_vec, j_vec_new),
                ReplacementTransform(k_vec, k_vec_new)
            )

            self.wait()
            cube = new_cube
            i_vec, j_vec, k_vec = i_vec_new, j_vec_new, k_vec_new
            self.wait(1)

        self.wait(1)
