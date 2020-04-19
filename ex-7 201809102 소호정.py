import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at Point posn, with width w, height h """
        self.corner = posn 
        self.width = w
        self.height = h

    def __str__(self):
        return f"({self.corner},{self.width},{self.height})"  
    
    def __repr__(self):
        return  "Rectangle({0}, {1}, {2})".format(
            repr(self.corner), self.width, self.height)
    
    def grow(self, delta_width, delta_height):
        """ Grow (or shrink) this object by the deltas """
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        """ Move this object by the deltas """
        self.corner.x += dx
        self.corner.y += dy

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width * 2) + (self.height * 2)
    
    def flip(self):
        tmp = self.width
        self.width = self.height
        self.height = tmp
        return self.width, self.height

    def contains(self, other):
        if(self.width > other.x) and (self.height > other.y):
            if(other.x >= self.corner.x) or (other.y >= self.corner.y):
                return True
            else: pass
        

  
class Point:    
    """2D Point class"""
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __repr__(self):
        return "Point({0}, {1})".format(self.x, self.y)

    def distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2) ** 0.5
    
    def midpoint(self, other):
        """ Return the midpoint of points p1 and p2 """
        mx = (self.x + other.x)/2
        my = (self.y + other.y)/2
        return Point(mx, my)
    
    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)
    
    def __ne__(self, other):
        return (self.x, self.y) != (other.x, other.y)
    
    def reflect_x(self):
            return Point(self.x, -self.y)

    def slope_from_origin(self):
        try:
            return self.x / self.y
        except ZeroDivisionError:
            print("Zero cannot be divided. Please check the number.")

    def get_line_to(self, other):
        try: 
            a = int((other.y - self.y) / (other.x - self.x)) #기울기 구하기
            b = self.y - (a * self.x)
            return a, b
        except ZeroDivisionError:
            print("Zero cannot be divided. Please check the numbers.")

if __name__ == "__main__":
    test(Point(3,5).reflect_x() == Point(3, -5))
    test(Point(10,4).slope_from_origin() == 2.5)
    test(Point(4, 11).get_line_to(Point(6, 15)) == (2, 3))

    r = Rectangle(Point(100, 50), 10, 5)
    test(r.area() == 50)
    test(r.perimeter() == 30)
    r.flip()    # this method modifies its attributes
    test(r.width == 5 and r.height == 10)

    r = Rectangle(Point(0, 0), 10, 5)
    test(r.contains(Point(0, 0)))
    test(r.contains(Point(3, 3)))
    test(not r.contains(Point(3, 7)))
    test(not r.contains(Point(3, 5)))
    test(r.contains(Point(3, 4.99999)))
    test(not r.contains(Point(-3, -3)))

