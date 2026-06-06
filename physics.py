from body import Body
from vector import Vector2D

G = 6.674e-11

def gravitational_force(earth, moon):
    direction = (moon.position - earth.position).normalize()
    distance = earth.position.distance_to(moon.position)
    if distance < 1:
        return
    F = G * earth.mass * moon.mass / distance**2
    force = direction * F
    return force



