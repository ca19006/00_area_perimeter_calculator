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
                    if question3 == "yes":
                        hypotenuse = int(input("What is the length of the hypotenuse in cm?: "))
                        opposite = int(input("What is the length of the opposite in cm?: "))
                        adjacent = (hypotenuse**2) - (opposite**2)
                        answer = math.sqrt(adjacent)
                        print("The length of the adjacent is {} cm".format(answer))
                    else:
                        opposite = int(input("What is the length of the opposite in cm?: "))
                        adjacent = int(input("What is the length of the adjacent in cm?: "))
                        hypotenuse = (opposite**2) + (adjacent**2)
                        answer = math.sqrt(hypotenuse)
                        print("The length of the hypotenuse is {} cm".format(answer))
                    #
            # This Section is the SOH CAH TOA section of the triangle code
            elif two_sides == "no":
                print("You should have 1 side and 1 angle")
                sct = input("Do you need to use SOH / CAH / TOA?: ").lower()
                if sct == "soh":
                    angle = int(input("What is the angle in degrees?: "))
                    side = int(input("What is the length of the side in cm?: "))
                    adjacent = side / math.sin(math.radians(angle))
                    print("The length of the adjacent is {} cm".format(adjacent))
                    return adjacent
                elif sct == "cah":
                    angle = int(input("What is the angle in degrees?: "))
                    side = int(input("What is the length of the side in cm?: "))
                    opposite = side / math.sin(math.radians(angle))
                    print("The length of the opposite is {} cm".format(opposite))
                    return opposite
                elif sct == "toa":
                    angle = int(input("What is the angle in degrees?: "))
                    side = int(input("What is the length of the side in cm?: "))
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

shape_valid = "invalid choice"
while shape_valid == "invalid choice":
    question = input("Do you want to calculate a shape?: ").lower()
    shape_valid = string_check(question, yes_no)
    print("You said:", shape_valid)

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
