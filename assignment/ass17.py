def multiply_list_elements(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product

def main():
    numbers = [float(x) for x in input("Enter numbers separated by spaces: ").split()]
    result = multiply_list_elements(numbers)

    print(f"The product of all the numbers in the list is: {result}")

if __name__ == "__main__":
    main()