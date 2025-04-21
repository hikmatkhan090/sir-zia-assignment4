def show_first_item(items):
    """
    Displays the first item from the given list.
    """
    print("First item in the list:", items[0])


def collect_items():
    """
    Asks the user to input list items one by one and returns the completed list.
    """
    items = []
    entry: str = input("Enter an item (leave blank to finish): ")
    while entry != "":
        items.append(entry)
        entry = input("Enter another item (or press enter to stop): ")
    return items


def main():
    user_list = collect_items()
    if user_list:
        show_first_item(user_list)
    else:
        print("The list is empty. Nothing to show.")


if __name__ == '__main__':
    main()
