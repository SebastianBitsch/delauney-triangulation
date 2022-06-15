from dataclasses import dataclass
import matplotlib.pyplot as plt

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


def plot_configuration(options: PlotOptions, points, inner_edges:list, outer_edges:list, last_frame:bool = False, special_points:list = [], labels:list = []):

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