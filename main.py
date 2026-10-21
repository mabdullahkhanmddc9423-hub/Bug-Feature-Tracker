def add_entry(entries):
    title = input("Enter title/description: ").strip()
    if not title:
        print("Error: Title cannot be empty!")
        return

    entry_type = input("Enter type (Bug/Feature): ").strip().capitalize()
    if entry_type not in ["Bug", "Feature"]:
        print("Invalid type! Setting default to 'Bug'.")
        entry_type = "Bug"

    priority = input("Enter priority (Low/Medium/High): ").strip().capitalize()
    if priority not in ["Low", "Medium", "High"]:
        print("Invalid priority! Setting default to 'Medium'.")
        priority = "Medium"

    status = input("Enter status (Open/Resolved): ").strip().capitalize()
    if status not in ["Open", "Resolved"]:
        print("Invalid status! Setting default to 'Open'.")
        status = "Open"

    entry = {
        "title": title,
        "type": entry_type,
        "priority": priority,
        "status": status
    }
    entries.append(entry)
    print("Entry added successfully!")

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