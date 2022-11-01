import math

# Function to calculate the area or perimeter of a square, circle, rectangle, parallelogram and triangle


def square_calc():
    valid = False
    while valid is False:
        try:
            question = input("Would you like the area or perimeter?: ").lower()
            if question == "area":
                side = float(input("What is the length of one side in cm?: "))
                answer = side * side
                print("The area of your square is {} cm".format(answer))
                return answer
            elif question == "perimeter":
                side = float(input("What is the length of one side in cm?: "))
                answer = side * 4
                print("The perimeter of your square is {} cm".format(answer))
                return answer
            else:
                print("Please enter either area or perimeter")
        except ValueError:
            print()


def circle_calc():
    valid = False
    while valid is False:
        try:
            question = input("Are you trying to find the circumference or area?: ").lower()
            decimal_place = int(input("How many decimal places do you want?: "))
            if question == "area":
                radius = float(input("What is the radius of your circle in cm?: "))
                answer = 2 * math.pi * radius
                print("The area of your circle is {:.{}f}".format(answer, decimal_place))
                return answer
            elif question == "circumference":
                radius = float(input("What is the radius of your circle in cm?: "))
                answer = math.pi * radius ** 2
                print("The circumference of your circle is {:.{}f} cm".format(answer, decimal_place))
                return answer
            else:
                print("Please enter either area or circumference")
        except ValueError:
            print()


def rectangle_calc():
    valid = False
    while valid is False:
        try:
            question = input("Do you want to find the area or perimeter?: ").lower()
            if question == "area":
                s_side = float(input("What is the length of the short side in cm?: "))
                l_side = float(input("What is the length of the long side in cm?: "))
                answer = s_side * l_side
                print("The area of your rectangle is {} cm".format(answer))
                return answer
            elif question == "perimeter":
                s_side = float(input("What is the length of the short side in cm?: "))
                l_side = float(input("What is the length of the long side in cm?: "))
                answer = 2 * (s_side + l_side)
                print("The perimeter of your rectangle is {} cm".format(answer))
                return answer
            else:
                print("Please enter either area or perimeter")
        except ValueError:
            print()


def parallelogram_calc():
    valid = False
    while valid is False:
        try:
            question = input("Do you want to find the area or perimeter: ")
            if question == "area":
                base = float(input("What is the length of the base in cm?: "))
                height = float(input("What is the height of the parallelogram in cm?: "))
                answer = base * height
                print("The area of your parallelogram is ", answer)
                return answer
            elif question == "perimeter":
                base = float(input("What is the length of the base side in cm?: "))
                height = float(input("What is the height of the parallelogram in cm?: "))
                answer = 2 * (base + height)
                print("The perimeter of your parallelogram is {} cm".format(answer))
                return answer
            else:
                print("Please enter either area or perimeter")
        except ValueError:
            print()


# Initial variables
valid = False
while valid is False:
    try:
        question = input("What shape do you want to calculate?: ").lower()
        if question == "square":
            square = square_calc()
            break
        elif question == "circle":
            circle = circle_calc()
            break
        elif question == "rectangle":
            rectangle = rectangle_calc()
            break
        elif question == "parallelogram":
            parallelogram = parallelogram_calc()
        else:
            print("Please enter either square, circle, rectangle or parallelogram")
    except ValueError:
        print()


# Square calculations:
# Area is Side*Side
# Perimeter is Side*4

# This is due to all sides being the same size

# Rectangle calculations:
# Area is Side1*Side2 or Smaller_side*Larger_side
# Perimeter is (Side1*2)+(Side2*2) or (Smaller_side*2)+(Larger_side*2)
# Smaller/Larger side would be better in this case as there are 4 sides and the parallel sides are the same size

# Triangle calculations:
# Area is 1/2base*height
# If 1 side is known and 2 angles is known use known side(sin (known angle)) use the answer of this and do ans/sin known angle
    # Note known side and known angle have to be opposite of each other and the other angle is in the first half of the equation


# For square roots use variable1 = math.sqrt(variable2)
# For exponents use number/variable ** number/variable
