import matplotlib.pyplot as plt
import numpy as np

# ---------------- Linear Graph ----------------
def draw_linear_graph(output_path="linear_graph.png"):
    x = np.linspace(-10, 10, 200)
    y = 2 * x + 1  # example linear
    plt.plot(x, y, label="y=2x+1")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Linear Graph")
    plt.legend()
    plt.grid(True)
    plt.savefig(output_path)
    plt.close()
    return output_path

# ---------------- Parabola ----------------
import matplotlib.pyplot as plt
import numpy as np

def draw_parabola(points=None, output_path="parabola.png"):
    """
    Draw a parabola passing through given points.
    points: list of tuples [(x1,y1), (x2,y2), ...]
    If None, plots default y = x^2
    """
    if points is None or len(points) < 2:
        # default parabola
        x = np.linspace(-10, 10, 200)
        y = x**2
    else:
        # Fit a quadratic: y = ax^2 + bx + c
        x_coords = [p[0] for p in points]
        y_coords = [p[1] for p in points]
        coeffs = np.polyfit(x_coords, y_coords, 2)  # returns [a,b,c]
        a, b, c = coeffs
        x = np.linspace(min(x_coords)-1, max(x_coords)+1, 200)
        y = a*x**2 + b*x + c

    plt.plot(x, y, label="Parabola")
    
    if points is not None:
        # Plot points for reference
        px = [p[0] for p in points]
