import pygame as pg
import random as r

pg.init()

res_x, res_y = 600, 600
screen = pg.display.set_mode((res_x, res_y))
clock = pg.time.Clock()
dt = 0
fps = 144
run = True
grid_size = 20
direction = 'right'
speed = 20
eat = False

points = [[40, 40], [60, 40], [80, 40]]


class Snake():
    def __init__(self, pts):
        self.length = 3
        self.points = pts
        self.timer = 0

    def update(self):
        for point in self.points:
            pg.draw.rect(screen, (0, 0, 255),
                         (point[0], point[1], grid_size, grid_size))

    def move(self):
        global eat
        self.timer += 1
        if self.timer >= speed:
            self.timer = 0
            if direction == 'right':
                self.points.append(
                    [self.points[-1][0]+grid_size, self.points[-1][1]])
                if not eat:
                    self.points.pop(0)
                else:
                    eat = False
            elif direction == 'down':
                self.points.append(
                    [self.points[-1][0], self.points[-1][1]+grid_size])
                if not eat:
                    self.points.pop(0)
                else:
                    eat = False
            elif direction == 'left':
                self.points.append(
                    [self.points[-1][0]-grid_size, self.points[-1][1]])
                if not eat:
                    self.points.pop(0)
                else:
                    eat = False
            elif direction == 'up':
                self.points.append(
                    [self.points[-1][0], self.points[-1][1]-grid_size])
                if not eat:
                    self.points.pop(0)
                else:
                    eat = False

            if points[-1][0] >= res_x:
                points[-1][0] = 0
            if points[-1][1] >= res_y:
                points[-1][1] = 0
            if points[-1][0] <= -grid_size:
                points[-1][0] = res_x
            if points[-1][1] <= -grid_size:
                points[-1][1] = res_y


class Food:
    def __init__(self):
        self.pos = [r.randint(0, int(res_x/grid_size)-1)*grid_size,
                    r.randint(0, int(res_y/grid_size)-1)*grid_size]
        if self.pos in points:
            self.pos = [r.randint(0, int(res_x/grid_size)-1)*grid_size,
                        r.randint(0, int(res_y/grid_size)-1)*grid_size]

    def draw(self):
        pg.draw.rect(screen, (255, 0, 0),
                     (self.pos[0], self.pos[1], grid_size, grid_size))

    def create(self):
        self.pos = [r.randint(0, int(res_x/grid_size)-1)*grid_size,
                    r.randint(0, int(res_y/grid_size)-1)*grid_size]
        if self.pos in points:
            self.pos = [r.randint(0, int(res_x/grid_size)-1)*grid_size,
                        r.randint(0, int(res_y/grid_size)-1)*grid_size]


snake = Snake(points)
food = Food()

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_d and direction != 'left':
                direction = 'right'
            elif event.key == pg.K_a and direction != 'right':
                direction = 'left'
            elif event.key == pg.K_s and direction != 'up':
                direction = 'down'
            elif event.key == pg.K_w and direction != 'down':
                direction = 'up'
            elif event.key == pg.K_SPACE:
                speed = 10
        if event.type == pg.KEYUP:
            if event.key == pg.K_SPACE:
                speed = 20

    screen.fill((0, 0, 0))

    snake.update()
    snake.move()
    food.draw()

    if points[-1] == food.pos:
        food.create()
        eat = True

    for i in range(0, len(points)-1):
        if points[-1] == points[i]:
            run = False

    for i in range(0, res_x-grid_size, grid_size):
        pg.draw.line(screen, (100, 100, 100),
                     (i+grid_size, 0), (i+grid_size, res_y), 1)
    for i in range(0, res_y-grid_size, grid_size):
        pg.draw.line(screen, (100, 100, 100),
                     (0, i+grid_size), (res_x, i+grid_size), 1)

    pg.display.flip()

    dt = clock.tick(fps) / 100


pg.quit()
