from vector import Vector2D

class Body:

    def __init__(self, mass, position, velocity):
        self.mass=mass
        self.position=position
        self.velocity=velocity
        self.acceleration=Vector2D(0, 0)

    def apply_force(self, force):
        self.acceleration += force / self.mass
    
    def update(self, dt):
        self.velocity+=self.acceleration * dt
        self.position+=self.velocity * dt
        self.acceleration=Vector2D(0, 0)
    
    
