from Models.Course import Course

class CourseController:
    allCourses = []

    # TODO : add capacity for courses 

    def addCourse(self,code, title, credit, time, prof):
        # TODO : prevent duplicate course code 
        course = Course(code, title, credit, prof, time)
        self.allCourses.append(course)
        prof.courses.append(course)
        return "course created successfully!"
    
    def pickCourse(self, courseCode, student):
        course = self.findCourseByCode(courseCode)
        if course == None: 
            return "no course with given id!"
        else:
            if student.hasCourse(course):
                return "you already have this course!"
            else:
                student.courses.append(course)
                return "you picked course successfully!"

    def showAllCourses(self):
        result = f"courses count: {len(self.allCourses)} \n"
        result += "\n==================\n"
        for course in self.allCourses: 
            result += str(course)
            result += "\n==================\n"
        return result
    
    def findCourseByCode(self, courseCode):
        for course in self.allCourses: 
            if course.code == courseCode:
                return course 
        return None



