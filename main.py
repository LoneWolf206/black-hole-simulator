import pygame
from body import Body
from vector import Vector2D
from physics import gravitational_force

pygame.init()

WIDTH, HEIGHT = 1000, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Black Hole Simulator")
clock = pygame.time.Clock()

# Scale: 1 pixel = 1,000,000 metres
SCALE = 1e9
DT = 36000  # 1 hour per frame


sun  = Body(2e30, Vector2D(WIDTH/2 * SCALE, HEIGHT/2 * SCALE), Vector2D(0, 0))
earth = Body(5.97e24, Vector2D((WIDTH/2 + 150) * SCALE, HEIGHT/2 * SCALE), Vector2D(0, 29000))
mars  = Body(6.39e23, Vector2D((WIDTH/2 + 228) * SCALE, HEIGHT/2 * SCALE), Vector2D(0, 24000))

earth_trail = []
mars_trail = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    F_se = gravitational_force(earth, sun)
    earth.apply_force(F_se)
    sun.apply_force(F_se * -1)

    F_sm = gravitational_force(mars, sun)
    mars.apply_force(F_sm)
    sun.apply_force(F_sm * -1)

    F_em = gravitational_force(earth, mars)
    earth.apply_force(F_em)
    mars.apply_force(F_em * -1)

    earth.update(DT)
    mars.update(DT)
    sun.update(DT)
    

    mars_trail.append((int(mars.position.x / SCALE), int(mars.position.y / SCALE)))
    earth_trail.append((int(earth.position.x / SCALE), int(earth.position.y / SCALE)))
    if len(mars_trail) > 500:
        mars_trail.pop(0)
    if len(earth_trail) > 500:
        earth_trail.pop(0)

    screen.fill((0, 0, 0))

    for point in mars_trail:
        pygame.draw.circle(screen, (220, 60, 60), point, 1)
    for point in earth_trail:
        pygame.draw.circle(screen, (100, 180, 255), point, 1)

    ex = int(earth.position.x / SCALE)
    ey = int(earth.position.y / SCALE)
    mx = int(mars.position.x / SCALE)
    my = int(mars.position.y / SCALE)
    sun_x = int(sun.position.x / SCALE)
    sun_y = int(sun.position.y / SCALE)

    pygame.draw.circle(screen, (100, 180, 255), (ex, ey), 10)
    pygame.draw.circle(screen, (220, 60, 60), (mx, my), 5.3)
    pygame.draw.circle(screen, (255, 220, 0), (sun_x, sun_y), 109)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()