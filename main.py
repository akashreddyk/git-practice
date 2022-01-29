def add(a: int, b: int) -> int:
    """Addition Function
    """
    return a+b

if __name__ == "__main__":
    first_value = input("Enter first value: ")
    second_value = input("Enter second value: ")
    result = add(first_value,second_value)
    print(result)

