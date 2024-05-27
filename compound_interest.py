def main():
    principal = float(input("Principal amount: "))
    annual_rate = float(input("Annual percentage rate: "))
    times_compounded_per_year = int(input(" times_compounded_per_year"))
    years = int(input("Number of years in the life of the loan: " ))

    compound_interest = calculate_compound_interest(principal, annual_rate, times_compounded_per_year, years)

    print(f"Compound interest: {compound_interest}")


def calculate_compound_interest(principal, annual_rate, times_compounded_per_year, years):
    """writing a function that calculates compound interest

    Parameters:
    principal:
    annual rate
    times_compounded_per_year
    years

    return the amount after compounding
    
    """
    rate_per_period =  annual_rate / times_compounded_per_year

    newRate = rate_per_period / 100

    total_period = times_compounded_per_year * years

    amount = principal * (1 + newRate)** total_period

    return amount


if __name__ == "__main__":
    main()


# def main():
#     principal = float(input("Principal amount: "))
#     annual_rate = float(input("Annual percentage rate: ")) / 100  # Convert to decimal
#     times_compounded_per_year = int(input("Times compounded per year: "))
#     years = int(input("Number of years in the life of the loan: "))

#     compound_interest = calculate_compound_interest(principal, annual_rate, times_compounded_per_year, years)

#     print(f"Compound interest: {compound_interest:.2f}")


# def calculate_compound_interest(principal, annual_rate, times_compounded_per_year, years):
#     """
#     Calculates compound interest

#     Parameters:
#     principal: Initial amount of money
#     annual_rate: Annual interest rate as a decimal
#     times_compounded_per_year: Number of times interest is compounded per year
#     years: Number of years the money is invested

#     Returns:
#     The amount after compounding
#     """
#     rate_per_period = annual_rate / times_compounded_per_year
#     total_periods = times_compounded_per_year * years
#     amount = principal * (1 + rate_per_period) ** total_periods

#     return amount


# if __name__ == "__main__":
#     main()
