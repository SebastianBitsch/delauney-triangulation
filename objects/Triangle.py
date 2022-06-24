from Point import Point
from Edge import Edge
from objects.CircumCircle import CircumCircle

class Triangle:
    
    def __init__(self, points: list[Point]) -> None:
        assert len(points) == 3
        
        self.points = points
        self.edges = [
            Edge(points[0],points[1]),
            Edge(points[1],points[2]),
            Edge(points[2],points[0])
        ]
        self.circum_circle = CircumCircle(*points)

    def __iter__(self):
        yield from self.edges

    def has_edge(self, edge:Edge) -> bool:
        return 0 < sum([edge == e for e in self.edges])

    def has_point(self, point:Point) -> bool:
        return 0 < sum([point == p for p in self.points])

    def get_points(self):
        return [p.arr for p in self.points]