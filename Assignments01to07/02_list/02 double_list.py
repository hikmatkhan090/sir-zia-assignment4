def main():
    digits: list[int] = [1, 2, 3, 4, 5, 6, 7]

  
    for idx, original_value in enumerate(digits):
        digits[idx] = original_value * 2

    print(digits)


if __name__ == '__main__':
    main()
