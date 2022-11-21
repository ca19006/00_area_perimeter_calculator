import math
import pandas


# Function to calculate the area or perimeter of a square, circle, rectangle, parallelogram and triangle

# This function is for asking if the user wants to calculate a shape
def string_check(choice, options):
    for var_list in options:
        if choice in var_list:
            chosen = var_list[0].title()
            is_valid = "yes"
            break
        else:
            is_valid = "no"
    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"


# This function is for calculating the area and perimeter of square
def square_calc():
    valid = False
    while valid is False:
        try:
            # Ask the user for 1 side of their square
            side = float(input("What is the length of one side in cm?: "))
            # Calculations
            area = side * side
            perimeter = side * 4
            # Inserting data into lists for history
            history_shape.insert(0, chosen_shape)
            history_length.insert(0, side)
            history_width.insert(0, side)
            history_area.insert(0, area)
            history_perimeter.insert(0, perimeter)
            dataframe = pandas.DataFrame(sr_shape_data)
            print(dataframe)
            return side
        except ValueError:
            # Prints message on error
            print("Please enter a number")


# This function is for calculating the area and perimeter of square
def circle_calc():
    valid = False
    while valid is False:
        try:
            # Question for the radius
            radius = float(input("Whats the radius of your circle in cm?: "))
            # Calculations
            circumference = 2 * math.pi * radius
            c_area = math.pi * radius ** 2
            # Inserting data into lists for history
            history_circle.insert(0, chosen_shape)
            history_radius.insert(0, radius)
            history_circle_area.insert(0, c_area)
            history_circumference.insert(0, circumference)
            dataframe = pandas.DataFrame(c_shape_data)
            print(dataframe)
            return c_area and circumference
        except ValueError:
            # Prints message on error
            print("Please enter a number")


# This function is for calculating the area and perimeter of square
def rectangle_calc():
    valid = False
    while valid is False:
        try:
            # Questions for dimensions of the rectangle
            small = float(input("What is the length of the small side in cm?: "))
            large = float(input("What is the length of the large side in cm?: "))
            # Calculations
            r_area = small * large
            r_perimeter = (small * 2) + (large * 2)
            # Inserting data into lists
            history_shape.insert(0, chosen_shape)
            history_length.insert(0, small)
            history_width.insert(0, large)
            history_area.insert(0, r_area)
            history_perimeter.insert(0, r_perimeter)
            dataframe = pandas.DataFrame(sr_shape_data)
            print(dataframe)
            return r_area and r_perimeter
        except ValueError:
            # Error message for not entering a number
            print("Please enter a number")


# This function is for calculating the area and perimeter of square
def parallelogram_calc():
    valid = False
    while valid is False:
        try:
            # Questions for the dimensions of the shape
            side = float(input("What is the length of the side?: "))
            base = float(input("What is the length of your base in cm?: "))
            height = float(input("What is the height in cm?: "))
            # Calculations
            p_area = base * height
            p_perimeter = 2 * (base + side)
            # Adding the data to lists for the history
            history_parallelogram.insert(0, chosen_shape)
            history_base.insert(0, base)
            history_height.insert(0, height)
            history_parallelogram_area.insert(0, p_area)
            history_parallelogram_side.insert(0, side)
            history_parallelogram_perimeter.insert(0, p_perimeter)
            dataframe = pandas.DataFrame(p_shape_data)
            print(dataframe)
            return p_area and p_perimeter
        except ValueError:
            # Error message to say what the user had done wrong
            print("Please enter a number")


