# Information about student
print("Welcome to the Student Life Simulator!")

student_name = "Abraheem Ashe"
current_gpa = 3.0
study_hours = 25
social_points = 65
stress_level = 45

print("Choose your course load:")
print("A) Light (12 credits)")
print("B) Standard (15 credits)")
print("C) Heavy (18 credits)")

choice = input("Your choice: ")

if choice == "A":  # Light load
    if current_gpa <= 2.1:
        study_hours += 5    # Extra time because course load is light
        stress_level -= 10  # Less stress
        print("Light load")
    else:
        study_hours += 2
        stress_level -= 5
elif choice == "B":  # Standard load
    if current_gpa >= 2.1 and current_gpa < 3.5:
        study_hours -= 2    # Slightly more work
        stress_level += 5   # Slight stress increase
        print("Standard load ")
    else:
        study_hours -= 1
        stress_level += 3
elif choice == "C":  # Heavy load
    if current_gpa >= 3.8:
        study_hours -= 5    # More time needed
        stress_level += 10  # High stress
        print("Heavy load")
    else:
        study_hours -= 3
        stress_level += 7
else:
    print("Invalid choice!")

print(f"Current study hours: {study_hours}, stress level: {stress_level}")

# Study options
study_options = ["Programming", "Math", "English", "History"]

user_choice = input("Choose a subject to study (Programming, Math, English, History): ")

if user_choice in study_options:
    if user_choice in ["Programming", "Math"] and current_gpa < 3.5:
        # Harder subjects slightly improve GPA more but increase stress
        if user_choice == "Programming":
            current_gpa += 0.3
            study_hours -= 5
            stress_level += 10
        elif user_choice == "Math":
            current_gpa += 0.2
            study_hours -= 4
            stress_level += 8
    elif user_choice in ["English", "History"] or current_gpa >= 3.5:
        # Easier subjects or high GPA -> smaller impact
        if user_choice == "English":
            current_gpa += 0.1
            study_hours -= 3
            stress_level += 5
        elif user_choice == "History":
            current_gpa += 0.15
            study_hours -= 2
            stress_level += 6

    print(f"After studying {user_choice}, your GPA is now {current_gpa:.2f}, study hours left: {study_hours}, stress level: {stress_level}")

elif user_choice not in study_options:
    print(f"{user_choice} is not a valid study option. Please choose from: {study_options}")