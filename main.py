from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class ballon_calc(MDApp):
    def build(self):
        return MDLabel(text="Hello, World", halign="center")



ballon_calc().run()