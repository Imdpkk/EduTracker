# Edutracker
# A way of know your growth.
def personalized_dashboard():
    name = input("Hello user! Please enter your name!:\n").title()
    print(f'Hello {name}, welcome to the EduTracker')

    print("* Python\n* Java\n* Data Science\n* Web Development\n* Machine Learning\n* Cyber Security\n* Cloud Computing")

    available_courses = ["Python", "Java", "Data Science", "Web Development", "Machine Learning", "Cyber Security", "Cloud Computing"]

    while True:
        course = input("Which course would you like to enroll in?\n").strip().title()
        if course in available_courses:
            print(f'You have selected {course}')
            break
        else:
            print("Invalid course selection. Please choose a course from the available options:")
            print("* Python\n* Java\n* Data Science\n* Web Development\n* Machine Learning\n* Cyber Security\n* Cloud Computing")

    days = int(input("Enter the duration of the course in days:\n"))

    def study_hours_per_day(total_hours, days):
        return total_hours / days

    total_hours = 100
    recommended_hours = study_hours_per_day(total_hours, days)
 
    def get_valid_progress():
        while True:
            try:
                progress = int(input("Enter your course progress (0-100): "))
                if 0 <= progress <= 100:
                    return progress
                else:
                    print("Progress must be between 0 and 100. Try again.")
            except ValueError:
                print("Invalid input! Please enter an integer.")

    progress = get_valid_progress()

    display_dashboard(name, course, progress, recommended_hours)

def display_dashboard(name, course, progress, recommended_hours):
    print(f"\n{'='*30}\nDashboard for {name}\n{'='*30}")
    print(f"Course Enrolled: {course}")
    print(f"Progress: {progress}%")
    print(f"Recommended Study Hours per Day: {recommended_hours:.2f} hours\n")

# here i am Calling  the function
personalized_dashboard()
