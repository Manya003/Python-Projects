# Contact Book

def menu():
    print("\n📒✨ --- Contact Book --- ✨📒")
    print("1️⃣  Add Contact ")
    print("2️⃣  Remove Contact ")
    print("3️⃣  Update Contact ")
    print("4️⃣  Display Contacts ")
    print("5️⃣  Exit ")
 
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
        print("❌ Name should be at most 15 characters!")
        return

    phone = input("Enter phone number: ")

    if not is_valid_phone(phone):
        print("❌ Phone number must be exactly 10 digits!")
        return
    
    if name in contacts:
        print("⚠️ Contact already exists!")
    else:
        contacts[name] = phone
        print("✅ Contact added successfully!")

contacts = {}

# Remove Contact
def remove_contact(contacts):
    name = input("Enter name to remove: ")
    
    if name in contacts:
        del contacts[name]
        print("Contact removed!")
    else:
        print("Contact not found!")

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
                print("❌ Name should be at most 15 characters!")
                return

            if new_name in contacts:
                print("⚠️ This name already exists!")
            else:
                contacts[new_name] = contacts[name]
                del contacts[name]
                print("✅ Name updated successfully!")

        elif choice == "2":
            new_phone = input("Enter new phone number: ")

            if not is_valid_phone(new_phone):
                print("❌ Phone must be exactly 10 digits!")
                return

            contacts[name] = new_phone
            print("✅ Phone updated successfully!")

        else:
            print("❌ Invalid choice!")

    else:
        print("❌ Contact not found!")

# Display Contacts
def display_contacts(contacts):
    if not contacts:
        print("No contacts found!")
    else:
        print("\nYour Saved Contacts 👤✨")
        for i, (name, phone) in enumerate(contacts.items(), start=1): 
            print(f"{i}️⃣  {name} 📞 : {phone}")

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
        print("Exiting...")
        break
    else:
        print("Invalid choice!")

