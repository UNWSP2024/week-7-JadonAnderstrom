# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.
def rainfall_stats():
    # Initialize an empty list to store the rainfall data
    rainfall = []

    # Get rainfall data from the user for each month
    for i in range(12):
        while True:
            try:
                # Get the rainfall for the month and ensure it's a float
                rain = float(input(f"Enter the rainfall for month {i + 1}: "))
                rainfall.append(rain)
                break
            except ValueError:
                print("Please enter a valid number.")

    #Calculate total rainfall
    total_rainfall = sum(rainfall)

    #Average monthly rainfall
    average_rainfall = total_rainfall / 12

    #Highest and lowest rainfall
    highest_rainfall = max(rainfall)
    lowest_rainfall = min(rainfall)
    month_highest = rainfall.index(highest_rainfall) + 1
    month_lowest = rainfall.index(lowest_rainfall) + 1

    #Display results
    print("\nRainfall Statistics")
    print(" -----------------")
    print(f"Total rainfall for the year: {total_rainfall:.2f}")
    print(f"Average monthly rainfall: {average_rainfall:.2f}")
    print(f"Month {month_highest} had the highest rainfall: {highest_rainfall:.2f}")
    print(f"Month {month_lowest} had the lowest rainfall: {lowest_rainfall:.2f}")

#Call function
rainfall_stats()

  # Jadon anderstrom, October 18th, "rainfall".
