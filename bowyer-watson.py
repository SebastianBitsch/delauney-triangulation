from plotting import PlotOptions

from objects.Delauney import generate_points, Delauney
from plotting import plot_configuration
import math

def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang
 
if __name__ == "__main__":
    
    N = [5, 10,50, 100, 250]
    
    for n in N:
        p = generate_points(n, scale = (1,1))
        plot_options = PlotOptions(title=f'N={n}', bounds=(1,1))
        
        # d = Delauney(p,plot_options=plot_options)
        d = Delauney(p)

                
        plot_configuration(options=plot_options, points=d.get_points(), triangles=d.get_triangles(), edges=d.get_hull(), last_frame=True)
        
        # Plot the Voronoi diagram
        # plot_configuration(options=plot_options, edges=d.voronoi, last_frame=True)