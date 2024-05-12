# The first indented line inside the function is the doc_string  the indented string should be in ''' doc string''' 

#Example
def days_in_month(year, month):
    '''This is a doc string'''
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
days_in_month()