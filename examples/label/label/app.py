import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class LabelApp(toga.App):
    def startup(self):
        self.name = "test"

        # Main container
        main_box = toga.Box(style=Pack(direction=COLUMN, margin=10))
        
        # Label to display text
        self.label = toga.Label("Hello,\n Toga!", style=Pack(font_size=20, margin=10))
        main_box.add(self.label)

        self.slider = toga.Slider(min=10, max=50, value=20, on_change=self.update_font_size, style=Pack(margin=10))
        main_box.add(self.slider)

        # Create the main window
        self.main_window = toga.MainWindow(title=self.name)
        self.main_window.content = main_box
        self.main_window.show()

    def update_font_size(self, widget):
        """Update label font size based on slider value."""
        self.label.line_height = int(self.slider.value)

def main():
    return LabelApp("Label Example", "org.example.label").main_loop()
