from dataclasses import dataclass
from numpy.linalg import norm
from Point import Point


@dataclass
class Edge:
    p1: Point
    p2: Point

    def __eq__(self, __o: object) -> bool:
        return (self.p1 == __o.p1 and self.p2 == __o.p2) or (self.p1 == __o.p2 and self.p2 == __o.p1)

    @property
    def len(self) -> float:
        return norm(self.p1.arr-self.p2.arr)
