import pgzrun
import random

WIDTH = 840
HEIGHT = 620

def draw():
    rect_width = 500
    rect_height = 500
    r = 255
    g = 36
    b = 255
    for i in range(7):
        rect = Rect((0,0), (rect_width, rect_height))
        rect.center = (WIDTH/2, HEIGHT/2)
        screen.draw.rect(rect, (r, g, b))
        rect_width += 20
        rect_height += 20
        r -= 15
        g += 30
        b -= 15

pgzrun.go()