# This function is for calculating the area and perimeter of square
def triangle_calc():
    valid = False
    while valid is False:
        try:
            # This section is for the questions
            two_sides = input("Are you given 2 sides?: ").lower()
            if two_sides == "yes":
                third_side = input("Do you need a 3rd side?: ").lower()
                if third_side == "yes":
                    question3 = input("Are you given the hypotenuse?: ").lower()
                    #
                    # This section uses Pythagoras theorem as there are 2 sides and the user needs the 3rd side
                    if question3 == "yes":
                        hypotenuse = float(input("What is the length of the hypotenuse in cm?: "))
                        opposite = float(input("What is the length of the opposite in cm?: "))
                        _adjacent = (hypotenuse ** 2) - (opposite ** 2)
                        adjacent = math.sqrt(_adjacent)
                        t_area = (0.5 * opposite) * adjacent
                        t_perimeter = hypotenuse + adjacent + opposite
                        history_triangle.insert(0, chosen_shape)
                        history_hypotenuse.insert(0, hypotenuse)
                        history_adjacent.insert(0, adjacent)
                        history_opposite.insert(0, opposite)
                        history_triangle_area.insert(0, t_area)
                        history_triangle_perimeter.insert(0, t_perimeter)
                        dataframe = pandas.DataFrame(t_shape_data)
                        print(dataframe)
                        print()
                    elif question3 == "no":
                        opposite = float(input("What is the length of the opposite in cm?: "))
                        adjacent = float(input("What is the length of the adjacent in cm?: "))
                        _hypotenuse = (opposite ** 2) + (adjacent ** 2)
                        hypotenuse = math.sqrt(_hypotenuse)
                        t_area = (0.5 * opposite) * adjacent
                        t_perimeter = hypotenuse + adjacent + opposite
                        history_triangle.insert(0, chosen_shape)
                        history_hypotenuse.insert(0, hypotenuse)
                        history_adjacent.insert(0, adjacent)
                        history_opposite.insert(0, opposite)
                        history_triangle_area.insert(0, t_area)
                        history_triangle_perimeter.insert(0, t_perimeter)
                        dataframe = pandas.DataFrame(t_shape_data)
                        print(dataframe)
                        print()
                    else:
                        print("Please enter yes or no")
                else:
                    print()
            # This Section is the SOH CAH TOA section of the triangle code
            elif two_sides == "no":
                print("You should have 1 side and 1 angle")
                sct = input("Do you need to use SOH / CAH / TOA?: ").lower()
                if sct == "soh":
                    angle = float(input("What is the angle in degrees?: "))
                    opposite = float(input("What is the length of the opposite in cm?: "))
                    hypotenuse = opposite / math.sin(math.radians(angle))
                    _adjacent = (hypotenuse ** 2) - (opposite ** 2)
                    adjacent = math.sqrt(_adjacent)
                    t_area = (0.5 * opposite) * adjacent
                    t_perimeter = hypotenuse + adjacent + opposite
                    history_triangle.insert(0, chosen_shape)
                    history_hypotenuse.insert(0, hypotenuse)
                    history_adjacent.insert(0, adjacent)
                    history_opposite.insert(0, opposite)
                    history_triangle_area.insert(0, t_area)
                    history_triangle_perimeter.insert(0, t_perimeter)
                    dataframe = pandas.DataFrame(t_shape_data)
                    print(dataframe)
                    return adjacent
                elif sct == "cah":
                    angle = float(input("What is the angle in degrees?: "))
                    adjacent = float(input("What is the length of the adjacent in cm?: "))
                    hypotenuse = adjacent / math.cos(math.radians(angle))
                    _opposite = (hypotenuse ** 2) - (adjacent ** 2)
                    opposite = math.sqrt(_opposite)
                    t_area = (0.5 * opposite) * adjacent
                    t_perimeter = hypotenuse + adjacent + opposite
                    history_triangle.insert(0, chosen_shape)
                    history_hypotenuse.insert(0, hypotenuse)
                    history_adjacent.insert(0, adjacent)
                    history_opposite.insert(0, opposite)
                    history_triangle_area.insert(0, t_area)
                    history_triangle_perimeter.insert(0, t_perimeter)
                    dataframe = pandas.DataFrame(t_shape_data)
                    print(dataframe)
                    return opposite
                elif sct == "toa":
                    angle = float(input("What is the angle in degrees?: "))
                    opposite = float(input("What is the length of the opposite in cm?: "))
                    adjacent = opposite / math.tan(math.radians(angle))
                    _hypotenuse = (opposite ** 2) + (adjacent ** 2)
                    hypotenuse = math.sqrt(_hypotenuse)
                    t_area = (0.5 * opposite) * adjacent
                    t_perimeter = hypotenuse + adjacent + opposite
                    history_triangle.insert(0, chosen_shape)
                    history_hypotenuse.insert(0, hypotenuse)
                    history_adjacent.insert(0, adjacent)
                    history_opposite.insert(0, opposite)
                    history_triangle_area.insert(0, t_area)
                    history_triangle_perimeter.insert(0, t_perimeter)
                    dataframe = pandas.DataFrame(t_shape_data)
                    print(dataframe)
                    return hypotenuse
                else:
                    print("Please enter SOH CAH or TOA")
            else:
                print("Please enter yes or no")
        except ValueError:
            print("Please enter a number")


