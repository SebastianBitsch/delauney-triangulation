from dataclasses import dataclass
import matplotlib.pyplot as plt

@dataclass
class PlotOptions:
    fig_size: tuple = (8,8)
    bounds: tuple = (2,2)
    frame_time: float = 0.05
    start_time: float = 1
    end_time: float = 4

    point_color: str = 'black'
    inner_edge_color: str = 'lightgrey'
    outer_edge_color: str = 'black'


def plot_configuration(options: PlotOptions, points, inner_edges:list, outer_edges:list, last_frame:bool = False, special_points:list = []):

    plt.figure(figsize=options.fig_size)
    plt.axes(xlim=(0, options.bounds[0]), ylim=(0, options.bounds[0]))
    
    if 0 < len(points):
        plt.scatter(x=points[:,0],y=points[:,1], color=options.point_color, marker='.')
    
    for point, label in special_points:
        plt.scatter(x=[point[0]],y=[point[1]],label=label)
    
    for edge in inner_edges:
        plt.plot([edge[0][0],edge[1][0]],[edge[0][1],edge[1][1]], options.inner_edge_color, '--')
    
    for edge in outer_edges:
        plt.plot([edge[0][0],edge[1][0]],[edge[0][1],edge[1][1]], options.outer_edge_color, ':')
    
    if special_points:
        plt.legend()

    final_time = options.end_time if last_frame else 0

    plt.show(block=False)
    plt.pause(options.frame_time + final_time)
    plt.close()