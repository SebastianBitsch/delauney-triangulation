from copy import deepcopy
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm

from util import circle_center, angle, sort_points


def get_closest_point(x, x0, xj):
    """
    Find the point xk that creates the smallest circum-circle with x0 and xj and record the cetner of the circum-circle C.
    Return x, xj and C
    """
    # Running variables
    A_min = np.Infinity
    A_min_index = None

    # Loop through all points
    for i, xk in enumerate(x):
        a = np.linalg.norm(xk - x0)
        b = np.linalg.norm(x0 - xj)
        c = np.linalg.norm(xj - x0)
        s = (a+b+c) * 0.5
        A = (np.pi * 0.25) * s**2
        if A < A_min:
            A_min = A
            A_min_index = i

    # Update x and declare xk and C
    xk = x[A_min_index]
    x = np.delete(x, A_min_index, 0)
    C = circle_center(x0,xj,xk)
    return (x,xk,C)


def get_closest_point(x, x0, xj):
    """
    Find the point xk that creates the smallest circum-circle with x0 and xj and record the cetner of the circum-circle C.
    Return x, xj and C
    """
    # Running variables
    A_min = np.Infinity
    A_min_index = None

    # Loop through all points
    for i, xk in enumerate(x):
        a = np.linalg.norm(xk - x0)
        b = np.linalg.norm(x0 - xj)
        c = np.linalg.norm(xj - x0)
        s = (a+b+c) * 0.5
        A = (np.pi * 0.25) * s**2
        if A < A_min:
            A_min = A
            A_min_index = i

    # Update x and declare xk and C
    xk = x[A_min_index]
    x = np.delete(x, A_min_index, 0)
    C = circle_center(x0,xj,xk)
    return (x,xk,C)


def visible_edges(p, points):
    angles = np.array([angle(x,p) for x in points])

    # If the triangle collides with the positive x-axis from the point - rotate 90 degrees to
    if np.array([270 < x or x < 180 for x in angles]).all():
        angles += 90
        angles %= 360

    i = np.argmax(angles)
    min_angle = np.min(angles)

    edges = []
    while True:
        edges.append((points[i%3],points[(i+1)%3]))
        i += 1
        if angles[i%3] == min_angle:
            break
    
    return edges

if __name__ == "__main__":
    triangles = []
    edges = []
    points = []

    # Generate points
    N = 20
    x = np.random.rand(N,2)
    all_x = deepcopy(x)

    # Select first point at random
    x0 = x[0]
    x = np.delete(x,0,0)

    # Find the closest point to x0
    x = sort_points(x,x0)

    # Get closest point to x0
    xj = x[0]
    x = np.delete(x,0,0)

    x, xk, C = get_closest_point(x, x0, xj)

    # Add triangle and edges
    tri = sorted([x0,xk,xj], key=lambda x: angle(x,C))
    
    triangles.append(tri)
    edges.extend([[tri[0],tri[1]],[tri[1],tri[2]],[tri[2],tri[0]]])
    points.extend([x0,xk,xj])

    # Sort points according to distance from center
    x = sort_points(x,C)
    xi = x[0]
    x = np.delete(x,0,0)

    # Get visible edges from the point
    # TODO: SHOULD TAKE POINTS; - BUT WONT WORK BECAUSE 
    # APPROACH CURRENTLY REQUIRES POINTS TO BE ORDERED
    # COUNTER-CLOCKWISE
    e = visible_edges(xi, tri)

    # For every edge add new triangle, edges and point
    for edge in e:
        tri = sorted([edge[0],edge[1],xi], key=lambda x: angle(x,C))

        triangles.append(tri)
        edges.extend([[tri[0],tri[1]],[tri[1],tri[2]],[tri[2],tri[0]]])
        points.append(xi)

    
    plt.figure(figsize=[7,7])
    plt.axes([0.1, 0.1, 0.8, 0.8], xlim=(0, 1), ylim=(0, 1))
    plt.scatter(x=all_x[:,0],y=all_x[:,1])
    plt.scatter(x=[x0[0]],y=[x0[1]],label="x0")
    plt.scatter(x=[xj[0]],y=[xj[1]],label="xj")
    plt.scatter(x=[xk[0]],y=[xk[1]],label="xk")
    plt.scatter(x=[xi[0]],y=[xi[1]],label="xi")
    for edge in edges:
        plt.plot([edge[0][0],edge[1][0]],[edge[0][1],edge[1][1]],"r-")
    plt.legend()

    points_whole_ax = 7 * 0.8 *72    # 1 point = dpi / 72 pixels
    for tri in triangles:
        t1 = plt.Polygon(tri,fill=False)
        plt.gca().add_patch(t1)

    plt.show()