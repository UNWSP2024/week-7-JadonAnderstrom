# Program #4: Coordinates
# Write a distance function that will take two 3-dimensional coordinates (as input) 
# and will return (as output) the distance between those points in space.  
# The 3-dimensional coordinates must be stored as tuples.
# Now write a mainline that has the user enter the two tuples.  
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.  
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is 
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2) 
import math

def distance(coord1, coord2):
    # Calculate the distance using the formula: sqrt((x2 - x1)^2 + (y2 - y1)^2 + (z2 - z1)^2)
    return math.sqrt(
        (coord2[0] - coord1[0]) ** 2 +
        (coord2[1] - coord1[1]) ** 2 +
        (coord2[2] - coord1[2]) ** 2
    )

def main():
    print("Enter the coordinates as x, y, z.")
    try:
        # Get first coordinate from user
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        z1 = float(input("Enter z1: "))
        coord1 = (x1, y1, z1)
        
        # Get second coordinate from the user
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))
        z2 = float(input("Enter z2: "))
        coord2 = (x2, y2, z2)
        
        # Call distance function and store result
        result = distance(coord1, coord2)
        
        # Display distance
        print(f"\nThe distance between the points {coord1} and {coord2} is: {result:.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values for the coordinates.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call main function.
if __name__ == '__main__':
    main()

# Jadon Anderstrom, October 18th, "Coordintes".
