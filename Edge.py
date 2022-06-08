from dataclasses import dataclass
from numpy.linalg import norm
from Point import Point


@dataclass
class Edge:
    p1: Point
    p2: Point

    def len(self) -> float:
        return norm(self.p1.arr-self.p2.arr)
