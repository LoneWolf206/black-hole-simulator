import matplotlib.pyplot as plt
import matplotlib.animation as animation
from body import Body
from vector import Vector2D
from physics import gravitational_force

earth = Body(5.97e24, Vector2D(0, 0), Vector2D(0, 0))
moon = Body(7.34e22, Vector2D(3.84e8, 0), Vector2D(0, 1022))

DT = 3600
positions = []

for i in range(720):  # 30 days
    F = gravitational_force(earth, moon)
    earth.apply_force(F)
    moon.apply_force(F * -1)
    earth.update(DT)
    moon.update(DT)
    positions.append((moon.position.x, moon.position.y))

xs = [p[0] for p in positions]
ys = [p[1] for p in positions]

plt.figure(figsize=(6,6))
plt.plot(xs, ys)
plt.plot(0, 0, 'yo', markersize=15, label='Earth')
plt.title('Moon orbit (30 days)')
plt.axis('equal')
plt.savefig('orbit.png')
print("Saved orbit.png")