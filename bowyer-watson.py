from plotting import PlotOptions

from objects.Delauney import generate_points, Delauney
from plotting import plot_configuration

if __name__ == "__main__":

    N = [5, 10, 5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,50, 100, 250]
    
    n = 5
    while True:
        p = generate_points(n, scale = (1,1))

        plot_options = PlotOptions(title=f'N={n}', bounds=(1,1))
        d = Delauney(p, plot_options=plot_options)
        
        # plot_configuration(options=plot_options, points=d.get_points(), edges=d.get_hull(), last_frame=True)