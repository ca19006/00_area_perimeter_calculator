# Function to calculate the area or perimeter of a square
def square_calc(term):
    if term == "area":
        base = int(input("What is the length of the base?: "))
        height = int(input("What is the height?: "))
        answer = base*height
        print("The area of your square is", answer)
        return answer
    else:
        valid = False
        side1 = int(input("What is the length of side 1?: "))
        side2 = int(input("What is the length of side 2?: "))
        side3 = int(input("What is the length of side 3?: "))
        side4 = int(input("What is the length of side 4?: "))
        answer = side1+side2+side3+side4
        print("The perimeter of your square is", answer)
        return answer
# Initial variables


valid = False
while valid == False:
    question = input("Would you like the area or perimeter?: ")
    square_calc(question)
