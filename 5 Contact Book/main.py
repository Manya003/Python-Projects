# Contact Book

def menu():
    print("\n--- Contact Book ---")
    print("1. Add Contact ")
    print("2. Remove Contact ")
    print("3. Update Contact ")
    print("4. Display Contacts ")
    print("5. Search Contact ")
    print("6. Exit ")
 
contacts = {}

# Save contacts to file
def save_contacts():
    with open("contacts.txt", "w") as file:
        for name, phone in contacts.items():
            file.write(f"{name},{phone}\n")


# Load contacts from file
def load_contacts():
    contacts.clear()
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                name, phone = line.strip().split(",")
                contacts[name] = phone
    except:
        pass

#  Phone Number Validation
def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10

# Name Validation
def is_valid_name(name):
    return len(name) <= 15

#  Add Contact
def add_contact(contacts):
    name = input("Enter name: ")
    
    if not is_valid_name(name):
        print("Name should be at most 15 characters!")
        return

    phone = input("Enter phone number: ")

    if not is_valid_phone(phone):
        print("Phone number must be exactly 10 digits!")
        return
    
    if name in contacts:
        print("⚠️ Contact already exists!")
    else:
        contacts[name] = phone
        save_contacts()  
        print("Contact added successfully!")

    display_contacts(contacts)

# Remove Contact
def remove_contact(contacts):
    # Check if contacts dictionary is empty
    if not contacts:
        print("You cannot remove a contact because no contacts exist!")
        return

    name = input("Enter name to remove: ")
    
    if name in contacts:
        del contacts[name]
        save_contacts()
        print("Contact removed!")
    else:
        print("Contact not found!")

    display_contacts(contacts) 

# Update Contact
def update_contact(contacts):
    name = input("Enter name to update: ")
    
    if name in contacts: 
        print("What do you want to update?")
        print("1. Name")
        print("2. Phone Number")
        
        choice = input("Enter choice: ")

        if choice == "1":
            new_name = input("Enter new name: ")

            if not is_valid_name(new_name):
                print("Name should be at most 15 characters!")
                return

            if new_name in contacts:
                print("⚠️ This name already exists!")
            else:
                contacts[new_name] = contacts[name]
                del contacts[name]
                save_contacts()
                print("Name updated successfully!")

        elif choice == "2":
            new_phone = input("Enter new phone number: ")

            if not is_valid_phone(new_phone):
                print("Phone must be exactly 10 digits!")
                return

            contacts[name] = new_phone
            save_contacts() 
            print("Phone updated successfully!")

        else:
            print("Invalid choice!")

    else:
        print("Contact not found!")
    display_contacts(contacts)

# Display Contacts
def display_contacts(contacts):
    if not contacts:
        print("No contacts found!")
    else:
        print("\nYour Saved Contacts")
        for i, (name, phone) in enumerate(contacts.items(), start=1): 
            print(f"{i}️ {name} : {phone}")


# ─────────────────────────────────────────────────────────────────────────────
# SEARCH ALGORITHMS
# ─────────────────────────────────────────────────────────────────────────────

# Binary Search by Name — O(log n)
# Works by sorting the contact names and repeatedly halving the search space
# until the target is found or the space is exhausted.
def binary_search_by_name(contacts, target):
    sorted_names = sorted(contacts.keys(), key=str.lower)   # sort alphabetically
    low = 0
    high = len(sorted_names) - 1
    target_lower = target.lower()

    while low <= high:
        mid = (low + high) // 2
        mid_name_lower = sorted_names[mid].lower()

        if mid_name_lower == target_lower:
            name = sorted_names[mid]
            return [(name, contacts[name])]         # exact match
        elif mid_name_lower < target_lower:
            low = mid + 1
        else:
            high = mid - 1

    return []   # not found


# Reverse Phone Lookup — O(1) average
# Builds an inverted index {phone: name} so every phone number lookup is instant.
def build_phone_index(contacts):
    return {phone: name for name, phone in contacts.items()}


def search_by_phone(contacts, phone):
    phone_index = build_phone_index(contacts)   # O(n) to build, O(1) lookup
    if phone in phone_index:
        name = phone_index[phone]
        return [(name, contacts[name])]
    return []


# Display search results
def display_results(results):
    if not results:
        print("No contact found!")
    else:
        print("\nSearch Result:")
        for name, phone in results:
            print(f"  {name}  {phone}")


# Search Menu — lets user pick which algorithm to use
def search_contact(contacts):
    if not contacts:
        print("No contacts exist to search!")
        return

    print("\nSearch by:")
    print("  1. Name") # (Binary Search — O(log n))
    print("  2. Phone") #  (Hash Lookup  — O(1))
    method = input("Enter choice: ").strip()

    if method == "1":
        name = input("Enter name to search: ").strip()
        results = binary_search_by_name(contacts, name)
        display_results(results)
    elif method == "2":
        phone = input("Enter phone number to search: ").strip()
        results = search_by_phone(contacts, phone)
        display_results(results)
    else:
        print("Invalid choice!")


# ─────────────────────────────────────────────────────────────────────────────
# MAIN LOOP
# ─────────────────────────────────────────────────────────────────────────────

load_contacts()

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact(contacts)
    elif choice == "2":
        remove_contact(contacts)
    elif choice == "3":
        update_contact(contacts)
    elif choice == "4":
        display_contacts(contacts)
    elif choice == "5":
        search_contact(contacts)
    elif choice == "6":
        print("Exiting... ")
        break
    else:
        print("Invalid choice!")


