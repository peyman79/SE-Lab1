class Student:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.courses = []

    def __str__(self):
        return f"id: {self.id}\nname: {self.name}"

    def showAllCourses(self):
        result = f"courses count: {len(self.courses)} \n"
        result += "\n==================\n"
        for course in self.courses: 
            result += str(course)
            result += "\n==================\n"
        return result
    
    def hasCourse(self, course):
        for c in self.courses:
            if c.code == course.code: 
                return True 
        return False