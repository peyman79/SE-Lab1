class Student:
    courses = []

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"id: {self.id}\nname: {self.name}"

    def showAllCourses(self):
        result = f"courses count: {len(self.courses)} \n"
        result += "\n==================\n"
        for course in self.courses: 
            result += str(course)
            result += "\n==================\n"
        return result