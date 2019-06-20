import signal
from blessed import Terminal
from functools import partial

echo = partial(print, end='', flush=True)

def center(t, s):
    x = (t.width - len(s))//2
    return t.move_x(x) + s

def middle(t, s):
    y = (t.height - s.count('\n'))//2
    return t.move_y(y) + s

draw = False

def main():
    t = Terminal()
    with t.fullscreen():
        echo(t.clear)
        with t.cbreak():
            while True:
                val = t.inkey()
                if val.lower() == 'q':
                    break
                blit(t, val)

def blit(t, val):
  global draw
  if val.code == t.KEY_ENTER:
      draw = not draw
      if draw:
          with t.location():
              echo(t.standout(' '))
  if val.code in [t.KEY_DOWN, t.KEY_UP, t.KEY_LEFT, t.KEY_RIGHT]:
      echo(val)
      if draw:
          with t.location():
              echo(t.standout(' '))
      return
  if val.code == t.KEY_BACKSPACE:
      echo(t.clear) 
      return
  with t.location():
      echo(val)
