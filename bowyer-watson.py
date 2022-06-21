import numpy as np

from plotting import plot_configuration

from plotting import PlotOptions
from Point import Point
from Triangle import Triangle


# https://www.youtube.com/watch?v=GctAunEuHt4
# https://en.wikipedia.org/wiki/Bowyer–Watson_algorithm


def generate_points(N: int, scale:tuple) -> list:
    """Generate N 2D points uniformly and scale them to the bounds"""
    p = np.random.rand(N,2)
    p *= np.array(scale)
    
    return [Point(x,y) for (x,y) in p]


def generate_super_triangle(bounds: tuple) -> Triangle:
    """Generates a right-angled triangle that exactly encompasses the bounds."""
    return Triangle([Point(0,0), Point(bounds[0] * 2,0), Point(0, bounds[1] * 2)])


def triangulate(points: list[Point], bounds: tuple) -> list[Triangle]:

    super_triangle = generate_super_triangle(bounds)
    
    triangulation = set([super_triangle])

    for p in points:
        bad_triangles = set()
        polygon = set()

        for tri in triangulation:
            if tri.circum_circle.contains_point(p):
                bad_triangles.add(tri)
        
        all_edges = []
        for tri in bad_triangles:
            all_edges.extend(tri.edges)

        for edge in all_edges:
            if all_edges.count(edge) == 1:
                polygon.add(edge)

        for tri in bad_triangles:
            triangulation.remove(tri)
        
        for edge in polygon:
            new_tri = Triangle([edge.p1,edge.p2,p])
            triangulation.add(new_tri)
        

    # Remove all edges containing points from the super triangle
    tris = set(triangulation)
    for tri in triangulation:
        for p in super_triangle.points:
            if tri.has_point(p) and tri in tris:
                tris.remove(tri)

    return tris




if __name__ == "__main__":
    # Options
    # np.random.seed(20)
    N = 50
    bounds = (1,1)
    
    # Generate points
    p = generate_points(N, bounds)

    triangles = triangulate(p, bounds)

    plot_options = PlotOptions(title=f'N={N}', bounds=bounds)
    plot_configuration(options=plot_options, points=p, triangles=triangles,last_frame=True)