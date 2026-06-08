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
DT = 10000  # 1 hour per frame


sun  = Body(2e30, Vector2D(WIDTH/2 * SCALE, HEIGHT/2 * SCALE), Vector2D(0, 0))
earth = Body(5.97e24, Vector2D((WIDTH/2 + 150) * SCALE, HEIGHT/2 * SCALE), Vector2D(0, 29000))
mars  = Body(6.39e23, Vector2D((WIDTH/2 + 228) * SCALE, HEIGHT/2 * SCALE), Vector2D(0, 24000))

earth_trail = []
mars_trail = []
sun_trail = []
frame_count = 0
BLACK_HOLE_SPAWN = 300  # 5 seconds at 60fps
bodies = [sun, earth, mars]
black_holes = []  # black hole not included yet
ABSORPTION_RADIUS = 11  # pixels

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            c_x, c_y = pygame.mouse.get_pos()
            new_bh = Body(2e31, Vector2D(c_x * SCALE, c_y * SCALE), Vector2D(0, -35000))
            bodies.append(new_bh)
            black_holes.append(new_bh)

    for i in range(len(bodies)):
        for j in range(i + 1, len(bodies)):
            force = gravitational_force(bodies[i], bodies[j])
            bodies[i].apply_force(force)
            bodies[j].apply_force(force* -1)

    earth.update(DT)
    mars.update(DT)
    sun.update(DT)
    for black_hole in black_holes:
        black_hole.update(DT)

    for bh in black_holes:
       for body in [earth, mars, sun]:
          if body in bodies:
             dist_pixels = bh.position.distance_to(body.position) / SCALE
             if dist_pixels < ABSORPTION_RADIUS:
                 bodies.remove(body)

    if len(mars_trail) > 500:
        mars_trail.pop(0)
    if len(earth_trail) > 500:
        earth_trail.pop(0)
    if len(sun_trail) > 500:
        sun_trail.pop(0)

    screen.fill((0, 0, 0))
    

    for point in mars_trail:
        pygame.draw.circle(screen, (220, 60, 60), point, 1)
    for point in earth_trail:
        pygame.draw.circle(screen, (100, 180, 255), point, 1)
    for point in sun_trail:
        pygame.draw.circle(screen, (255, 220, 0), point, 1)

    if earth in bodies:
      ex = int(earth.position.x / SCALE)
      ey = int(earth.position.y / SCALE)
    if mars in bodies:
      mx = int(mars.position.x / SCALE)
      my = int(mars.position.y / SCALE)
    if sun in bodies:
      sun_x = int(sun.position.x / SCALE)
      sun_y = int(sun.position.y / SCALE)

    if earth in bodies:
       pygame.draw.circle(screen, (100, 180, 255), (ex, ey), 10)
    if mars in bodies:
       pygame.draw.circle(screen, (220, 60, 60), (mx, my), 5)
    if sun in bodies:
       pygame.draw.circle(screen, (255, 220, 0), (sun_x, sun_y), 30)
    # after drawing sun/earth/mars:
    for bh in black_holes:
       bh_x = int(bh.position.x / SCALE)
       bh_y = int(bh.position.y / SCALE)
       pygame.draw.circle(screen, (255, 140, 0), (bh_x, bh_y), 11)
       pygame.draw.circle(screen, (0, 0, 0), (bh_x, bh_y), 10)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()