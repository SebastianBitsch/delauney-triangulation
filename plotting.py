from dataclasses import dataclass
import matplotlib.pyplot as plt
import numpy as np
from objects.Point import Point
from objects.Triangle import Triangle
from objects.Edge import Edge

@dataclass
class PlotOptions:
    title: str
    fig_size: tuple = (7,7)
    bounds: tuple = (1,1)
    frame_time: float = 0.2
    start_time: float = 0
    end_time: float = 3

    point_color: str = 'black'
    special_color: str = 'blue'
    inner_edge_color: str = 'lightgrey'
    outer_edge_color: str = 'black'
    triangle_color: str = 'orange'
    circle_color: str = 'lightgrey'


def plot_configuration(
    options: PlotOptions, 
    points:list[Point] = [], 
    edges:list[Edge] = [], 
    triangles:list[Triangle] = [],
    special_points:list = [], 
    labels:list = [],
    last_frame:bool = False,
    first_frame:bool = False):
    """
    Function for plotting all elements in a configuration inclduing points, edges and triangles.
    """

    plt.figure(figsize=options.fig_size)
    # plt.axes(xlim=(0, options.bounds[0]), ylim=(0, options.bounds[1]))
    plt.axes(xlim=(0, options.bounds[0]*2), ylim=(0, options.bounds[1]*2))
    plt.title(options.title, loc='left')
    plt.title("Bowyer-Watson Triangulation", loc='center')
    plt.xticks([])
    plt.yticks([])

    # Plot bounds
    b = plt.Rectangle((0,0),options.bounds[0],options.bounds[1], color=options.circle_color, fill=False, zorder=0)
    plt.gca().add_patch(b)

    # Plot all regular points
    points = np.array([p.arr for p in points])
    if 0 < len(points):
        plt.scatter(x=points[:,0],y=points[:,1], color=options.point_color, marker='.', zorder=2)
    
    # Plot special points, e.g. the current point being plotted
    special_points = np.array([p.arr for p in special_points])
    for point in special_points:
        plt.scatter(x=[point[0]],y=[point[1]],label=labels,color=options.special_color, zorder=5)

    # Plot a legend if any labels are providede
    if labels:
        plt.legend(loc='upper left')

    # Plot the triangles and their corresponding circum circles
    for tri in triangles:
        t = plt.Polygon(tri.get_points(), edgecolor=options.triangle_color, fill=False, zorder=1)
        plt.gca().add_patch(t)

        if not last_frame:
            c = plt.Circle(tri.circum_circle.center.arr, tri.circum_circle.radius, color=options.circle_color, fill=False, zorder=0)
            plt.gca().add_patch(c)

    # Plot the centers of the circum circles
    if not last_frame:
        circle_centers = np.array([t.circum_circle.center.arr for t in triangles])
        if 0 < len(circle_centers):
            plt.scatter(x=circle_centers[:,0],y=circle_centers[:,1], color=options.circle_color, marker='.', zorder=1)
    

    # Plot all edges
    for edge in edges:
        plt.plot([edge.p1.x, edge.p2.x],[edge.p1.y,edge.p2.y], options.outer_edge_color, zorder=1)
    

    extra_end_time = options.end_time if last_frame else 0
    extra_start_time = options.start_time if first_frame else 0

    plt.show(block=False)
    plt.pause(options.frame_time + extra_start_time + extra_end_time)
    plt.close()



# def plot_shull(options: PlotOptions, points, inner_edges:list, outer_edges:list, last_frame:bool = False, special_points:list = [], labels:list = []):

#     plt.figure(figsize=options.fig_size)
#     plt.axes(xlim=(0, options.bounds[0]), ylim=(0, options.bounds[0]))
#     plt.title(options.title, loc='left')
#     plt.title("Triangulation", loc='center')
#     plt.xticks([])
#     plt.yticks([])

#     if 0 < len(points):
#         plt.scatter(x=points[:,0],y=points[:,1], color=options.point_color, marker='.')
    
#     for point in special_points:
#         if labels:
#             plt.scatter(x=[point[0]],y=[point[1]],labels=labels,color=options.special_color)
#         else:
#             plt.scatter(x=[point[0]],y=[point[1]],color=options.special_color)

#     for edge in inner_edges:
#         plt.plot([edge[0][0],edge[1][0]],[edge[0][1],edge[1][1]], options.inner_edge_color)
    
#     for edge in outer_edges:
#         plt.plot([edge[0][0],edge[1][0]],[edge[0][1],edge[1][1]], options.outer_edge_color)
    
#     if labels:
#         plt.legend()

#     final_time = options.end_time if last_frame else 0

#     plt.show(block=False)
#     plt.pause(options.frame_time + final_time)
#     plt.close()