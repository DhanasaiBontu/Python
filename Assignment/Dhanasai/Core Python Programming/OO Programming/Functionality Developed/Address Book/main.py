from usecases.uc1_create_contact import main as uc1_main
from usecases.uc2_add_contact import main as uc2_main
from usecases.uc3_edit_contact import main as uc3_main
from usecases.uc4_delete_contact import main as uc4_main
from usecases.uc5_add_multiple_contacts import main as uc5_main
from usecases.uc6_manage_multiple_books import main as uc6_main
from usecases.uc7_duplicate_check import main as uc7_main
from usecases.uc8_search_city_state import main as uc8_main
from usecases.uc9_view_by_city_state import main as uc9_main
from usecases.uc10_count_by_city_state import main as uc10_main
from usecases.uc11_sort_by_name import main as uc11_main
from usecases.uc12_sort_by_attr import main as uc12_main
from usecases.uc13_file_io import main as uc13_main
from usecases.uc14_csv_io import main as uc14_main
from usecases.uc15_json_io import main as uc15_main

def main():
    print("Welcome to Address Book Program")
    while True:
        print("\nSelect a Use Case to run (1-15) or 0 to Exit:")
        print("1. UC1 - Create Contact")
        print("2. UC2 - Add Contact")
        print("3. UC3 - Edit Contact")
        print("4. UC4 - Delete Contact")
        print("5. UC5 - Add Multiple Contacts")
        print("6. UC6 - Manage Multiple Address Books")
        print("7. UC7 - Duplicate Check")
        print("8. UC8 - Search by City/State")
        print("9. UC9 - View by City/State")
        print("10. UC10 - Count by City/State")
        print("11. UC11 - Sort by Name")
        print("12. UC12 - Sort by City/State/Zip")
        print("13. UC13 - File IO")
        print("14. UC14 - CSV IO")
        print("15. UC15 - JSON IO")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("Exiting program. Goodbye!")
            break
        elif choice == "1":
            uc1_main()
        elif choice == "2":
            uc2_main()
        elif choice == "3":
            uc3_main()
        elif choice == "4":
            uc4_main()
        elif choice == "5":
            uc5_main()
        elif choice == "6":
            uc6_main()
        elif choice == "7":
            uc7_main()
        elif choice == "8":
            uc8_main()
        elif choice == "9":
            uc9_main()
        elif choice == "10":
            uc10_main()
        elif choice == "11":
            uc11_main()
        elif choice == "12":
            uc12_main()
        elif choice == "13":
            uc13_main()
        elif choice == "14":
            uc14_main()
        elif choice == "15":
            uc15_main()
        else:
            print("Invalid choice. Please enter a number between 0 and 15.")

if __name__ == "__main__":
    main()
