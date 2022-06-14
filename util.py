import numpy as np

def diff(a:list, b:list) -> list:
    """
    Helper function for subtracting two lists - similarily to numpy arrays.
    eg. [2,5,8] - [1,5,3] = [1,0,5]
    """
    return [x-y for x,y in zip(a,b)]

def sort_points(x:list, x0:list):
    """
    Sort points by distance to a seed point x0, by the second order euclidean dist |xi - x0|**2
    """
    arr = sorted(x, key=lambda xi: np.linalg.norm(diff(xi,x0),2))
    return np.array(arr).tolist()
    


def circle_center(A:list, B:list, C:list) -> list[float]:
    """
    A function for calculting the Cartesian coordinates of the circumcenter given three 2D points (A,B,C).
    Aka. returns the center of a circle that goes through the points A, B and C.

    source: https://math.fandom.com/wiki/Circumscribed_circle
    """
    D = 2*(A[0]*(B[1]-C[1]) + B[0]*(C[1]-A[1]) + C[0]*(A[1]-B[1]))
    
    Ux = (A[0]**2+A[1]**2)*(B[1]-C[1])+(B[0]**2+B[1]**2)*(C[1]-A[1])+(C[0]**2+C[1]**2)*(A[1]-B[1])
    Uy = (A[0]**2+A[1]**2)*(C[0]-B[0])+(B[0]**2+B[1]**2)*(A[0]-C[0])+(C[0]**2+C[1]**2)*(B[0]-A[0])

    return np.array([Ux/D,Uy/D])




def angle(p1: list[float], p2: list[float], offset: float = 0) -> float:
    """ 
    Returns the angle in degrees between a point (p1) and another point (p2) - measured from the horizontal 
    axis plus an offset in degrees.
    """
    return (np.arctan2(p1[1]-p2[1], p1[0]-p2[0]) * 180/np.pi + 360 + offset) % 360

