print("1. Add student")
print("2. View students")
print("3. Search student")
print("4. Delete student")

choice = input("Enter option: ")

# ---------------- ADD STUDENT ----------------
if choice == "1":
    roll = input("Enter roll number: ")
    name = input("Enter student name: ")

    duplicate = False
    with open("data.txt", "r") as f:
        for line in f:
            if line.startswith(roll + ","):
                duplicate = True
                break

    if duplicate:
        print("Roll number already exists!")
    else:
        with open("data.txt", "a") as f:
            f.write(roll + "," + name + "\n")
        print("Student saved!")


# ---------------- VIEW STUDENTS ----------------
elif choice == "2":
    with open("data.txt", "r") as f:
        data = f.read()

    print("\nStudents List:\n")
    print(data)


# ---------------- SEARCH STUDENT ----------------
elif choice == "3":
    search_roll = input("Enter roll number to search: ")

    found = False
    with open("data.txt", "r") as f:
        for line in f:
            if line.startswith(search_roll + ","):
                print("Student found:", line)
                found = True
                break

    if not found:
        print("Student not found")


# ---------------- DELETE STUDENT ----------------
elif choice == "4":
    delete_roll = input("Enter roll number to delete: ")

    new_lines = []
    found = False

    with open("data.txt", "r") as f:
        for line in f:
            if not line.startswith(delete_roll + ","):
                new_lines.append(line)
            else:
                found = True

    with open("data.txt", "w") as f:
        f.writelines(new_lines)

    if found:
        print("Student deleted!")
    else:
        print("Roll number not found")


else:
    print("Invalid option")
