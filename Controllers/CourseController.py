from Models.Course import Course

class CourseController:
    allCourses = []

    def addCourse(self,code, title, credit, time, prof):
        course = Course(code, title, credit, prof, time)
        self.allCourses.append(course)
        prof.courses.append(course)
        return "course created successfully!"

    def showAllCourses(self):
        result = f"courses count: {len(self.allCourses)} \n"
        result += "\n==================\n"
        for course in self.allCourses: 
            result += str(course)
            result += "\n==================\n"
        return result


