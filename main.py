def main():
    entries = []
    while True:
        print("\n=== Bug & Feature Tracker ===")
        print("1. Add Entry")
        print("2. View All Entries")
        print("3. View Summary Statistics")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice! Please select between 1 and 4.")

if __name__ == "__main__":
    main()