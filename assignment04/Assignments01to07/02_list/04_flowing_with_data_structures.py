def insert_three_times(target_list, item):
    for _ in range(3):
        target_list.append(item)


def main():
    user_input = input("Type a message to be added 3 times: ")
    result_list = []
    print("Before adding:", result_list)
    insert_three_times(result_list, user_input)
    print("After adding:", result_list)


if __name__ == "__main__":
    main()
