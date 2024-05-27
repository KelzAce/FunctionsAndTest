def main():
    """
    This program computes and prints the remaining 
    balance for a loan with a fixed annual percentage rate and a fixed number 
    of payments per year
    """

    principal = float(input("Principal amount: "))
    annual_rate = float(input("Annual percentage rate: "))
    years = int(input("Number of years in the life of the loan: " ))
    payment_per_year = int(input("Number of payments per year: "))
    payments_made = int(input("Number of payment already paid: "))

    balance = compute_balance(principal, annual_rate, years, payment_per_year, payments_made)
    print()
    print(f"Balance remaining: {balance}")

def compute_balance(princ, annual_rate, years, payment_per_year, payments_made):
    """Calculate and return the remaining balance of a laon after a certain 
    number of payment have been made.
    
    """
    payment = computer_payment(princ, annual_rate, years, payment_per_year)
    rate = annual_rate / payment_per_year


    # Compound Interest
    power = (1 + rate)** payments_made
    print()
    print(f"payment: {payment} rate: {rate}, power: {power}")
    balance = princ * power - payment * (power - 1) / rate
    print(f"balance: {balance}")
    return round(balance, 2)


def computer_payment(princ, annual_rate, years, payment_per_year):
    """Calculate the fixed payment per period"""
    print()
    print(f"Compute_payment({princ}, {annual_rate}, {years}, {payment_per_year})")

    rate = annual_rate / payment_per_year

    n = years * payment_per_year

    print(f" rate: {rate} n: {n}")
    payment = princ * rate / (1 - (1 + rate) ** -n)

    print(f" payment: {payment}")
    return round(payment, 2)

if __name__ == "__main__":
    main()



