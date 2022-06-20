from copy import copy
import numpy as np

from util import circle_center, angle, sort_points, diff, generate_points
from plotting import PlotOptions, plot_configuration
from Point import Point


def triangulate(x, options):
    pass


if __name__ == "__main__":
    # Options
    np.random.seed(20)
    bounds = (1,1)
    N = 20

    # Generate points
    
    x = generate_points(N, bounds).tolist()
    options = PlotOptions(title=f'N={N}', bounds=bounds)
        
    triangles = triangulate(x, options)