class Professor:
    courses = []

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"id: {self.id}\nname: {self.name}"

    def showAllCourses(self):
        pass
