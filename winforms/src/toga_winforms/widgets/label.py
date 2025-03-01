from decimal import ROUND_UP

import System.Windows.Forms as WinForms
from System.Drawing import SolidBrush, PointF
from travertino.size import at_least

from toga.colors import TRANSPARENT
from toga_winforms.libs.fonts import TextAlignment

from .base import Widget

class Label(Widget):
    def create(self):
        self.native = WinForms.Label()
        self._default_background_color = TRANSPARENT
        self.native.Text = ""  
        self.native.Paint += self.custom_paint

    def set_text_align(self, value):
        self.text_align = value

    def set_line_height(self, value):
        self.line_height = value

    def get_text(self):
        return self.native.Text

    def set_text(self, value):
        self.custom_text = value
        self.update_size()

    def rehint(self):
        self.interface.intrinsic.width = self.scale_out(
            at_least(self.native.PreferredSize.Width), ROUND_UP
        )
        self.interface.intrinsic.height = self.scale_out(
            self.native.Height, ROUND_UP
        )

    def update_size(self):
        num_lines = self.custom_text.count("\n") + 1 
        new_height = num_lines * self.line_height  
        self.native.Height = new_height 

    def custom_paint(self, _, e):
        brush = SolidBrush(self.native.ForeColor)
        y = 0

        for line in self.custom_text.split("\n"):
            e.Graphics.DrawString(line, self.native.Font, brush, PointF(0, y))
            y += self.line_height 