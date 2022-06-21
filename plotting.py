from dataclasses import dataclass
import matplotlib.pyplot as plt
import numpy as np
from Point import Point
from Triangle import Triangle
from Edge import Edge

@dataclass
class PlotOptions:
    title: str
    fig_size: tuple = (7,7)
    bounds: tuple = (2,2)
    frame_time: float = 0.1
    start_time: float = 2
    end_time: float = 2

    point_color: str = 'black'
    special_color: str = 'orange'
    inner_edge_color: str = 'lightgrey'
    outer_edge_color: str = 'black'
    triangle_color: str = 'orange'


def plot_configuration(options: PlotOptions, points:list[Point] = [], edges:list[Edge] = [], triangles:list[Triangle] = [], last_frame:bool = False, special_points:list = [], labels:list = []):

    plt.figure(figsize=options.fig_size)
    plt.axes(xlim=(0, options.bounds[0]), ylim=(0, options.bounds[1]))
    plt.title(options.title, loc='left')
    plt.title("Triangulation", loc='center')
    plt.xticks([])
    plt.yticks([])


    points = np.array([p.arr for p in points])
    if 0 < len(points):
        plt.scatter(x=points[:,0],y=points[:,1], color=options.point_color, marker='.', zorder=2)
    
    for point in special_points:
        if labels:
            plt.scatter(x=[point[0]],y=[point[1]],labels=labels,color=options.special_color, zorder=3)
        else:
            plt.scatter(x=[point[0]],y=[point[1]],color=options.special_color)

    if labels:
        plt.legend()

    for tri in triangles:
        t = plt.Polygon(tri.get_points(), edgecolor=options.triangle_color, fill=False, zorder=1)
        plt.gca().add_patch(t)

    for edge in edges:
        plt.plot([edge.p1.x, edge.p2.x],[edge.p1.y,edge.p2.y], options.inner_edge_color, zorder=1)
    
    final_time = options.end_time if last_frame else 0

    plt.show(block=False)
    plt.pause(options.frame_time + final_time)
    plt.close()


def plot_shull(options: PlotOptions, points, inner_edges:list, outer_edges:list, last_frame:bool = False, special_points:list = [], labels:list = []):

    plt.figure(figsize=options.fig_size)
    plt.axes(xlim=(0, options.bounds[0]), ylim=(0, options.bounds[0]))
    plt.title(options.title, loc='left')
    plt.title("Triangulation", loc='center')
    plt.xticks([])
    plt.yticks([])

    if 0 < len(points):
        plt.scatter(x=points[:,0],y=points[:,1], color=options.point_color, marker='.')
    
    for point in special_points:
        if labels:
            plt.scatter(x=[point[0]],y=[point[1]],labels=labels,color=options.special_color)
        else:
            plt.scatter(x=[point[0]],y=[point[1]],color=options.special_color)

    for edge in inner_edges:
        plt.plot([edge[0][0],edge[1][0]],[edge[0][1],edge[1][1]], options.inner_edge_color)
    
    for edge in outer_edges:
        plt.plot([edge[0][0],edge[1][0]],[edge[0][1],edge[1][1]], options.outer_edge_color)
    
    if labels:
        plt.legend()

    final_time = options.end_time if last_frame else 0

    plt.show(block=False)
    plt.pause(options.frame_time + final_time)
    plt.close()