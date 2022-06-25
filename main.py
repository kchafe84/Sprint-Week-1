# Preparing travel claims processing system program for NL Chocolate Company.
# Authors: Kyle Snow & Ken Chafe
# Start Date: 2022-07-17
# Completion Date: 2022-07-25


# Using functions created to format values & dates. Located in FormatValues.py included with the program
import FormatValues as FV

import datetime
import math
import matplotlib.pyplot as plt


# Stating constants for the EmployeeTravelClaim(): function.

Daily_Rate = 85.00
Mileage_Rate = 0.17
RentedCarDaily_Rate = 65.00
HST_Rate = 0.15


def CalcBonus(TripDay, KiloTravel, CType, DateMonth, DateDay):

    # Created by Kyle
    # Function to calculate the bonus in the EmployeeTravelClaim(): program.
    # This function takes in Days of the trip, Kilo's traveled, Claim type, start day, and month, as parameters.
    # And returns the bonus.

    Bonus = 0

    if TripDay > 3:
        Bonus = Bonus + 100.00

    if KiloTravel > 1000.00:
        Bonus = Bonus + (0.04 * KiloTravel)

    if CType == "E":
        Bonus = Bonus + (45.00 * TripDay)


    if DateMonth == 12 and DateDay <= 22 and DateDay >= 15:
        Bonus = Bonus + (50.00 * TripDay)

    return Bonus


