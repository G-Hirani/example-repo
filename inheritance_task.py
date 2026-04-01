class Course:
    # Class attribute for the course name
    name = "Fundamentals of Computer Science"

    # Class attribute for the contact website
    contact_website = "www.hyperiondev.com"

    # Class attribute for head office location
    ho_location = "Cape Town"

    # Method to display contact details
    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)
    # Method to print head office location

    def head_office_location(self):
        print(f"Head office is located in {self.ho_location}")


# Example usage:
# Create an instance of the Course class
course = Course()

# Call the contact_details method to display contact information
course.contact_details()
course.head_office_location()

# create subclass OOPCourse
class OOPCourse(Course):
    def __init__(self):
        '''initialise attributes description and trainer'''
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"

    def trainer_details(self):
        '''prints info about course and trainer'''
        print(f"Your trainer for {self.description} is {self.trainer}")

    course_id = "#12345"

    def show_course_id(self):
        '''prints course id'''
        print(f"Your course ID is {self.course_id}")

# create an object in OOPCourse subclass
course1 = OOPCourse()
# call on methods:
course1.contact_details()
course1.trainer_details()
course1.show_course_id()
