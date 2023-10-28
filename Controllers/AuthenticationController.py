from Models.Student import Student


class Authenticator:
    currentUser = None
    allStudents = []
    allProfessors = []

    def studentLogin(self, id):
        pass

    def professorLogin(self, id):
        pass

    def studentRegister(self, id, name):
        self.currentUser = Student(id, name)
        self.allStudents.append(self.currentUser)
        return "successfully registered!"

    def logout(self):
        pass
