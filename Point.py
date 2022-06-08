from numpy import ndarray
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

    @property
    def arr(self) -> ndarray:
        return ndarray([self.x,self.y])