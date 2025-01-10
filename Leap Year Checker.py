#Leap Year Checker
#Amelie Lynde

#Init
#Rules for Leap Year:
#If a year is divisible by 4, it is a leap year.
#However, if that year is also divisible by 100, it is not a leap year, unless
#it is divisible by 400. In that case, it is a leap year.

#Functions
def leap_year(year):
    if year % 400 == 0:
        print("True")
    elif year % 100 == 0:
        print("False")
    elif year % 4 == 0:
        print("True")


#Main
leap_year(2024) #true
leap_year(1900) #false
leap_year(1600) #true
