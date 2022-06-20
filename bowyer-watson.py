import numpy as np

#from util import generate_points
from plotting import PlotOptions, plot_configuration
from Point import Point
from Triangle import Triangle

def generate_points(N: int, scale:tuple) -> list:
    """Generate N 2D points uniformly and scale them to the bounds"""
    x = np.random.rand(N,2)
    x[:,0] *= scale[0]
    x[:,1] *= scale[1]
    
    return [Point(x,y) for (x,y) in x]

def triangulate(points, options):

    super_triangle = Triangle([Point(-1,-2),Point(2,-2),Point(0.5,4)])
    triangulation = [super_triangle]

    for p in points:
        bad_triangles = set()

        for tri in triangulation:            
            if tri.circum_circle.contains_point(p):
                bad_triangles.add(tri)
            
        polygon = set()

        for tri in bad_triangles:
            for edge in tri:
                pass
                # https://en.wikipedia.org/wiki/Bowyer–Watson_algorithm
                # TODO: Continue from here


if __name__ == "__main__":
    # Options
    np.random.seed(20)
    bounds = (1,1)
    N = 4

    # Generate points    
    x = generate_points(N, bounds)
    print(x)
    options = PlotOptions(title=f'N={N}', bounds=bounds)
        
    triangles = triangulate(x, options)