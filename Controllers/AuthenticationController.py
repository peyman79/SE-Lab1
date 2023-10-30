from Models.Professor import Professor
from Models.Student import Student


class Authenticator:
    currentUser = None
    allStudents = []
    allProfessors = []

    def studentLogin(self, id):
        for student in self.allStudents:
            if student.id == id:
                self.currentUser = student
                return "logged in successfully!"
        return "there is no student with this id!"

    def professorLogin(self, id):
        for prof in self.allProfessors:
            if prof.id == id:
                self.currentUser = prof
                return "logged in successfully!"
        return "there is no professor with this id!"

    def studentRegister(self, id, name):
        self.currentUser = Student(id, name)
        self.allStudents.append(self.currentUser)
        return "successfully registered!"

    def professorRegister(self, id, name):
        self.currentUser = Professor(id, name)
        self.allProfessors.append(self.currentUser)
        return "successfully registered!"

    def logout(self):
        self.currentUser = None
        return "logged out!"

    def showUserInfo(self):
        return str(self.currentUser)
