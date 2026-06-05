from body import Body
from vector import Vector2D

b1=Body(100, Vector2D(0, 0), Vector2D(0, 0))
b2=Body(100, Vector2D(100, 0), Vector2D(0, 0))

def gravitational_force(b1, b2):
    G = 1000
    direction = (b2.position - b1.position).normalize()
    distance = b1.position.distance_to(b2.position)
    F = G * b1.mass * b2.mass / distance**2
    force = direction * F
    return force

force = gravitational_force(b1, b2)
b1.apply_force(force)
b2.apply_force(force* -1)

for i in range (100):
     direction = (b2.position - b1.position).normalize()

     distance = b1.position.distance_to(b2.position)

     F = G * b1.mass * b2.mass / distance**2

     force = direction * F

     b1.apply_force(force)
     b2.apply_force(force * -1)

     b1.update(0.1)
     b2.update(0.1)
