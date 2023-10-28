class MainMenu:

    def run(self):
        print("Welcome to our course selection program!")
        while True:
            command = input("Enter a command:\n")
            if command == "exit":
                print("Goodbye!")
                break
