def show_last_item(data_list):
    """Displays the last item of the given list if it's not empty."""
    if data_list:
        print("Last item in the list:", data_list[-1])
    else:
        print("The list is empty!")


def gather_items():
    """Asks the user to input elements and builds the list."""
    items = []
    while True:
        entry = input("Add an item (leave blank to finish): ").strip()
        if entry == "":
            break
        items.append(entry)
    return items


def main():
    user_data = gather_items()
    show_last_item(user_data)


if __name__ == '__main__':
    main()
