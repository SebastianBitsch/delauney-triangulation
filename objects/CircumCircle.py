from Point import Point
from numpy import sqrt

class CircumCircle():

    def __init__(self, A: Point, B: Point, C: Point) -> None:
        self.center = self.calculate_center(A,B,C)
        self.radius = self.calculate_radius(A,B,C)


    def contains_point(self, p:Point) -> bool:
        """ Check if a point is within the area of the circle"""
        return p.dist_to(self.center) < self.radius


    def calculate_radius(self, A:Point, B:Point, C:Point) -> float:
        """
        Calculates the radius of a circle given three points on its circumference
        Source: https://artofproblemsolving.com/wiki/index.php/Circumradius
        """
        a = A.dist_to(B)
        b = B.dist_to(C)
        c = C.dist_to(A)
        s = 0.5 * (a + b + c)
        A = sqrt(s*(s-a)*(s-b)*(s-c))
        R = (a*b*c) / (4*A)
        return R


    def calculate_center(self, A:Point, B:Point, C:Point) -> Point:
        """
        A function for calculting the Cartesian coordinates of the circumcenter given three 2D points (A,B,C).
        Aka. returns the center of a circle that goes through the points A, B and C.

        source: https://math.fandom.com/wiki/Circumscribed_circle
        """
        D = 2*(A.x*(B.y-C.y) + B.x*(C.y-A.y) + C.x*(A.y-B.y))
        
        Ux = (A.x**2+A.y**2)*(B.y-C.y)+(B.x**2+B.y**2)*(C.y-A.y)+(C.x**2+C.y**2)*(A.y-B.y)
        Uy = (A.x**2+A.y**2)*(C.x-B.x)+(B.x**2+B.y**2)*(A.x-C.x)+(C.x**2+C.y**2)*(B.x-A.x)

        return Point(Ux/D,Uy/D)