def EmployeeTravelClaim():

    # Created by Kyle
    # Function to calculate and process an employees travel claims.

    # Gathering all inputs

    while True:

        while True:

            EmpNumber = input("Enter the Employee number (5 characters): ")
            EmpNumber = EmpNumber.upper()

            if EmpNumber == "":
                print("Error - Cannot be blank. ")

            elif len(EmpNumber) > 5 or len(EmpNumber) < 5:
                print("Error - Must be 5 characters. ")

            else:
                break

        while True:

            allowed_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz'")

            EmpFirstName = input("Enter employee first name: ")
            EmpFirstName = EmpFirstName.title()

            if EmpFirstName == "":
                print("Error - Cannot be blank. ")

            elif set(EmpFirstName).issubset(allowed_characters) == False:
                print("Error - Invalid characters. ")

            else:
                break

        while True:


            EmpLastName = input("Enter employee last name: ")
            EmpLastName = EmpLastName.title()

            if EmpLastName == "":
                print("Error - Cannot be blank. ")

            elif set(EmpLastName).issubset(allowed_characters) == False:
                print("Error - Invalid characters. ")

            else:
                break

        while True:

            Location = input("Enter the location of the trip: ")
            Location = Location.title()

            if Location == "":
                print("Error - Cannot be blank. ")

            elif set(Location).issubset(allowed_characters) == False:
                print("Error - Invalid characters. ")

            else:
                break

        CurrentDate = datetime.datetime.now()

        while True:

            try:

                StartDate = input("Enter the trip start date (YYYY-MM-DD): ")
                StartDate = datetime.datetime.strptime(StartDate, "%Y-%m-%d")

            except:
                print("Error - Incorrect format. ")

            else:
                if StartDate > CurrentDate:
                    print("Error - cannot be after the current date")
                else:
                    break

        EndDateDeadline = StartDate + datetime.timedelta(days= 7)

        while True:

            try:

                EndDate = input("Enter the trip end date (YYYY-MM-DD): ")
                EndDate = datetime.datetime.strptime(EndDate, "%Y-%m-%d")
                EndDateDay = EndDate.day

            except:
                print("Error - Incorrect format. ")

            else:
                if EndDate < StartDate:
                    print("Error - Cannot be before the start date. ")
                elif EndDate > EndDateDeadline:
                    print("Error - Cannot be no more then 7 days after start date. ")

                else:
                    break

        DateDifference = EndDate - StartDate
        TripDays = DateDifference.days

        while True:

            CarRentOrOwn = input("Was the car your own or rented, Enter (O OR R): ")
            CarRentOrOwn = CarRentOrOwn.upper()

            if CarRentOrOwn == "":
                print("Error - Cannot br blank. ")

            elif CarRentOrOwn.upper() != "O" and CarRentOrOwn.upper() != "R":
                print("Error - must be O or R. ")

            else:
                break

        KiloTraveled = 0

        while CarRentOrOwn == "O":

            try:

                KiloTraveled = input("Enter the Kilometers driven: ")
                KiloTraveled = int(KiloTraveled)

            except:
                print("Error - Must be numbers. ")

            else:
                if KiloTraveled > 2000:
                    print("Error - Cannot exceed 2000 KM. ")

                elif KiloTraveled < 0:
                    print("Error - Cannot be less then 0. ")

                else:
                    break

        while True:

            ClaimType = input("Enter the claim type, Standard or executive (S or E): ")
            ClaimType = ClaimType.upper()

            if ClaimType == "":
                print("Error - Cannot be blank. ")

            elif ClaimType.upper() != "S" and ClaimType.upper() != "E":
                print("Error - Must be S or E. ")

            else:
                break

    # Calculations

        PerDiemAmount = TripDays * Daily_Rate

        MileageAmount = 0
        RentedCarAmount = 0

        if CarRentOrOwn == "O":

            MileageAmount = KiloTraveled * Mileage_Rate

        if CarRentOrOwn == "R":

            RentedCarAmount = TripDays * RentedCarDaily_Rate


        StartDateMonth = StartDate.month
        StartDateDay = StartDate.day

    # Here is where the CalcBonus(): function is used to determine the bonus.

        Bonus = CalcBonus(TripDays, KiloTraveled, ClaimType, StartDateMonth, StartDateDay)


        ClaimAmount = PerDiemAmount + MileageAmount + Bonus

        HST = PerDiemAmount * HST_Rate

        ClaimTotal = ClaimAmount + HST

    # Printing all the outputs

        print()
        print("{:^40s}".format("NL Chocolate Company "))
        print("{:^40s}".format("Employee Travel Claims "))
        print("{:^40s}".format(FV.FDateLong(CurrentDate)))
        print()
        print("To:")
        print("   {} {}".format(EmpFirstName, EmpLastName))
        print("   Employee Number {}".format(EmpNumber))
        print("-" * 40)
        print("Trip Location: {}".format(Location))
        print("Start Date:    {:>10s}".format(FV.FDateShort(StartDate)))
        print("End Date:      {:>10s}        Days: {}".format(FV.FDateShort(EndDate), TripDays))
        print("Claim Type:                         {}".format(ClaimType))
        print("-" * 40)

    # the if statements are to make the output print different lines based on the users input.

        if CarRentOrOwn == "O":
            print("Vehicle Used:                   {:>8s}".format("Personal"))
            print("Kilometers Traveled:             {:>4d} KM".format(KiloTraveled))
            print("Mileage Amount:                  {:>7s}".format(FV.FDollar2(MileageAmount)))

        if CarRentOrOwn == "R":
            print("Vehicle Used:                    {:>7s}".format("Rental"))
            print("Rented Car Amount:               {:>7s}".format(FV.FDollar2(RentedCarAmount)))

        print("                                --------")
        print("Per Diem:                        {:>7s}".format(FV.FDollar2(PerDiemAmount)))
        print("Bonus:                           {:>7s}".format(FV.FDollar2(Bonus)))
        print("Claim:                         {:>9s}".format(FV.FDollar2(ClaimAmount)))
        print("HST:                             {:>7s}".format(FV.FDollar2(HST)))
        print("                                --------")
        print("Total Claim:                   {:>9s}".format(FV.FDollar2(ClaimTotal)))
        print()

    # Prompt to go back to the main menu or process another claim.

        while True:

            backtomenu = input("Would you like to process another claim? (Y/N): ")

            if backtomenu == "":
                print("Error - Cannot be blank ")

            elif backtomenu.upper() != "Y" and backtomenu.upper() != "N":
                print("Error - Must be Y or N ")

            else:
                break

        if backtomenu.upper() == "N":
            break



def FunInterviewQuestion():

    # Created by Kyle
    # A function that Creates a loop and executes it 100 times
    # Prints out numbers 1 to 100
    # Then for every number divisible 5 it displays Fizz
    # For every number divisible by 8 it displays Buzz
    # If divisible by both it displays FizzBuzz

    for numbers in range(1, 101):

        if numbers % 5 == 0 and numbers % 8 == 0:

            numbers = "FizzBuzz"

        elif numbers % 5 == 0:

            numbers = "Fizz"

        elif numbers % 8 == 0:

            numbers = "Buzz"

        print(numbers)

    print()

    # Prompt to get the user back to the main menu.

    while True:
        backtomenu = input("Press any key to return to menu: ")
        break


