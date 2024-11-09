from manim import *

# Definiere hier deine eigene Mathe_GFS Animation
class MatheGFS(Animation):
    def __init__(self, mobject, **kwargs):
        super().__init__(mobject, **kwargs)

    def create(self):
        self.mobject.set_color(YELLOW)  # Beispiel für eine einfache Farbänderung
        self.mobject.scale(1.5)          # Beispiel für eine Skalierung

# Definiere hier deine eigene Julian_Kropff Animation
class JulianKropff(Animation):
    def __init__(self, mobject, **kwargs):
        super().__init__(mobject, **kwargs)

    def create(self):
        self.mobject.set_color(RED)      # Beispiel für eine einfache Farbänderung
        self.mobject.scale(1.5)

# Definiere hier deine eigene TGM_J2 Animation
class TGMJ2(Animation):
    def __init__(self, mobject, **kwargs):
        super().__init__(mobject, **kwargs)

    def create(self):
        self.mobject.set_color(BLUE)     # Beispiel für eine einfache Farbänderung
        self.mobject.scale(1.5)

class Indications(Scene):
    def construct(self):
        # Definiere hier die Animationen
        indications = [MatheGFS, JulianKropff, TGMJ2, FocusOn, Indicate, ShowPassingFlash, Wiggle]
        # Die Klassennamen jetzt in Dollarzeichen einschließen
        names = [Tex(f"${i.__name__}$").scale(3) for i in indications]

        self.add(names[0])
        for i in range(len(names)):
            if indications[i] is TGMJ2:
                self.play(TGMJ2(names[i]))  # TGM_J2 mit dem entsprechenden Tex-Objekt aufrufen
            elif indications[i] is ShowPassingFlash:
                self.play(ShowPassingFlash(Underline(names[i])))
            else:
                self.play(indications[i](names[i]))  # Hier wird die angepasste Animation verwendet
            self.play(AnimationGroup(
                FadeOut(names[i], shift=UP*1.5),
                FadeIn(names[(i+1)%len(names)], shift=UP*1.5),
            ))
