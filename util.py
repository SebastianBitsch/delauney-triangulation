import numpy as np

def diff(a,b):
    return [x-y for x,y in zip(a,b)]

def sort_points(x, x0: list):
    """ Sort points by distance to a seed point x0, by the second order euclidean dist |xi - x0|**2"""
    arr = sorted(x, key=lambda xi: np.linalg.norm(diff(xi,x0),2))
    return np.array(arr).tolist()
    


def circle_center(A,B,C) -> list[float]:
    D = 2*(A[0]*(B[1]-C[1]) + B[0]*(C[1]-A[1]) + C[0]*(A[1]-B[1]))
    Ux = (A[0]**2+A[1]**2)*(B[1]-C[1])+(B[0]**2+B[1]**2)*(C[1]-A[1])+(C[0]**2+C[1]**2)*(A[1]-B[1])
    Uy = (A[0]**2+A[1]**2)*(C[0]-B[0])+(B[0]**2+B[1]**2)*(A[0]-C[0])+(C[0]**2+C[1]**2)*(B[0]-A[0])
    return np.array([Ux/D,Uy/D])


def angle(point: list[float], center: list[float]) -> float:
    """ Returns the angle in degrees between a point and a center"""
    return (np.arctan2(point[1]-center[1], point[0]-center[0]) * 180/np.pi + 360) % 360

def angle(point: list[float], center: list[float], offset: float) -> float:
    """ Returns the angle in degrees between a point and a center"""
    return (np.arctan2(point[1]-center[1], point[0]-center[0]) * 180/np.pi + 360 + offset) % 360

