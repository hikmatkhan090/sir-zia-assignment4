def access_element(lst, index):
    try:
        return f"Element at index {index}: {lst[index]}"
    except IndexError:
        return "⚠️ Index out of range."

def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return f"✅ Modified list: {lst}"
    except IndexError:
        return "⚠️ Index out of range."

def slice_list(lst, start, end):
    return f"🧩 Sliced portion ({start}:{end}): {lst[start:end]}"

def index_game():
    lst = [1, 2, 3, 4, 5]
    print("🎮 Welcome to the List Index Game!")
    print("Your current list:", lst)

    while True:
        print("\nChoose an operation: access, modify, slice or quit")
        operation = input("🔧 Operation: ").strip().lower()

        if operation == "access":
            index = int(input("Enter the index you want to access: "))
            print(access_element(lst, index))
        elif operation == "modify":
            index = int(input("Enter the index you want to modify: "))
            new_value = input("Enter the new value: ")
            print(modify_element(lst, index, new_value))
        elif operation == "slice":
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print(slice_list(lst, start, end))
        elif operation == "quit":
            print("👋 Exiting the game. Bye!")
            break
        else:
            print("❌ Invalid operation. Please choose from access, modify, slice, or quit.")

if __name__ == "__main__":
    index_game()