# Initial variables
number_regex = "^[1-9]"
shape_list = [
    ["square", "s"],
    ["circle", "c"],
    ["rectangle", "r"],
    ["parallelogram", "p"],
    ["triangle", "t"]
]
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

# Lists for the history of calculations
history_shape = []
history_length = []
history_width = []
history_area = []
history_base = []
history_height = []
history_radius = []
history_perimeter = []
history_circle_area = []
history_circumference = []
history_circle = []
history_parallelogram = []
history_parallelogram_area = []
history_parallelogram_perimeter = []
history_parallelogram_side = []
history_hypotenuse = []
history_adjacent = []
history_opposite = []
history_hypotenuse_angle = []
history_adjacent_angle = []
history_opposite_angle = []
history_triangle_area = []
history_triangle_perimeter = []
history_triangle = []

# Dictionaries for the history
sr_shape_data = {
    'Shape': history_shape,
    'Length': history_length,
    'Width': history_width,
    'Area': history_area,
    'perimeter': history_perimeter
}

c_shape_data = {
    'Shape': history_circle,
    'Radius': history_radius,
    'Area': history_circle_area,
    'Circumference': history_circumference
}

p_shape_data = {
    'Shape': history_parallelogram,
    'Side': history_parallelogram_side,
    'Base': history_base,
    'Height': history_height,
    'Area': history_parallelogram_area,
    'perimeter': history_parallelogram_perimeter
}

t_shape_data = {
    'Shape': history_triangle,
    'Hypotenuse': history_hypotenuse,
    'Adjacent': history_adjacent,
    'Opposite': history_opposite,
    'Perimeter': history_triangle_perimeter,
    'Area': history_triangle_area
}

t_angle_data = {
    'Hypotenuse Angle': history_hypotenuse_angle,
    'Adjacent Angle': history_adjacent_angle,
    'Opposite Angle': history_opposite_angle,
}

# While loop to ask if they want to calculate a shape
shape_valid = "invalid choice"
while shape_valid == "invalid choice":
    question = input("Do you want to calculate a shape?: ").lower()
    shape_valid = string_check(question, yes_no)
    print("You said:", shape_valid)
    print()

# While loop to ask what shape they want to calculate and if they want to exit the program
if shape_valid == "Yes":
    shape_choice = ""
    while shape_choice != shape_list:
        shape_choice = input("What shape would you like to calculate? There is: \n"
                             "Square \n"
                             "Triangle \n"
                             "Circle \n"
                             "Rectangle \n"
                             "Parallelogram \n"
                             "Type Exit to stop \n"
                             "Type Here: ").lower()
        print()
        shape_choice = shape_choice.strip()
        # If, elif and else statements to call the functions based on the users response
        if shape_choice == "exit":
            break
        chosen_shape = string_check(shape_choice, shape_list)
        print("Shape selected: ", chosen_shape)
        if shape_choice == "square" or shape_choice == "s":
            square = square_calc()
        elif shape_choice == "rectangle" or shape_choice == "r":
            rectangle = rectangle_calc()
        elif shape_choice == "circle" or shape_choice == "c":
            circle = circle_calc()
        elif shape_choice == "parallelogram" or shape_choice == "p":
            parallelogram = parallelogram_calc()
        elif shape_choice == "triangle" or shape_choice == "t":
            triangle = triangle_calc()
        else:
            print("Please enter a valid shape ")
