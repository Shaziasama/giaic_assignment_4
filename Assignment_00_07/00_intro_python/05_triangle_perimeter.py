def main():
    # Get the 3 side lengths of the triangle
    side1 = float(input("\033[1;3m What is the length of side 1? \033[0m "))
    side2 = float(input("What is the length of side 2? "))
    side3 = float(input("What is the length of side 3? "))

    # Print out the perimeter (sum of the sides) of the triangle, make sure to cast it to a str when concatenating!
    print("The perimeter of the triangle is " + str(side1 + side2 + side3))




if __name__ == '__main__':
    main()