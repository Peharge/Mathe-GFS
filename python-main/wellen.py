from manim import *

class MeerAnimation(ThreeDScene):
    def construct(self):
        # Setze die Achsen
        axes = ThreeDAxes()

        # Erzeuge die Meeresoberfläche
        ocean_surface = self.create_ocean_surface(0)

        # Füge die Achsen und die Meeresoberfläche zur Szene hinzu
        self.add(axes, ocean_surface)

        # Kamera Animation
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES, run_time=3)

        # Animation der Wellen
        self.animate_waves(ocean_surface)

    def create_ocean_surface(self, t):
        # Erstelle die Meeresoberfläche mit einer parametrischen Funktion
        ocean_surface = Surface(
            lambda u, v: np.array([
                u,
                0.5 * np.sin(2 * np.pi * (u + t)) + 0.2 * np.sin(3 * np.pi * (v + t)),  # Kombiniere Sinuswellen für glattere Bewegung
                v
            ]),
            u_range=[-5, 5],
            v_range=[-5, 5],
            resolution=(30, 30),
            color=BLUE,
            fill_opacity=0.8
        )

        return ocean_surface

    def animate_waves(self, ocean_surface):
        # Animiert die Wellen über die Zeit
        for t in np.linspace(0, 2 * PI, 60):  # 60 Frames für 60 FPS
            self.remove(ocean_surface)  # Entferne die vorherige Oberfläche
            ocean_surface = self.create_ocean_surface(t)  # Erstelle eine neue Oberfläche
            self.add(ocean_surface)  # Füge die neue Oberfläche hinzu
            self.wait(0.033)  # Wartezeit für 60 FPS

# Um die Animation in 4K HD zu rendern, führe den folgenden Befehl im Terminal aus:
# manim -pqh dein_script_name.py MeerAnimation
