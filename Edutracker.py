import json

DATA_FILE = "edutracker_data.json"

# ------------------- Data Loading and Saving -------------------

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# ------------------- Main Dashboard -------------------

def personalized_dashboard():
    data = load_data()

    name = input("Hello user! Please enter your name:\n").title()

    if name in data:
        print(f"\nWelcome back {name}! Loading your previous progress...\n")
        user_data = data[name]
        display_dashboard(name, user_data["course"], user_data["progress"], user_data["recommended_hours"])
        return
    
    print(f'Hello {name}, welcome to EduTracker!\n')

    available_courses = [
        "Python", "Java", "Data Science", "Web Development",
        "Machine Learning", "Cyber Security", "Cloud Computing"
    ]

    print("\nAvailable Courses:")
    for course in available_courses:
        print(f"* {course}")

    while True:
        course = input("\nWhich course would you like to enroll in?\n").strip().title()
        if course in available_courses:
            print(f"You have selected {course}")
            break
        else:
            print("\nInvalid selection! Choose from the available courses.")

    # Course duration
    while True:
        try:
            days = int(input("Enter the duration of the course in days:\n"))
            break
        except ValueError:
            print("Please enter a valid number of days!")

    # Study hours calculation
    total_hours = 100
    recommended_hours = total_hours / days

    # Progress validation
    progress = get_valid_progress()

    # Save data for multi-user support
    data[name] = {
        "course": course,
        "progress": progress,
        "recommended_hours": recommended_hours
    }

    save_data(data)
    print("\nYour progress has been saved successfully!")
    display_dashboard(name, course, progress, recommended_hours)

# ------------------- Progress Validation -------------------

def get_valid_progress():
    while True:
        try:
            progress = int(input("Enter your course progress (0-100): "))
            if 0 <= progress <= 100:
                return progress
            else:
                print("Progress must be between 0 and 100!")
        except ValueError:
            print("Invalid input! Enter a valid number.")

# ------------------- Dashboard Display -------------------

def display_dashboard(name, course, progress, recommended_hours):
    print(f"\n{'='*35}")
    print(f"📘 Dashboard for {name}")
    print(f"{'='*35}")
    print(f"Course Enrolled: {course}")
    print(f"Progress: {progress}%")
    print(f"Recommended Study Hours/Day: {recommended_hours:.2f} hours")
    print("="*35)

# ------------------- Start App -------------------

personalized_dashboard()