def StringAndDates():

    # Created by Ken
    # A function that asks for employee information.
    # manipulate strings and dates, and print it to the screen.

    # Gathering inputs

    while True:

        cur_date = datetime.datetime.now()
        time = datetime.timedelta
        first_name = input("Enter Employee First Name: ")
        first_name = first_name.title()
        last_name = input("Enter Employee Last Name: ")
        last_name = last_name.title()
        phone_number = input("Enter Phone Number: ")
        cur_date = cur_date
        birtdate = input("Enter Birthdate: ")

        while True:
            try:
                start_date = input("Enter the employee start date (YYYY-MM-DD): ")
                start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
            except:
                print("Error - Incorrect format. ")
            else:
                if start_date > cur_date:
                    print("Error - cannot be after the current date")
                else:
                    break

        # Creating employee number and calculating next evaluation date.

        employee_num = first_name.title() + last_name.title() + phone_number[7:10]
        next_evaluation = cur_date + datetime.timedelta(days=30)

        print("       Employee Monthly Evaluation")
        print("-" * 40)
        print("Date: {}".format(cur_date.strftime("%m-%d-%Y")))
        print("Employee Name:               {} {}".format(first_name, last_name))
        print("Employee Number:             {}".format(employee_num))
        print("Employee Phone Number:       {}".format(phone_number))
        print("Employee Start Date:         {}".format(start_date.strftime("%m-%d-%Y")))
        print("Employee Birth Date:         {}".format(birtdate))
        print("Next Evaluation:             {}".format(next_evaluation.strftime("%m-%d-%Y")))

        # Prompt to go back to the main menu or process another claim.

        while True:

            backtomenu = input("Would you like to process another employee? (Y/N): ")

            if backtomenu == "":
                print("Error - Cannot be blank ")

            elif backtomenu.upper() != "Y" and backtomenu.upper() != "N":
                print("Error - Must be Y or N ")

            else:
                break

        if backtomenu.upper() == "N":
            break


def GraphMonthClaims():

    # Created by Ken
    # A function that asks for monthly sales then creates a graph based on numbers entered.


    # Gathering the number values for each month

    while True:


        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October','November', 'December']
        sales = []

        for x in range(1, 13):

            while True:

                try:

                    TotalMonthSales = input("Enter the total monthly sales for " + months[x - 1] + ": ")
                    TotalMonthSales = float(TotalMonthSales)

                except:
                    print("Error - Must be a value ")

                else:
                    break


            sales.append(TotalMonthSales)


        print()
        print(months)
        print(sales)

        # Calculation for Graphing Total Monthly Sales

        plt.plot(months, sales, "m")
        plt.xlabel('Months')
        plt.ylabel('Total Sales')
        plt.title('Total Monthly Sales Per Month')
        plt.grid(True)
        plt.show()
        print()

        # Prompt to go back to the main menu or create another graph.

        while True:

            print()

            backtomenu = input("Would you like to create another graph? (Y/N): ")

            if backtomenu == "":
                print("Error - Cannot be blank ")

            elif backtomenu.upper() != "Y" and backtomenu.upper() != "N":
                print("Error - Must be Y or N ")

            else:
                break

        if backtomenu.upper() == "N":
            break




# Main program starts here
# Main menu program



while True:

    # displaying menu choices

    print()
    print("NL Chocolate Company ")
    print("Travel Claims Processing System ")
    print()
    print("1. Enter an Employee Travel Claim. ")
    print("2. Fun Interview Question. ")
    print("3. Cool Stuff with Strings and Dates. ")
    print("4. Graph Monthly Claims Totals. ")
    print("5. Quit Program. ")
    print()

    # Validating Choice selected

    while True:

        try:

            Selection = input("   Enter choice (1-5): ")
            Selection = int(Selection)

        except:
            print("Error - Must be (1-5) ")

        else:
            if Selection > 5 or Selection  < 1:
                print("Error - Number must be on the list. ")
            else:
                break

    print()

    # Determining the choice selected, and sending the user to the function needed

    if Selection == 1:
        EmployeeTravelClaim()

    if Selection == 2:
        FunInterviewQuestion()

    if Selection == 3:
        StringAndDates()

    if Selection == 4:
        GraphMonthClaims()

    if Selection == 5:
        break



