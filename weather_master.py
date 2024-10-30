"""
File: weather_master.py
Name:
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

EXIT = -100


def main():
    """
    This program help user compute the average, highest, lowest, cold days among the inputs.
    -
    Algorithm
    Main to use the "assign and re-assign" concept to variate input data.
    (I really enjoy this assignment! It seems a great practice to learn variables.)
    """
    print("StanCode \"Weather Master 4.0\"!")
    temp = int(input("Next Temperature: (or "+str(EXIT)+" to quit)? "))
    if temp == EXIT:
        print("No temperatures were entered.")
    else:
        # 1st data
        cold_days = 0
        if temp < 16:
            cold_days = 1
            # in case the first data<16, not being counted
        total_days = 1
        total_temp = temp
        highest = temp
        lowest = temp
        while True:
            temp = int(input("Next Temperature: (or "+str(EXIT)+" to quit)? "))
            # 2nd data
            total_days += 1
            total_temp = total_temp+temp
            # temperatures summary
            if temp == EXIT:
                break
            if temp > highest:
                highest = temp
            if temp < lowest:
                lowest = temp
            if temp < 16:
                cold_days += 1
        print("Highest temperature= " + str(highest))
        print("Lowest temperature= " + str(lowest))
        print("Average= " + str((total_temp-EXIT)/(total_days-1)))
        # total_days-1 to deduct the double counting
        print(str(cold_days) + " cold day(s)")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
