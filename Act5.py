from random import shuffle
from turtle import *
from freegames import path

# Reemplaza los números con símbolos o emojis
symbols = ['😀', '😎', '😃', '😅', '😉', '😍', '😘', '😜',
           '🤓', '🥳', '😏', '😤', '🤖', '👽', '👾', '🧠',
           '🌟', '🔥', '🌈', '🎵', '⚽', '🏀', '🎯', '🎲',
           '🚗', '🚀', '🚁', '🛸', '⛵', '✈️', '🚂', '🏍️'] * 2

car = path('car.gif')
state = {'mark': None, 'taps': 0}
hide = [True] * 64

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']
    state['taps'] += 1  # Incrementa el contador de taps

    if mark is None or mark == spot or symbols[mark] != symbols[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 25, y + 10)  # Ajusta las coordenadas para centrar
        color('black')
        write(symbols[mark], align="center", font=('Arial', 20, 'normal'))  # Centra el símbolo

    # Muestra el número de taps
    up()
    goto(0, 180)
    color('black')
    write(f"Taps: {state['taps']}", align="center", font=('Arial', 16, 'normal'))

    # Detecta si todos los cuadros han sido destapados
    if all(not hidden for hidden in hide):
        goto(0, 0)
        color('red')
        write("¡Todos los cuadros han sido destapados!", align="center", font=('Arial', 20, 'bold'))

    update()
    ontimer(draw, 100)

shuffle(symbols)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()