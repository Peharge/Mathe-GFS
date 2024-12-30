from manim import *

class LightThemeBanner(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        banner = ManimBanner(dark_theme=False)
        self.play(banner.create())
        self.play(banner.expand())
        self.wait()
        self.play(Unwrite(banner))
        self.wait()