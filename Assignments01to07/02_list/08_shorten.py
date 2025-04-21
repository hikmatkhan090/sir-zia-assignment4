LIMIT: int = 4

def trim_list(data):
    """
    Removes elements from the end of the list until its length is within the allowed limit.
    """
    while len(data) > LIMIT:
        removed = data.pop()
        print("Removed:", removed)


def collect_input():
    """
    Asks the user to enter elements one by one, returns the full list.
    """
    items = []
    entry = input("Enter an item (or press Enter to finish): ")
    while entry != "":
        items.append(entry)
        entry = input("Enter another item (or press Enter to finish): ")
    return items


def main():
    user_list = collect_input()
    trim_list(user_list)


if __name__ == '__main__':
    main()
