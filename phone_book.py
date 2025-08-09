# phonebook_manager.py

def save_contact():
    """Add a new contact to the text file."""
    person_name = input("Full Name: ").strip()
    mobile_number = input("Phone Number: ").strip()
    email_id = input("Email Address: ").strip()

    with open("phonebook.txt", "a") as file:
        file.write(f"{person_name},{mobile_number},{email_id}\n")

    print(f"✔ Contact for '{person_name}' saved successfully.")

def display_contacts():
    """Show all stored contacts."""
    try:
        with open("phonebook.txt", "r") as file:
            records = file.readlines()

        if not records:
            print("⚠ No contacts available.")
            return

        print("\n📒 Stored Contacts:")
        for record in records:
            person_name, mobile_number, email_id = record.strip().split(",")
            print(f"Name: {person_name} | Phone: {mobile_number} | Email: {email_id}")

    except FileNotFoundError:
        print("⚠ No contact file found. Add a contact first.")

def find_contact():
    """Search for a contact by name or phone number."""
    keyword = input("Search by name or phone: ").strip().lower()
    match_found = False

    try:
        with open("phonebook.txt", "r") as file:
            for record in file:
                person_name, mobile_number, email_id = record.strip().split(",")
                if keyword in person_name.lower() or keyword in mobile_number:
                    print(f"🔍 Match → Name: {person_name}, Phone: {mobile_number}, Email: {email_id}")
                    match_found = True

        if not match_found:
            print("❌ No contact matches your search.")

    except FileNotFoundError:
        print("⚠ No contact file found. Add a contact first.")

def run_phonebook():
    """Main menu loop for the contact book application."""
    while True:
        print("\n===== PHONEBOOK MENU =====")
        print("1. Add a New Contact")
        print("2. View All Contacts")
        print("3. Search for a Contact")
        print("4. Exit Program")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            save_contact()
        elif choice == "2":
            display_contacts()
        elif choice == "3":
            find_contact()
        elif choice == "4":
            print("👋 Exiting phonebook. Goodbye!")
            break
        else:
            print("⚠ Invalid choice. Please try again.")

if __name__ == "__main__":
    run_phonebook()
