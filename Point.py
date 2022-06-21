from numpy import ndarray, sqrt
from dataclasses import dataclass

@dataclass(frozen=True, eq=True)
class Point:
    x: float
    y: float

    @property
    def arr(self) -> list:
        return [self.x,self.y]

    def dist_to(self, p) -> float:
        return sqrt((self.x - p.x)**2 + (self.y - p.y)**2)

    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y