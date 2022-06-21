import numpy as np
import matplotlib.pyplot as plt

#from util import generate_points
from plotting import PlotOptions
from Point import Point
from Triangle import Triangle

# https://www.youtube.com/watch?v=GctAunEuHt4
# https://en.wikipedia.org/wiki/Bowyer–Watson_algorithm


def generate_points(N: int, scale:tuple) -> list:
    """Generate N 2D points uniformly and scale them to the bounds"""
    x = np.random.rand(N,2)
    x[:,0] *= scale[0]
    x[:,1] *= scale[1]
    
    return [Point(x,y) for (x,y) in x]

def triangulate(points: list[Point]) -> list[Triangle]:

    super_triangle = Triangle([Point(-1,-2),Point(2,-2),Point(0.5,4)])
    triangulation = [super_triangle]

    for p in points:
        bad_triangles = set()

        for tri in triangulation:
            if tri.circum_circle.contains_point(p):
                bad_triangles.add(tri)
            
        polygon = set()

        all_edges = []
        for tri in bad_triangles:
            all_edges.extend(tri.edges)

        for edge in all_edges:
            if all_edges.count(edge) == 1 and not edge in polygon:
                polygon.add(edge)

        for tri in bad_triangles:
            triangulation.remove(tri)
        
        for edge in polygon:
            new_tri = Triangle([edge.p1,edge.p2,p])
            triangulation.append(new_tri)
    
    tris = set(triangulation)
    for tri in triangulation:
        for p in super_triangle.points:
            if tri.has_point(p) and tri in tris:
                tris.remove(tri)

    return tris



def plot_configuration(options: PlotOptions, points:list[Point], triangles:list[Triangle], last_frame:bool = False, special_points:list = [], labels:list = []):

    plt.figure(figsize=options.fig_size)
    plt.axes(xlim=(0, options.bounds[0]), ylim=(0, options.bounds[0]))
    plt.title(options.title, loc='left')
    plt.title("Triangulation", loc='center')
    plt.xticks([])
    plt.yticks([])


    for tri in triangles:
        t = plt.Polygon(tri.get_points(), edgecolor=options.triangle_color, fill=False)
        plt.gca().add_patch(t)


    points = np.array([p.arr for p in points])
    if 0 < len(points):
        plt.scatter(x=points[:,0],y=points[:,1], color=options.point_color, marker='o')
    
    for point in special_points:
        if labels:
            plt.scatter(x=[point[0]],y=[point[1]],labels=labels,color=options.special_color)
        else:
            plt.scatter(x=[point[0]],y=[point[1]],color=options.special_color)

    if labels:
        plt.legend()

    final_time = options.end_time if last_frame else 0

    plt.show()
    # plt.show(block=False)
    # plt.pause(options.frame_time + final_time)
    # plt.close()


if __name__ == "__main__":
    # Options
    np.random.seed(20)
    bounds = (1,1)
    N = 50

    # Generate points    
    p = generate_points(N, bounds)
    
    triangles = triangulate(p)

    options = PlotOptions(title=f'N={N}', bounds=bounds)
    plot_configuration(options=options,points=p, triangles=triangles,last_frame=True)