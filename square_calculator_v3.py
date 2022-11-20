import math
import pandas


# Function to calculate the area or perimeter of a square, circle, rectangle, parallelogram and triangle


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


def square_calc():
    valid = False
    while valid is False:
        try:
            side = float(input("What is the length of one side in cm?: "))
            area = side * side
            perimeter = side * 4
            history_shape.insert(0, chosen_shape)
            history_length.insert(0, side)
            history_width.insert(0, side)
            history_area.insert(0, area)
            history_perimeter.insert(0, perimeter)
            dataframe = pandas.DataFrame(sr_shape_data)
            print(dataframe)
            return side
        except ValueError:
            print("Please enter a number")


def circle_calc():
    valid = False
    while valid is False:
        try:
            radius = float(input("Whats the radius of your circle in cm?: "))
            circumference = 2 * math.pi * radius
            c_area = math.pi * radius ** 2
            history_circle.insert(0, chosen_shape)
            history_radius.insert(0, radius)
            history_circle_area.insert(0, c_area)
            history_circumference.insert(0, circumference)
            dataframe = pandas.DataFrame(c_shape_data)
            print(dataframe)
            return c_area and circumference
        except ValueError:
            print("Please enter a number")


def rectangle_calc():
    valid = False
    while valid is False:
        try:
            small = float(input("What is the length of the small side in cm?: "))
            large = float(input("What is the length of the large side in cm?: "))
            r_area = small * large
            r_perimeter = (small * 2) + (large * 2)
            history_shape.insert(0, chosen_shape)
            history_length.insert(0, small)
            history_width.insert(0, large)
            history_area.insert(0, r_area)
            history_perimeter.insert(0, r_perimeter)
            dataframe = pandas.DataFrame(sr_shape_data)
            print(dataframe)
            return r_area and r_perimeter
        except ValueError:
            print("Please enter a number")


