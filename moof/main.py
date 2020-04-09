import signal
from contextlib import contextmanager
from datetime import datetime, timezone
from enum import IntEnum
from functools import partial
from time import time_ns

from blessed import Terminal


def main():
    App(Terminal()).run()


class App():
    def __init__(self, term):
        self.term = term
        self.stop = False
        self.draw = False
        self.color = Color.GREEN
        self.width = term.width
        self.height = term.height
        self.keys = []

    def run(self):
        t = self.term

        def on_resize(sig, action):
            raise Reset()

        signal.signal(signal.SIGWINCH, on_resize)

        with t.fullscreen():
            echo(t.clear)
            with t.cbreak():
                while self.step():
                    pass

    def step(self):
        t = self.term
        try:
            with optional(self.draw, t.hidden_cursor()):
                val = t.inkey()

                self.record_key(val)

                if val.code == t.KEY_ESCAPE:
                    self.write()
                    return False

                if val in (str(c.value) for c in list(Color)):
                    self.color = Color(int(val))
                if val.code == t.KEY_ENTER or val == ' ':
                    self.draw = not self.draw
                if val.code in [t.KEY_DOWN, t.KEY_UP, t.KEY_LEFT, t.KEY_RIGHT]:
                    echo(val)
                if val.code in [t.KEY_DELETE, t.KEY_BACKSPACE]:
                    raise Reset()
                if self.draw:
                    with t.location():
                        echo(getattr(t, f"on_{self.color.name.lower()}")(' '))
        except Reset:
            self.write()
            self.__init__(self.term)
            echo(t.clear)

        return True

    def record_key(self, val):
        self.keys.append(
            (time_ns(), ord(val[0]) if val.code is None else val.code))

    def write(self):
        if self.keys == []:
            return

        name = "moof-" + \
            datetime.now(timezone.utc).isoformat(timespec='seconds')

        with open(name, 'w') as f:
            print("<terminal width> <terminal height>", file=f)
            print(self.width, self.height, end='\n\n', file=f)
            print("<unix time in ns> <key code>", file=f)
            for t, k in self.keys:
                print(t, k, sep=' ', file=f)


class Reset(Exception):
    pass


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


echo = partial(print, end='', flush=True)


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
