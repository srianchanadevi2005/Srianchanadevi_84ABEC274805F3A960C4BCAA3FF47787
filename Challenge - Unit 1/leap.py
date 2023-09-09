def checkLeapYear(year):
    if year%400==0:
# if year is divisible by 400, return True
            return True
    elif year%4==0:
# if year is divisible by 4,then check is it divisible by 100 or not
            if year%100!=0:
#if year is not divisible by 100, then return True
                    return True
            else:
#if year is divisible by 100, then return False
                    return False;
    
# Driver Code for the leap year program in python
#taking input (year) from the user
year = int(input("Enter the year: "))
if (checkLeapYear(year)):
#if checkLeapYear function returns true
    print("Leap Year")
else:
#if checkLeapYear function returns false
    print("Not a Leap Year")