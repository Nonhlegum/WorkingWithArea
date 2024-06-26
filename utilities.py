# Loveness Gumede & Thabang Mahapa

import math


def calculate_circle_area(radius):
    """
    Takes  the radius as a  parameter, calculates and returns the area() of the circle.

    param:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    # The formula for area of a circle: Area = π * r^2
    return math.pi * radius ** 2


def calculate_sphere_volume(radius):
    """
    Takes one parameter which is the radius, calculates and returns the sphere volume

    param:
        radius (float): The radius of the sphere.

    Returns:
        float: The volume of the sphere.
    """
    # The formula for volume of a sphere: volume = (4/3) * π * r^3
    return (4 / 3) * math.pi * radius ** 3


def calculate_bmi():
    """
    Prompts the user to enter the weight in kilograms and the height in meters, calculates and returns the body mass
    index(BMI).

    Returns:
        float: The body mass index (BMI).
    """
    # weight and height inputs from user.
    weight_kg = float(input("Enter the weight in kilograms: "))
    height_m = float(input("Enter the height in meters: "))
    # The formula for BMI: BMI = weight / height^2
    return weight_kg / (height_m ** 2)


def calculate_hypotenuse():
    """
    Prompts the user to enter the lengths of side A and side B of a right triangle. The function will calculate and
    return the length of a right triangles hypotenuse

    Returns:

        float: The length of the hypotenuse.
    """
    # Input length of side A and length of side B
    side_a_cm = float(input("Enter the length of side A in cm: "))
    side_b_cm = float(input("Enter the length of side B in cm: "))
    # Using the hypot() function from math module to calculate the hypotenuse
    return math.hypot(side_a_cm, side_b_cm)
