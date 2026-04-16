students = {

"Aarav": {"Grade": "A", "Attendance": 92},

"Riya": {"Grade": "B", "Attendance": 85},

"Kabir": {"Grade": "A+", "Attendance": 96}
}
print("Initial Student Records:")
print(students)
students["Sneha"] = {"Grade": "B+", "Attendance": 88}
print("\nAfter Adding Sneha:")
print(students)
students["Riya"]["Grade"] = "A"
print("\nAfter Updating Riya's Grade:")
print(students)
students["Kabir"]["Attendance"] = 98
print("\nAfter Updating Kabir's Attendance:")
print(students)
del students["Aarav"]
print("\nAfter Deleting Aarav:")
print(students)
print("\nFinal Student Records:")
for name, details in students.items():
 print(f"Name: {name}")
 print(f" Grade: {details['Grade']}")
 print(f" Attendance: {details['Attendance']}%")
 print()