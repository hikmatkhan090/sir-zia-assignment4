def calculate_total(numbers: list[int]) -> int:
    """
    Receives a list of integers and returns their total sum.
    """
    result: int = 0
    for num in numbers:
        result += num
    return result


def main():
    values: list[int] = [1, 2, 3, 4, 5]
    total_sum: int = calculate_total(values)
    print(total_sum)


if __name__ == '__main__':
    main()
