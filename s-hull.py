from copy import copy
import numpy as np

from util import circle_center, angle, sort_points, diff, generate_points
from plotting import PlotOptions, plot_shull


# TODO: DOESNT WORK with 10 points and seed 9

# np.random.seed(9) # 


def get_closest_point(x:list, x0:list, xj:list) -> tuple:
    """
    Find the point xk that creates the smallest circum-circle with x0 and xj and record the cetner of the circum-circle C.
    Return x, xj and C
    """
    # Running variables
    A_min = np.Infinity
    A_min_index = None

    # Loop through all points
    for i, xk in enumerate(x):
        a = np.linalg.norm(diff(xk, x0))
        b = np.linalg.norm(diff(x0, xj))
        c = np.linalg.norm(diff(xj, x0))
        s = (a+b+c) * 0.5
        A = (np.pi * 0.25) * s**2
        if A < A_min:
            A_min = A
            A_min_index = i

    # Update x and declare xk and C
    xk = x.pop(A_min_index)
    C = circle_center(x0,xj,xk)
    return (x,xk,C)


def visible_edges(p0:list, points:list) -> list:
    """
    Find and return the visible edges from point p
    source: https://math.stackexchange.com/a/1743061
    """

    # Initialize
    offset = 0
    angle_span = np.Infinity
    n = len(points)
    edges = []
    
    # If the angle span is above 180, shift the axis using the offset. Done to avoid spillover from 0,360 degrees
    while 180 < angle_span:
        offset += 1
        angles = np.array([angle(x,p0,offset) for x in points])
        angle_span = np.max(angles) - np.min(angles)

    i = np.argmax(angles)
    min_angle = np.min(angles)

    # Keep traversing and adding edges until we reach the minimum angle
    while True:
        edges.append([points[i%n],points[(i+1)%n]])
        i += 1
        if angles[i%n] == min_angle:
            break
    
    return edges


def triangulate(x: list, plotting_options:PlotOptions = None) -> list:

    triangles = []
    all_edges = []
    outer_edges = []

    # Select first point at random
    x0 = x.pop(0)
    
    # Get closest point to x0
    x = sort_points(x,x0)
    xj = x.pop(0)

    x, xk, C = get_closest_point(x, x0, xj)
    
    # Add triangle and edges
    tri = sorted([x0,xk,xj], key=lambda x: angle(x,C))
    triangles.append(tri)
    
    all_edges.extend([[tri[0],tri[1]],[tri[1],tri[2]],[tri[2],tri[0]]])
    outer_edges = copy(all_edges)

    # Sort points according to distance from center
    x = sort_points(x,C)

    while x:
        print(f"Points left: {len(x)}")

        xi = x.pop(0)
        
        # Get the outer vertices
        all_verts = [p for e in outer_edges for p in e]
        outer_verts = np.unique(all_verts, axis=0).tolist()

        # Sort the outer verts to lie in counter clockwise direction
        # TODO: Doesnt always work
        outer_verts = sorted(outer_verts, key=lambda x: angle(x,C))

        # Get visible edges from the point
        e = visible_edges(xi, outer_verts)

        # For every edge add new triangle, edges and point
        for i, edge in enumerate(e):
            tri = sorted([edge[0],edge[1],xi], key=lambda x: angle(x,C))

            triangles.append(tri)

            # Add first new edge
            if not [edge[0],xi] in all_edges:
                all_edges.append([edge[0],xi])
            elif not [xi, edge[0]] in all_edges:
                all_edges.append([xi, edge[0]])

            # Add second new edge
            if not [edge[1],xi] in all_edges:
                all_edges.append([edge[1],xi])
            elif not [xi, edge[1]] in all_edges:
                all_edges.append([xi, edge[1]])

            # Remove outer edge that formed the base of triangle
            if edge in outer_edges:
                outer_edges.remove(edge)
            elif [edge[1],edge[0]] in outer_edges:
                outer_edges.remove([edge[1],edge[0]])

            # Convoluted way of not adding the middle edge 
            if len(e) == 1:
                outer_edges.extend([[edge[0],xi],[edge[1],xi]])
            else:
                if i == 0:
                    outer_edges.append([edge[0],xi])
                elif i == len(e)-1:
                    outer_edges.append([edge[1],xi])
    
        
        # Plot configuration if options are provided
        if plotting_options:
            plot_shull(
                options=plotting_options, 
                points=np.array(x), 
                inner_edges=all_edges, 
                outer_edges=outer_edges, 
                last_frame=len(x)==0, 
                special_points=[xi]
            )
    
    return triangles


if __name__ == "__main__":
    # Options
    bounds = (1,1)
    N = [5,10,25,50,100,200]

    # Generate points
    for n in N:
        x = generate_points(n, bounds).tolist()
        options = PlotOptions(title=f'N={n}', bounds=bounds)
        
        triangles = triangulate(x, options)