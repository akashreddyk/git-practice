def add(val_a: int, val_b: int) -> int:
    return val_a+val_b

if __name__ == "__main__":
    first_value = input("Enter first value: ")
    second_value = input("Enter second value: ")
    result = add(first_value,second_value)
    print(result)

