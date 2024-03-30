def leap_year(p_year):
    if p_year % 400 == 0 and p_year % 100 == 0:
        return f"{p_year} is a leap year"
    elif p_year % 4 == 0 and p_year % 100 != 0:
        return f"{p_year} is a leap year"
    else:
        return f"{p_year} is not a leap year"
