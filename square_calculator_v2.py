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
            print("The area of your square is {} cm".format(area))
            print("The perimeter of your square is {} cm".format(perimeter))
            return area and perimeter
        except ValueError:
            print("Please enter a number")


def circle_calc():
    valid = False
    while valid is False:
        try:
            decimal = int(input("How many decimal places do you want?: "))
            radius = float(input("Whats the radius of your circle in cm?: "))
            circumference = 2 * math.pi * radius
            c_area = math.pi * radius ** 2
            print("The area of your circle is {:.{}f} cm".format(c_area, decimal))
            print("The circumference of your circle is {:.{}f}".format(circumference, decimal))
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
            print("The area of your rectangle is {} cm".format(r_area))
            print("The perimeter of your rectangle is {} cm".format(r_perimeter))
            return r_area and r_perimeter
        except ValueError:
            print("Please enter a number")


def parallelogram_calc():
    valid = False
    while valid is False:
        try:
            side = int(input("What is the length of your side in cm?: "))
            base = int(input("What is the length of your base in cm?: "))
            height = int(input("What is the height in cm?: "))
            p_area = base * height
            p_perimeter = 2 * (base + side)
            print("The area of your parallelogram is {} cm".format(p_area))
            print("The perimeter of your parallelogram is {} cm".format(p_perimeter))
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
