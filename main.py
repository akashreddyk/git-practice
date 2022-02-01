def add(a: int, b: int) -> int:
    """Addition Fu
    """
    return a+b

if __name__ == "__main__":
    first_value = input("Enter first value: ")
    second_value = input("Enter second value: ")
    result = add(first_value,second_value)
    print("Printing Result :")
    print(result)

