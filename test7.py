from manim import *

class LinearTransformation3D(ThreeDScene):

    def create_matrix(self, np_matrix):

        m = Matrix(np_matrix)

        m.scale(0.5)
        m.set_column_colors(GREEN, RED, GOLD)  # Die Farben manuell übergeben

        m.to_corner(UP + LEFT)

        return m

    def construct(self):

        M = np.array([
            [2, 2, -1],
            [-2, 1, 2],
            [3, 1, 0]  # '-0' zu '0' korrigiert
        ])

        # Koordinatenachsen erstellen
        axes = ThreeDAxes()
        axes.set_color(GRAY)
        axes.add(axes.get_axis_labels(x_label="x", y_label="y", z_label="z"))

        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

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

        self.begin_ambient_camera_rotation(rate=0.2)

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
            Transform(i_vec, i_vec_new),
            Transform(j_vec, j_vec_new),
            Transform(k_vec, k_vec_new)
        )

        self.wait()

        self.wait(7)

