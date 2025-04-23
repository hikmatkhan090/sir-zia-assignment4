def main():
    items = []  

    entry = input("Type a value (or press Enter to stop): ")
    while entry:  
        items.append(entry)  
        entry = input("Type another value (or press Enter to stop): ")

    print("Final list:", items)


if __name__ == '__main__':
    main()
