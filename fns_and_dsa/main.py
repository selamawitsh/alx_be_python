from arithmetic_operations import perform_operation
import shopping_list_manager
import explore_datetime
import temp_conversion_tool


def arithmetic_menu():
    print("\nArithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")


def datetime_menu():
    print("\nExplore Datetime")
    explore_datetime.display_current_datetime()
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        explore_datetime.calculate_future_date(days)
    except ValueError:
        print("Invalid input. Please enter an integer.")


def temp_conversion_menu():
    print("\nTemperature Conversion Tool")
    temp_conversion_tool.run()   # changed from main() to run()


def shopping_list_menu():
    print("\nShopping List Manager")
    shopping_list_manager.run()   # changed from main() to run()


def main():
    while True:
        print("\n===== Main Menu =====")
        print("1. Arithmetic Operations")
        print("2. Shopping List Manager")
        print("3. Explore Datetime")
        print("4. Temperature Conversion Tool")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            arithmetic_menu()
        elif choice == "2":
            shopping_list_menu()
        elif choice == "3":
            datetime_menu()
        elif choice == "4":
            temp_conversion_menu()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
