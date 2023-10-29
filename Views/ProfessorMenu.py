class ProfessorMenu:
    def __init__(self, authenticator, courseController):
        self.authenticator = authenticator
        self.courseController = courseController

    def run(self):

        print(f"Welcome {self.authenticator.currentUser.name}")
        while True:
            command = input(
                "Enter a command:\n1.show my info\n2.logout\n3.new course\n4.all courses\n5.my courses\n6.edit course time \n")
            if command == "show my info":
                response = self.authenticator.showUserInfo()
                print(response)
            elif command == "new course":
                code = input("code: ")
                title = input("title: ")
                credit = int(input("credit: "))
                time = input("time (e.g. 13:30-15): ")
                capacity = int(input("capacity: "))
                prof = self.authenticator.currentUser
                response = self.courseController.addCourse(code, title, credit, time, capacity, prof)
                print(response)
            elif command == "all courses": 
                response = self.courseController.showAllCourses()
                print(response)
            elif command == "my courses": 
                prof = self.authenticator.currentUser
                response = prof.showAllCourses()
                print(response)
            elif command == "edit course time":
                courseCode = input("course code: ")
                newTime = input("new time (e.g. 13:30-15): ")
                response = self.courseController.editCourseTime(courseCode, newTime)
                print(response)
            elif command == "logout":
                response = self.authenticator.logout()
                print(response)
                break
