def main():
    principal = float(input("Enter the loan amount: "))
    annual_interest_rate = float(input)
    years = int(input)
    monthly_interest_rate = annual_interest_rate / 100 / 12
    total_payments = years * 12
    
    if monthly_interest_rate > 0:
        monthly_payment = (principal * monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments) / \
                          ((1 + monthly_interest_rate) ** total_payments - 1)
    else:
        monthly_payment = principal / total_payments
    
    
    print(f"Your monthly payment is: ${monthly_payment:.2f}")
if __name__ == "__main__":
    main()