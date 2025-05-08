# Create a Python class called Point that represents a point in 2D space.
#  Implement the __init__ method to initialize the x and y coordinates of the point. 
# Implement the __eq__ method to compare two Point objects for equality based on their coordinates.

class Point:
    def __init__ (self, x, y):
        self.x =x
        self.y= y

    def __eq__(self, other):
        return(self.x == other.x and self.y == other.y)
    
point1 =Point(1,2)
point2 =Point(1,4)
print(point1 == point2)