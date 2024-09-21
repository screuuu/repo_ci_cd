import math
from typing import List, Tuple
import matplotlib.pyplot as plt  # Third-party library


class Circle:
    """Class representing a circle."""

    def __init__(self, radius: float):
        """Initialize the Circle with a radius."""
        self.radius = radius

    def area(self) -> float:
        """Calculate the area of the circle."""
        return math.pi * self.radius ** 2

    def circumference(self) -> float:
        """Calculate the circumference of the circle."""
        return 2 * math.pi * self.radius

    def __str__(self) -> str:
        """Return a string representation of the circle."""
        return f"Circle with radius {self.radius:.2f}"


def filter_positive_numbers(numbers: List[int]) -> List[int]:
    """Filter and return positive numbers from a list."""
    return [num for num in numbers if num > 0]


def calculate_circle_properties(radii: List[float]) -> List[Tuple[float, float, float]]:
    """Calculate the area and circumference for a list of circle radii.

    Args:
        radii: A list of circle radii.

    Returns:
        A list of tuples containing radius, area, and circumference.
    """
    properties = []
    for radius in radii:
        circle = Circle(radius)
        properties.append(
            (circle.radius, circle.area(), circle.circumference()))
    return properties


def plot_circle_areas(radii: List[float], areas: List[float]) -> None:
    """Plot a graph of Circle Areas vs. Radii using matplotlib."""
    plt.figure(figsize=(8, 6))
    plt.plot(radii, areas, marker='o', linestyle='-', color='b', label='Area')
    plt.title("Circle Areas vs. Radii")
    plt.xlabel("Radius")
    plt.ylabel("Area")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # Example usage
    radii = [1.0, 2.5, 4.0]
    circle_properties = calculate_circle_properties(radii)

    print("Circle Properties:")
    areas = []
    for radius, area, circumference in circle_properties:
        areas.append(area)
        print(
            f"Radius: {radius:.2f}, Area: {area:.2f}, Circumference: {circumference:.2f}")

    # Plot circle areas vs radii
    plot_circle_areas(radii, areas)

    # Filtering example
    numbers = [-10, 15, 0, -3, 9]
    positive_numbers = filter_positive_numbers(numbers)
    print(f"Positive numbers: {positive_numbers}")
