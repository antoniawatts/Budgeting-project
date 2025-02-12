'''
Antonia Watts
CSC110
Project 3
This program has two functions; the first computes values to organize 
finances and the second calculates taxes using a bracket. 
'''


def wheres_the_money(salary, mortgage, bills, food, travel):
    '''
    This function calculates annual costs to be put in the organized table.
    Args:
        salary: integer for user's yearly salary, used to compute percentages.
        mortagage: integer for monthly cost to find yearly mortgage cost (x12).
        bills: integer for monthly costs to find yearly cost of bills (x12).
        food: integer for weekly food costs to find yearly cost of food (x52)
        travel: integer for yearly travel cost. 
    Returns:
        Message that displays resulting values from calculations using the arguments,
        in a formatted budgeting chart with percentages and 
        equal number of '#' characers.
    '''
    # variables to calculate yearly costs
    mortgage_annual = mortgage * 12
    bills_annual = bills * 12
    food_annual = food * 52    
    
    # variable used to find amount of extra funds
    calc_extra = salary - (mortgage_annual + bills_annual + food_annual + 
    travel + calculate_tax(salary))
    
    # variable that holds the value of the largest variable 
    # to format the chart to fit all '#' characters
    largest_value = mortgage_annual
    # checks which variable is the largest 
    if bills_annual > largest_value:
        largest_value = bills_annual
    if food_annual > largest_value:
        largest_value = food_annual
    if travel > largest_value:
        largest_value = travel
    if calculate_tax(salary) > largest_value:
        largest_value = calculate_tax(salary)
    if calc_extra > largest_value:
        largest_value = calc_extra
    
    # message that holds the table and inserts all calculated values
    message = "------------------------------------------{}\n".format( "-" * \
    int((largest_value/salary) * 100)) + \
    "See the financial breakdown below, based on a salary of ${:}\n".format(salary) + \
    "------------------------------------------{}\n".format( "-" * int((largest_value/salary) * 100)) +\
    "| mortgage/rent | ${:11,.2f} | {:6,.1%} | {}\n".format(mortgage_annual,mortgage_annual/salary, "#" * int((mortgage_annual/salary) * 100))+\
    "|         bills | ${:11,.2f} | {:6,.1%} | {}\n".format(bills_annual,bills_annual/salary, "#" * int((bills_annual/salary) * 100))+\
    "|          food | ${:11,.2f} | {:6,.1%} | {}\n".format(food_annual,food_annual/salary, "#" * int((food_annual/salary) * 100)) +\
    "|        travel | ${:11,.2f} | {:6,.1%} | {}\n".format(travel,travel/salary, "#" * int((travel/salary) * 100))+\
    "|           tax | ${:11,.2f} | {:6,.1%} | {}\n".format(calculate_tax(salary),calculate_tax(salary)/salary, "#" * round((calculate_tax(salary)/salary) * 100))+\
    "|         extra | ${:11,.2f} | {:6,.1%} | {}\n".format(calc_extra,calc_extra/salary, "#" * int((calc_extra/salary) * 100))+\
    "------------------------------------------{}".format( "-" * int((largest_value/salary) * 100)) 
     # checks if extra messages need to be added to the main table
    if calculate_tax(salary) >= 75000:
        message += "\n>>> TAX LIMIT REACHED <<<"
        print(message)
        return message
    elif calc_extra < 0:
        message += "\n>>> WARNING: DEFICIT <<<"
        print(message)
        return message
    else:
        print(message)
        return message

def calculate_tax(salary):
    '''
    This function calculates the tax using a tax percentage based on salary.
    Args:
        salary: integer for user's yearly salary
    Returns: 
        Calculated tax, includes a tax cap at 75k.
    '''
    # checks which range the salary is within to assign a percentage
    if 0 <= salary and salary <= 15000:
        tax_percentage = 10
    elif 15000 < salary and salary <= 75000:
        tax_percentage = 20
    elif 75000 < salary and salary <= 200000:
        tax_percentage = 25
    else:
        tax_percentage = 30
   
    # variable to store final tax amount based on percentage
    tax_amount = salary * (tax_percentage / 100.0)
    # ensure tax does not exceed the cap at 75k
    if tax_amount >= 75000:
        return 75000
    return tax_amount
