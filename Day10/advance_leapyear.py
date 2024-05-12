#Function to find leap year 
def leap_year(year):
    if(year % 4 == 0):
        if(year % 100 == 0):
            if(year % 400 == 0):
                return True
            else:
                return False
        else:
            return True

    else:
        return False

#Function to calculate days in given year month
def days_in_month(year, month):
    
    month_days = [
    31,  # January
    28,  # February (non-leap year)
    31,  # March
    30,  # April
    31,  # May
    30,  # June
    31,  # July
    31,  # August
    30,  # September
    31,  # October
    30,  # November
    31   # December
    ]
    if leap_year(year):
        month_days[1] = 29
        return (month_days[month-1])
    else: 
    
        return month_days[month-1]

#Taking inputs from user
year = int(input("Enter a year: "))
month = int (input("Enter a month: "))
day = days_in_month(year, month)
print(day)