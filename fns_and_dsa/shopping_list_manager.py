def add_item(shopping_list: list):
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"{item} added to the list")

def remove_item(shopping_list: list):
    item = input("Enter the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from the list")
    else:
        print("Item not found in the list")

def view_items(shopping_list: list):
    if shopping_list:
        print("Shopping List:")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")
    else:
        print("Shopping list is empty.")

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            add_item(shopping_list)
        elif choice == '2':
            # Prompt for and remove an item
            remove_item(shopping_list)
        elif choice == '3':
            # Display the shopping list
            view_items(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()