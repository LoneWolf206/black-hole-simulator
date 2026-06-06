class Vector2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)
    
    def __truediv__(self, scalar):
        return Vector2D(self.x / scalar, self.y / scalar)
    
    def magnitude(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            return Vector2D(0, 0)
        return self / mag
    
    def distance_to(self, other):
        return (self - other).magnitude()

    def __iadd__(self, other):
     self.x += other.x
     self.y += other.y
     return self
    
    def __repr__(self):
      return f"Vector2D({self.x:.2f}, {self.y:.2f})"