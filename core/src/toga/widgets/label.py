from __future__ import annotations

from typing import Any

from .base import StyleT, Widget


class Label(Widget):
    def __init__(
        self,
        text: str,
        id: str | None = None,
        style: StyleT | None = None,
        line_height: float | None = None,
        **kwargs,
    ):
        """Create a new text label.

        :param text: Text of the label.
        :param id: The ID for the widget.
        :param style: A style object. If no style is provided, a default style
            will be applied to the widget.
        :param line_height: The line height for the label.
        :param kwargs: Initial style properties.
        """
        super().__init__(id, style, **kwargs)

        self.text = text
        self.line_height = line_height

    def _create(self) -> Any:
        label = self.factory.Label(interface=self)
        if self.line_height is not None:
            label.set_line_height(self.line_height)
        return label

    def focus(self) -> None:
        """No-op; Label cannot accept input focus."""
        pass

    @property
    def text(self) -> str:
        """The text displayed by the label.

        ``None``, and the Unicode codepoint U+200B (ZERO WIDTH SPACE), will be
        interpreted and returned as an empty string. Any other object will be
        converted to a string using ``str()``.
        """
        return self._impl.get_text()

    @text.setter
    def text(self, value: object) -> None:
        if value is None or value == "\u200b":
            text = ""
        else:
            text = str(value)

        self._impl.set_text(text)
        self.refresh()

    @property
    def line_height(self) -> float | None:
        return self._line_height

    @line_height.setter
    def line_height(self, value: float | None) -> None:
        self._line_height = value
        if self._impl:
            self._impl.set_line_height(value)
        self.refresh()
