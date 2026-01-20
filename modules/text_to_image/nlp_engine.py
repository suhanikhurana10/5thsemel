import spacy
import os
import re
from visuals.geometry import generate_triangle, generate_circle, generate_rectangle
from visuals.physics import draw_force_diagram, draw_motion_vector
from visuals.graphs import draw_linear_graph, draw_parabola, draw_hyperbola, draw_bar_graph, plot_points
from visuals.derivative import draw_derivative


nlp = spacy.load("en_core_web_sm")

# ----------------- Utility Functions -----------------
def extract_numbers(text):
    """
    Extract all numbers from text safely, including integers and floats.
    Ignores parentheses and commas.
    Returns a list of numbers as floats.
    """
    numbers = re.findall(r"[-+]?\d*\.\d+|\d+", text)
    numbers = [float(num) for num in numbers]
    return numbers

def detect_shape(text):
    """
    Detect the type of visual: geometry, physics, or graph
    """
    text = text.lower()

    # Geometry
    if "triangle" in text:
        return "triangle"
    if "circle" in text or "radius" in text:
        return "circle"
    if "rectangle" in text:
        return "rectangle"

    # Physics
    if "force" in text or "newton" in text or "n " in text:
        return "force"
    if "motion" in text or "velocity" in text:
        return "motion"

    # Graphs
    if "graph" in text or "plot" in text or "bar" in text or "points" in text or "parabola" in text or "hyperbola" in text:
        return "graph"
    if "derivative" in text:
        return "derivative"

    


    return None

# ----------------- Main Conversion Function -----------------
def text_to_image(text, output_folder="generated_images"):
    """
    Convert input text to a visual and save as an image
    """
    os.makedirs(output_folder, exist_ok=True)
    shape = detect_shape(text)
    numbers = extract_numbers(text)

    if shape is None:
        return None

    # ----------------- Geometry -----------------
    if shape == "triangle":
        output_path = os.path.join(output_folder, "triangle.png")
        return generate_triangle(output_path=output_path)

    elif shape == "circle":
        radius = numbers[0] if numbers else 5
        output_path = os.path.join(output_folder, "circle.png")
        return generate_circle(radius=radius, output_path=output_path)

    elif shape == "rectangle":
        length = numbers[0] if len(numbers) > 0 else 6
        width = numbers[1] if len(numbers) > 1 else 4
        output_path = os.path.join(output_folder, "rectangle.png")
        return generate_rectangle(length=length, width=width, output_path=output_path)

    # ----------------- Physics -----------------
    elif shape == "force":
        value = numbers[0] if numbers else 10  # default 10 N

        # Detect direction in text
        direction = "up"
        if "left" in text.lower():
            direction = "left"
        elif "right" in text.lower():
            direction = "right"
        elif "down" in text.lower():
            direction = "down"

        output_path = os.path.join(output_folder, "force.png")
        return draw_force_diagram(force_value=value, direction=direction, output_path=output_path)

    elif shape == "motion":
        # Motion arrow direction
        direction = "left" if "left" in text.lower() else "right"
        output_path = os.path.join(output_folder, "motion.png")
        return draw_motion_vector(direction=direction, output_path=output_path)
    elif shape == "derivative":
        try:
            # Extract expression after "of"
            expr = text.lower().split("of")[1].strip()
            output_path = os.path.join(output_folder, "derivative.png")
            return draw_derivative(expr, output_path)
        except:
            return None


    # ----------------- Graphs -----------------
    elif shape == "graph":
        text_lower = text.lower()

        # ---------- Parabola ----------
        if "parabola" in text_lower:
            points = []
            # take numbers in pairs as (x,y)
            for i in range(0, len(numbers), 2):
                if i+1 < len(numbers):
                    points.append((numbers[i], numbers[i+1]))
            output_path = os.path.join(output_folder, "parabola.png")
            return draw_parabola(points=points, output_path=output_path)

        # ---------- Hyperbola ----------
        elif "hyperbola" in text_lower:
            points = []
            for i in range(0, len(numbers), 2):
                if i+1 < len(numbers):
                    points.append((numbers[i], numbers[i+1]))
            output_path = os.path.join(output_folder, "hyperbola.png")
            return draw_hyperbola(points=points, output_path=output_path)

        # ---------- Points ----------
        elif "point" in text_lower or "points" in text_lower:
            output_path = os.path.join(output_folder, "points.png")
            return plot_points(output_path=output_path)

        # ---------- Bar Graph ----------
        elif "bar" in text_lower:
            output_path = os.path.join(output_folder, "bar_graph.png")
            data = numbers if numbers else [5, 3, 7, 2]
            return draw_bar_graph(data=data, output_path=output_path)

        # ---------- Linear Graph ----------
        else:
            output_path = os.path.join(output_folder, "linear_graph.png")
            return draw_linear_graph(output_path=output_path)

    else:
        return None
