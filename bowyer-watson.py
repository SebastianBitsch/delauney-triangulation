from plotting import PlotOptions

from objects.Delauney import generate_points, Delauney
from plotting import plot_configuration

if __name__ == "__main__":

    N = [5, 10,50, 100, 250]
    
    for n in N:
        p = generate_points(n, scale = (1,1))

        plot_options = PlotOptions(title=f'N={n}', bounds=(1,1))
        d = Delauney(p, plot_options=plot_options)
        
        plot_configuration(options=plot_options, points=d.get_points(), triangles=d.get_triangles(), edges=d.get_hull(), last_frame=True)