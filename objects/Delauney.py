# Import packages
from copy import copy
import random

# Import objects
from objects.Point import Point
from objects.Edge import Edge
from objects.Triangle import Triangle
from plotting import PlotOptions, plot_configuration


def generate_points(N: int, scale:tuple = (1,1)) -> list:
    """Generate N 2D points uniformly and scale them to a given size."""
    return [(random.random() * scale[0], random.random() * scale[1]) for _ in range(N)]


class Delauney(object):
    """
    An object for computing the Dealuney triangulation using the Bowyer-Watson algorithm. 
    See: https://en.wikipedia.org/wiki/Bowyer-Watson_algorithm for further details.
    """

    def __init__(self, points: list[tuple], plot_options:PlotOptions = None) -> None:
        """
        Create a new Delauney triangulation object that produces a triangulation given a list of 2D points.
        
        Optionally a PlotOptions-object can be provided to plot the process of triangulating.
        """

        self.points = [Point(x,y) for (x,y) in points]
        self.triangulation = self.__triangulate(self.points, plot_options)
        self.voronoi = self.__calculate_vornoi()
    

    def get_points(self) -> list[Point]:
        return self.points

    def get_hull(self) -> list[Edge]:
        return self.hull

    def get_triangles(self) -> list[Triangle]:
        return self.triangulation

    def get_voronoi(self) -> list[Edge]:
        return self.voronoi

    def collinear(self, A: Point, B: Point, C: Point) -> bool:
        """
        Check if three points are colinear, aka do they lie in a straight line.
        Source: https://math.stackexchange.com/a/405981
        """
        return round((B.y - A.y) * (C.x - B.x),4) == round((C.y - B.y) * (B.x - A.x),4)

    
    def __triangulate(self, points: list[Point], plot_options:PlotOptions = None) -> list[Triangle]:
        """
        Computes the Delauney triangulation for a set of points.
        Source: https://en.wikipedia.org/wiki/Bowyer-Watson_algorithm
        """

        super_triangle = self.__generate_super_triangle()
        triangulation = set([super_triangle])
        remaining_points = copy(points)
        
        for p in points:
            remaining_points.remove(p)
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

            if plot_options:
                plot_configuration(options=plot_options, points=remaining_points, triangles=triangulation, special_points = [p], last_frame=False)

        # Remove all edges containing points from the super triangle
        tris = set(triangulation)
        hull = []
        for tri in triangulation:
            for p in super_triangle.points:
                if tri.has_point(p) and tri in tris:
                    
                    # Create the convex hull of the triangulation
                    points = tri.points
                    i = points.index(p)
                    ps = points[:i] + points[i+1:]
                    hull.append(Edge(*ps))

                    # Remove triangle from triangulation if it includes a vertex from the super tri
                    tris.remove(tri)

        # Remove the last of the edges in the convex hull. i.e. the edges in tris where two of the verts were in the supertriangle
        h = set(hull)
        for e in hull:
            if e.p1 in super_triangle.points or e.p2 in super_triangle.points:
                h.remove(e)

        self.hull = h
        self.tris = tris

        # Return final triangulation
        return tris

    
    def __calculate_vornoi(self) -> list[Triangle]:
        """ 
        A not very efficent implementation of getting the voronoi diagram from the delauney triangulation.
        Utilizes the fact that the edges in the vornoi will be edges between circum-circle-centers of
        neighbouring triangles in the delauney triangulation.
        """
        voronoi = []
        for tri in self.triangulation:
            for edge in tri:
                

                for t in self.triangulation:
                    if edge in t:
                        voronoi.append(Edge(tri.circum_circle.center, t.circum_circle.center))

        return voronoi


    def __generate_super_triangle(self) -> Triangle:
        """Generates a right-angled triangle at (0,0) that exactly encompasses the points"""
        x_coords = [p.x for p in self.points]
        y_coords = [p.y for p in self.points]
        return Triangle([Point(0,0), Point(max(x_coords) * 2, 0), Point(0, max(y_coords) * 2)])
