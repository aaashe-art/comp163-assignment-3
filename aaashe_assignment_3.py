#information about student (me)

print("Welcome to the Student Life Simulator!")
student_name = "Abraheem Ashe"
current_gpa = 2.2
study_hours = 25
social_points = 65
stress_level = 45

print("Choose your course load:")
print(f"A) Light (12 credits)")  
print(f"B) Standard (15 credits)")
print(f"C) Heavy (18 credits)")

choice = input("Your choice: ")

if choice == "A":
    if current_gpa <= 2.1:
        print("Light load")
    # Use comparison operators to check GPA and adjust variables
elif choice == "B":
    if current_gpa >= 2.1:
        print("Standard load")
    # Different logic path
elif choice == "C":
    if current_gpa >= 3.8:
        print("Heavy load")
    # Heavy load - check if GPA >= 3.5 for different outcomes
else:
    print("Fail")
    # Handle invalid input