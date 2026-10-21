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


def view_entries(entries):
    if not entries:
        print("No entries recorded yet.")
        return
    print("\n--- All Recorded Entries ---")
    for i, entry in enumerate(entries, 1):
        print(f"{i}. [{entry['type']}] {entry['title']} | Priority: {entry['priority']} | Status: {entry['status']}")


def display_statistics(entries):
    total = len(entries)
    bugs = sum(1 for e in entries if e['type'] == 'Bug')
    features = sum(1 for e in entries if e['type'] == 'Feature')
    open_entries = sum(1 for e in entries if e['status'] == 'Open')
    resolved_entries = sum(1 for e in entries if e['status'] == 'Resolved')

    print("\n--- Tracker Statistics ---")
    print(f"Total Entries: {total}")
    print(f"Total Bugs: {bugs}")
    print(f"Total Features: {features}")
    print(f"Open Entries: {open_entries}")
    print(f"Resolved Entries: {resolved_entries}")


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
            add_entry(entries)
        elif choice == '2':
            view_entries(entries)
        elif choice == '3':
            display_statistics(entries)
        elif choice == '4':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice! Please select between 1 and 4.")


if __name__ == "__main__":
    main()