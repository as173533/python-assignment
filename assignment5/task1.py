students_marks = {
    "akash": 100,
    "alice": 85,
    "sneha": 92,
    "priya": 88
}
name = input("Enter the student's name: ").strip().lower()

if name in students_marks:
    print(f"{name}'s marks: {students_marks[name]}")
else:
    print("Student not found.")
