from contextlib import contextmanager
from enum import IntEnum
from functools import partial

from blessed import Terminal


class Color(IntEnum):
    WHITE = 1
    MAGENTA = 2
    RED = 3
    ORANGE = 4
    YELLOW = 5
    GREEN = 6
    CYAN = 7
    BLUE = 8
    BLACK = 9


echo = partial(print, end='', flush=True)


draw = False
color = Color.GREEN


@contextmanager
def optional(condition, context_manager):
    """
    https://stackoverflow.com/a/41251962/5147619
    """
    if condition:
        with context_manager:
            yield
    else:
        yield


def main():
    t = Terminal()
    with t.fullscreen():
        echo(t.clear)
        with t.cbreak():
            while True:
                with optional(draw, t.hidden_cursor()):
                    val = t.inkey()
                    if val.code == t.KEY_ESCAPE:
                        break
                    blit(t, val)


def blit(t, val):
    global draw
    global color
    if val in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        color = Color(int(val))
    if val.code == t.KEY_ENTER or val == ' ':
        draw = not draw
    if val.code in [t.KEY_DOWN, t.KEY_UP, t.KEY_LEFT, t.KEY_RIGHT]:
        echo(val)
    if val.code in [t.KEY_DELETE, t.KEY_BACKSPACE]:
        echo(t.clear)
        draw = False
    if draw:
        with t.location():
            echo(getattr(t, f"on_{color.name.lower()}")(' '))