def parallelogram_calc():
    valid = False
    while valid is False:
        try:
            base = float(input("What is the length of your base in cm?: "))
            height = float(input("What is the height in cm?: "))
            p_area = base * height
            p_perimeter = 2 * (base + height)
            history_parallelogram.insert(0, chosen_shape)
            history_base.insert(0, base)
            history_height.insert(0, height)
            history_parallelogram_area.insert(0, p_area)
            history_parallelogram_perimeter.insert(0, p_perimeter)
            dataframe = pandas.DataFrame(p_shape_data)
            print(dataframe)
            return p_area and p_perimeter
        except ValueError:
            print("Please enter a number")


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
                    if question3 == "yes":  # This section is done
                        hypotenuse = float(input("What is the length of the hypotenuse in cm?: "))
                        opposite = float(input("What is the length of the opposite in cm?: "))
                        _adjacent = (hypotenuse ** 2) - (opposite ** 2)
                        adjacent = math.sqrt(_adjacent)
                        print("The adjacent side is {} cm".format(adjacent))
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
                        print("The length of the hypotenuse is {} cm".format(hypotenuse))
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
                elif third_side == "no":
                    inverse = int(input("What sides do you have? \n"
                                        "1. Opposite and Hypotenuse \n"
                                        "2. Adjacent and Hypotenuse \n"
                                        "3. Opposite and Adjacent \n"
                                        "Type Here: "))
                    if inverse == 1:
                        hypotenuse = float(input("What is the length of the hypotenuse in cm?: "))
                        opposite = float(input("What is the length of the opposite in cm?: "))
                        angle = math.degrees(math.asin(opposite / hypotenuse))
                        print("Your missing angle is {} degrees".format(angle))
                        _adjacent = (hypotenuse ** 2) - (opposite ** 2)
                        adjacent = math.sqrt(_adjacent)
                        t_perimeter = hypotenuse + opposite + adjacent
                        t_area = 2 / adjacent * opposite
                        adjacent_angle = math.degrees(math.acos(adjacent / hypotenuse))
                        hypotenuse_angle = math.degrees(math.atan(opposite / adjacent))
                        history_triangle.insert(0, chosen_shape)
                        history_opposite.insert(0, opposite)
                        history_hypotenuse.insert(0, hypotenuse)
                        history_opposite_angle.insert(0, angle)
                        history_adjacent.insert(0, adjacent)
                        history_adjacent_angle.insert(0, adjacent_angle)
                        history_hypotenuse_angle.insert(0, hypotenuse_angle)
                        history_triangle_perimeter.insert(0, t_perimeter)
                        history_triangle_area.insert(0, t_area)
                        dataframe = pandas.DataFrame(t_shape_data)
                        print(dataframe)
                        angle_data_frame = pandas.DataFrame(t_angle_data)
                        print(angle_data_frame)
                    elif inverse == 2:
                        hypotenuse = float(input("What is the length of the hypotenuse in cm?: "))
                        adjacent = float(input("What is the length of the opposite in cm?: "))
                        angle = math.degrees(math.acos(adjacent/hypotenuse))
                        print("Your missing angle is {} degrees".format(angle))
                        opposite = (math.tan(math.radians(angle))) * adjacent
                        print(opposite)
                        print(adjacent)
                        print(hypotenuse)
                        t_perimeter = hypotenuse + opposite + adjacent
                        t_area = 2 / adjacent * opposite
                        opposite_angle = math.degrees(math.asin(opposite / hypotenuse))
                        hypotenuse_angle = math.degrees(math.atan(hypotenuse / adjacent))
                        history_triangle.insert(0, chosen_shape)
                        history_opposite.insert(0, opposite)
                        history_hypotenuse.insert(0, hypotenuse)
                        history_opposite_angle.insert(0, opposite_angle)
                        history_adjacent.insert(0, adjacent)
                        history_adjacent_angle.insert(0, angle)
                        history_hypotenuse_angle.insert(0, hypotenuse_angle)
                        history_triangle_perimeter.insert(0, t_perimeter)
                        history_triangle_area.insert(0, t_area)
                        dataframe = pandas.DataFrame(t_shape_data)
                        print(dataframe)
                        angle_data_frame = pandas.DataFrame(t_angle_data)
                        print(angle_data_frame)
                    elif inverse == 3:
                        adjacent = float(input("What is the length of the adjacent in cm?: "))
                        opposite = float(input("What is the length of the opposite in cm?: "))
                        angle = math.degrees(math.atan(opposite / adjacent))
                        print("Your missing angle is {} degrees".format(angle))
                    else:
                        print("Please enter 1, 2 or 3")
            # This Section is the SOH CAH TOA section of the triangle code
            elif two_sides == "no":
                print("You should have 1 side and 1 angle")
                sct = input("Do you need to use SOH / CAH / TOA?: ").lower()
                if sct == "soh":
                    angle = float(input("What is the angle in degrees?: "))
                    side = float(input("What is the length of the side in cm?: "))
                    adjacent = side / math.sin(math.radians(angle))
                    print("The length of the adjacent is {} cm".format(adjacent))
                    return adjacent
                elif sct == "cah":
                    angle = float(input("What is the angle in degrees?: "))
                    side = float(input("What is the length of the side in cm?: "))
                    opposite = side / math.sin(math.radians(angle))
                    print("The length of the opposite is {} cm".format(opposite))
                    return opposite
                elif sct == "toa":
                    angle = float(input("What is the angle in degrees?: "))
                    side = float(input("What is the length of the side in cm?: "))
                    hypotenuse = side / math.sin(math.radians(angle))
                    print("The length of the hypotenuse {} cm".format(hypotenuse))
                    return hypotenuse

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
history_hypotenuse = []
history_adjacent = []
history_opposite = []
history_hypotenuse_angle = []
history_adjacent_angle = []
history_opposite_angle = []
history_triangle_area = []
history_triangle_perimeter = []
history_triangle = []

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

shape_valid = "invalid choice"
while shape_valid == "invalid choice":
    question = input("Do you want to calculate a shape?: ").lower()
    shape_valid = string_check(question, yes_no)
    print("You said:", shape_valid)
    print()

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
            print()
