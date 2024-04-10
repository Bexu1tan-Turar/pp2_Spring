import pygame as pg

pg.init()

clock = pg.time.Clock()

width, height = 640, 480
screen = pg.display.set_mode((width, height))
white = (255, 255, 255)
step = 20
x, y = 50, 50
dx, dy = 0, 0
radius = 25
screen.fill(white)

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    key = pg.key.get_pressed()

    dx, dy = 0, 0

    if key[pg.K_UP]: dy = -1
    if key[pg.K_DOWN]: dy = 1
    if key[pg.K_LEFT]: dx = -1
    if key[pg.K_RIGHT]: dx = 1

    if radius <= x + step * dx <= width - radius:
        x += step * dx
    if radius <= y + step * dy <= height - radius:
        y += step * dy

    screen.fill(white)
    pg.draw.circle(screen, (255, 0, 0), (x, y), radius)

    pg.display.flip()
    clock.tick(60)

pg.quit()