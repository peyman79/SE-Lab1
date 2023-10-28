class StudentMenu:
    def __init__(self, authenticator):
        self.authenticator = authenticator

    def run(self):

        print(f"Welcome {self.authenticator.currentUser.name}")
        while True:
            command = input(
                "Enter a command:\n1.Show my info\n2.logout\n")
            if command == "show my info":
                response = self.authenticator.showUserInfo()
                print(response)
            elif command == "logout":
                response = self.authenticator.logout()
                print(response)
                break
