# Student Registration System

from datetime import datetime

students = []
MAX_SEATS = 100
deadline = datetime(2026, 3, 25, 23, 59)


# Load data from file
def load_data():
    try:
        with open("students.txt", "r") as file:
            for line in file:
                name, course, sid = line.strip().split(",")
                students.append({
                    "id": int(sid),
                    "name": name,
                    "course": course
                })
    except:
        pass


# Save data to file
def save_data():
    with open("students.txt", "w") as file:
        for s in students:
            file.write(f"{s['name']},{s['course']},{s['id']}\n")


# Generate ID
def generate_id():
    if not students:
        return 1
    return students[-1]["id"] + 1


# Menu
def menu():
    print("\n" + "="*45)
    print("🎓 Student Registration System 🎓")
    print("="*45)
    print("1️⃣ Register Student ")
    print("2️⃣ View Students ")
    print("3️⃣ Search Student ")
    print("4️⃣ Remove Student ")
    print("5️⃣ Exit ")


# Register
def register_student():
    if datetime.now() > deadline:
        print("⛔ Deadline passed!")
        return

    if len(students) >= MAX_SEATS:
        print("🚫 Seats full!")
        return

    name = input("👤 Enter name: ").strip()
    course = input("📚 Enter course: ").upper().strip()

    if course != "MCA":
        print("❌ Only MCA allowed!")
        return

    student = {
        "id": generate_id(),
        "name": name,
        "course": course
    }

    students.append(student)
    save_data()

    print(f"✅ Registered! Your ID: {student['id']} 🎉")


# View
def view_students():
    if not students:
        print("No students found!")
    else:
        print("\n📋 Student List")
        for s in students:
            print(f"🆔 {s['id']} | {s['name']} | {s['course']}")


# Search
def search_student():
    sid = int(input("Enter student ID to search: "))

    for s in students:
        if s["id"] == sid:
            print(f"✅ Found: {s['name']} ({s['course']})")
            return

    print("❌ Student not found!")


# Remove
def remove_student():
    sid = int(input("Enter student ID to remove: "))

    for s in students:
        if s["id"] == sid:
            students.remove(s)
            save_data() 
            print("✅ Student removed!")
            return
 
    print("❌ Student not found!")


# Main
load_data()

while True:
    menu()
    choice = input("👉 Enter choice: ")

    if choice == "1":
        register_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        remove_student()

    elif choice == "5":
        print("👋 Exiting...")
        break

    else:
        print("❌ Invalid choice!")