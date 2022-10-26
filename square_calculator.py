# Function to calculate the area or perimeter of a square
def square_calc():
    valid = False
    while valid is False:
        try:
            question = input("Would you like the area or perimeter?: ").lower()
            if question == "area":
                side = int(input("What is the length of one side in cm?: "))
                answer = side * side
                print("The area of your square is", answer)
                return answer
            elif question == "perimeter":
                side = int(input("What is the length of one side in cm?: "))
                answer = side * 4
                print("The perimeter of your square is", answer)
                return answer
            else:
                print("Please enter either area or perimeter")
        except ValueError:
            print()


def triangle_calc():
    question = input("Are you using trigonometry?:").lower()
    if question == "yes":
        "a"

# Initial variables


square_calc()
triangle_calc()
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




