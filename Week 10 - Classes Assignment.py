import re  # Import regular expressions for input validation

# Validator class to check each piece of input
class Validator:
    @staticmethod
    def valid_name(name):
        # Name must only have letters and spaces
        return bool(re.fullmatch(r"[A-Za-z\s]+", name))

    @staticmethod
    def valid_email(email):
        # Email must be alphanumeric with @ and .
        return bool(re.fullmatch(r"[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", email))

    @staticmethod
    def valid_student_id(sid):
        # Student ID must be digits only, max 7 digits
        return sid.isdigit() and len(sid) <= 7

    @staticmethod
    def valid_instructor_id(iid):
        # Instructor ID must be digits only, max 5 digits
        return iid.isdigit() and len(iid) <= 5

# Person class for shared info (name and email)
class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def displayInformation(self):
        print("Name:", self.name)
        print("Email:", self.email)

# Student class inherits from Person and adds ID and program
class Student(Person):
    def __init__(self, name, email, student_id, program):
        super().__init__(name, email)
        self.student_id = student_id
        self.program = program

    def displayInformation(self):
        super().displayInformation()
        print("Student ID:", self.student_id)
        print("Program of Study:", self.program)

# Instructor class inherits from Person and adds ID, school, and degree
class Instructor(Person):
    def __init__(self, name, email, instructor_id, school, degree):
        super().__init__(name, email)
        self.instructor_id = instructor_id
        self.school = school
        self.degree = degree

    def displayInformation(self):
        super().displayInformation()
        print("Instructor ID:", self.instructor_id)
        print("Graduated From:", self.school)
        print("Highest Degree:", self.degree)

# Main list to hold all student and instructor records
college_records = []

# Add a preloaded student example as required
college_records.append(Student(
    name="Furhaan Khan",
    email="khanonball24@gmail.com",
    student_id="8852000",
    program="Cybersecurity"
))

# Loop for collecting more user input
while True:
    role = input("Is this person a student or instructor? ").strip().lower()
    while role not in ["student", "instructor"]:
        role = input("Please enter 'student' or 'instructor': ").strip().lower()

    name = input("Enter name: ").strip()
    while not Validator.valid_name(name):
        print("Invalid name. Try again.")
        name = input("Enter name: ").strip()

    email = input("Enter email: ").strip()
    while not Validator.valid_email(email):
        print("Invalid email. Try again.")
        email = input("Enter email: ").strip()

    if role == "student":
        sid = input("Enter student ID (up to 7 digits): ").strip()
        while not Validator.valid_student_id(sid):
            print("Invalid student ID. Try again.")
            sid = input("Enter student ID: ").strip()

        program = input("Enter program of study: ").strip()
        while not program:
            print("Program of study is required.")
            program = input("Enter program of study: ").strip()

        college_records.append(Student(name, email, sid, program))

    else:  # instructor
        iid = input("Enter instructor ID (up to 5 digits): ").strip()
        while not Validator.valid_instructor_id(iid):
            print("Invalid instructor ID. Try again.")
            iid = input("Enter instructor ID: ").strip()

        school = input("Enter last institution graduated from: ").strip()
        while not school:
            print("Institution is required.")
            school = input("Enter last institution graduated from: ").strip()

        degree = input("Enter highest degree earned: ").strip()
        while not degree:
            print("Degree is required.")
            degree = input("Enter highest degree earned: ").strip()

        college_records.append(Instructor(name, email, iid, school, degree))

    # Ask if the user wants to continue
    another = input("Would you like to enter another person? (yes/no): ").strip().lower()
    if another != "yes":
        break

# Print all records collected
print("\n--- All College Records ---\n")
for person in college_records:
    person.displayInformation()
    print("-" * 30)
