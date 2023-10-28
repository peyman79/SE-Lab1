from Controllers.AuthenticationController import Authenticator


class MainMenu:

    def run(self):
        authenticator = Authenticator()
        print("Welcome to our course selection program!")
        while True:
            command = input("Enter a command:\n1.register student\n2.register professor\n")
            if command == "register student":
                id = input("id: ")
                name = input("name: ")
                response = authenticator.studentRegister(id, name)
                print(response)
            elif command == "register professor":
                id = input("id: ")
                name = input("name: ")
                response = authenticator.professorRegister(id, name)
                print(response)
            elif command == "exit":
                print("Goodbye!")
                break
