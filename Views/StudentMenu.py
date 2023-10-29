class StudentMenu:
    def __init__(self, authenticator, courseController):
        self.authenticator = authenticator
        self.courseController = courseController

    def run(self):

        # TODO : show one prof courses 
        print(f"Welcome {self.authenticator.currentUser.name}")
        while True:
            command = input(
                "Enter a command:\n1.show my info\n2.logout\n3.pick course\n4.my courses\n5.all courses\n6.show prof courses \n")
            if command == "show my info":
                response = self.authenticator.showUserInfo()
                print(response)
            elif command == "pick course":
                courseCode = input("course code: ")
                response = self.courseController.pickCourse(courseCode, self.authenticator.currentUser)
                print(response)
            elif command == "my courses":
                student = self.authenticator.currentUser
                response = student.showAllCourses()
                print(response)
            elif command == "all courses": 
                response = self.courseController.showAllCourses()
                print(response)
            elif command == "show prof courses": 
                profId = input("prof id: ")
                response = self.courseController.showProfCourses(profId)
                print(response)
            elif command == "logout":
                response = self.authenticator.logout()
                print(response)
                break
