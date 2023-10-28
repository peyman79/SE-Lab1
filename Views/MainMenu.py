from Controllers.AuthenticationController import Authenticator
from Views.StudentMenu import StudentMenu


class MainMenu:

    def run(self):
        authenticator = Authenticator()
        print("Welcome to our course selection program!")
        while True:
            command = input(
                "Enter a command:\n1.register student\n2.register professor\n3.login student\n4.login "
                "professor\n")
            if command == "register student":
                id = input("id: ")
                name = input("name: ")
                response = authenticator.studentRegister(id, name)
                print(response)
                StudentMenu(authenticator).run()
            elif command == "register professor":
                id = input("id: ")
                name = input("name: ")
                response = authenticator.professorRegister(id, name)
                print(response)
            elif command == "login student":
                id = input("id: ")
                response = authenticator.studentLogin(id)
                print(response)
                StudentMenu().run()
            elif command == "login professor":
                id = input("id: ")
                response = authenticator.professorLogin(id)
                print(response)
            elif command == "exit":
                print("Goodbye!")
                break
