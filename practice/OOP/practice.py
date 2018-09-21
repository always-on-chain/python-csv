class Line:
  def __init__(self,coor1,coor2):
    self.coor1 = coor1
    self.coor2 = coor2
  def distance(self):
    inside = (self.coor2[0] - self.coor1[0])**2 + (self.coor2[1] - self.coor1[1])**2
    return (inside)**float(0.5)
  def slope(self):
    return float(self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])

coordinate1 = (3,2)
coordinate2 = (8,10)
line = Line(coordinate1, coordinate2)
print line.distance()
print line.slope()

class Cylinder:
  def __init__(self, height=1, radius=1):
    self.height = height
    self.radius = radius
  def volume(self):
    return self.height * float(3.14) * (self.radius)**2
  def surface_area(self):
    top = float(3.14) * (self.radius**2)
    return (2 * top) + (2 * 3.14 * self.radius * self.height)

cylinder = Cylinder(2, 3) 
print cylinder.volume()
print cylinder.surface_area()
    

