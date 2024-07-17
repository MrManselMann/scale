import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
show_graph = True
def f(coordinate):
    x = [81.41286307053942, 75.99221789883268, 192.96659707724424, 14, 0, 38.83606557377049, 78.9979381443299, 35.19230769230769, 17.058823529411764, 27.772727272727273, 25.771270036991368, 187.65454545454546, 179.02325581395348, 169.10679611650485, 116.56, 79.68, 15.27, 14.37, 175.0, 18.33, 78.38, 169.73, 14.45, 33.0, 200, 189.94]
    y = [2.38824, 2.220055, 6.715281, 0, 0, 1.44844, 2.361151, 1.41316, 0.917123, 1.24341, 1.21254, 5.94586762272919, 4.960401, 4.164532, 2.958604, 2.325877, 0.925942, 0.914918, 4.93615, 1.08908, 2.312649, 4.281377, 1.03, 1.55205, 6.713076, 4.462156]
    
    # Linear interpolation
    interp_func = interp1d(x, y, kind='linear')
    plt.plot(x, y, 'o', label='Data points')
    
    # Plotting the interpolated value at the given coordinate
    plt.plot(coordinate, interp_func(coordinate), 'ro', label='Interpolated point at {}'.format(coordinate))
    plt.legend()
    if show_graph:
        plt.show()
    return interp_func(coordinate)
f(100)
