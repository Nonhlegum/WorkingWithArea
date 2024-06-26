# Loveness Gumede & Thabang Mahapa

import utilities


def main():
    """
    This main function prompts the user for inputs, calls utility functions, and displays the results.
    """
    # Prompt the user to enter the radius of a circle, call function calculate_circle_area and display the result.
    radius_circle = float(input("Enter the radius of a circle in cm: "))
    circle_area = utilities.calculate_circle_area(radius_circle)
    print(f"The area of the circle is: {circle_area}")

    # Prompt the user to enter the radius of a sphere, call function calculate_sphere_volume() and display the result.
    radius_sphere = float(input("Enter the radius of a sphere in cm: "))
    sphere_volume = utilities.calculate_sphere_volume(radius_sphere)
    print(f"The volume of the sphere is: {sphere_volume}")

    # Call function calculate_BMI() and display the result based on user input.
    bmi = utilities.calculate_bmi()
    print(f"The Body Mass Index is: {bmi}")

    # Call function calculate_hypotenuse() and display the result based on user input for length of side A and B.
    hypotenuse_length = utilities.calculate_hypotenuse()
    print(f"The hypotenuse length of the right triangle is: {hypotenuse_length}")


if __name__ == "__main__":
    main()
