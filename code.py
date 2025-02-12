def wheres_the_money(salary, mortgage, bills, food, travel):
    mortgage_annual = mortgage * 12
    bills_annual = bills * 12
    food_annual = food * 52    
    
    
    calc_extra = salary - (mortgage_annual + bills_annual + food_annual + 
    travel + calculate_tax(salary))
    
    
    largest_value = mortgage_annual
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

    

    message = "------------------------------------------{}\n".format( "-" * \
    int((largest_value/salary) * 100)) + \
    "See the financial breakdown below, based on a salary of ${:}\n".format(salary) + \
    "------------------------------------------{}\n".format( "-" * int((largest_value/salary) * 100)) +\
    "| mortgage/rent | ${:11,.2f} | {:7,.1%} | {} \n".format(mortgage_annual,mortgage_annual/salary, "#" * int((mortgage_annual/salary) * 100))+\
    "|         bills | ${:11,.2f} | {:7,.1%} | {} \n".format(bills_annual,bills_annual/salary, "#" * int((bills_annual/salary) * 100))+\
    "|          food | ${:11,.2f} | {:7,.1%} | {} \n".format(food_annual,food_annual/salary, "#" * int((food_annual/salary) * 100)) +\
    "|        travel | ${:11,.2f} | {:7,.1%} | {} \n".format(travel,travel/salary, "#" * int((travel/salary) * 100))+\
    "|           tax | ${:11,.2f} | {:7,.1%} | {} \n".format(calculate_tax(salary),calculate_tax(salary)/salary, "#" * round((calculate_tax(salary)/salary) * 100))+\
    "|         extra | ${:11,.2f} | {:7,.1%} | {} \n".format(calc_extra,calc_extra/salary, "#" * int((calc_extra/salary) * 100))+\
    "------------------------------------------{}\n".format( "-" * int((largest_value/salary) * 100)) 
    
    if calculate_tax(salary) >= 75000:
        message += ">>> TAX LIMIT REACHED <<<"
        return message
    elif calc_extra < 0:
        message += ">>> WARNING: DEFICIT <<<"
        return message
    else:
        return message

def calculate_tax(salary):
    if salary <= 15000:
        tax_percentage = 10
    elif salary <= 75000:
        tax_percentage = 20
    elif salary <= 200000:
        tax_percentage = 25
    else:
        tax_percentage = 30
    
    tax_amount = salary * (tax_percentage / 100.0)
    
    return tax_amount

def main():
    print(wheres_the_money())

main()
