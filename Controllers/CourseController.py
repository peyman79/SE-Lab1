from Models.Course import Course

class CourseController:
    allCourses = []

    # TODO : add capacity for courses 

    def addCourse(self,code, title, credit, time, capacity, prof):
        # TODO : prevent duplicate course code 
        course = Course(code, title, credit, prof, time, capacity)
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
        return CourseController.showCourses(self.allCourses)
    
    def findCourseByCode(self, courseCode):
        for course in self.allCourses: 
            if course.code == courseCode:
                return course 
        return None
    
    def showProfCourses(self, profId):
        profCourses = []
        for course in self.allCourses: 
            if course.professor.id == profId:
                profCourses.append(course)
        return CourseController.showCourses(profCourses)

    def showCourses(courses):
        result = f"courses count: {len(courses)} \n"
        result += "\n==================\n"
        for course in courses: 
            result += str(course)
            result += "\n==================\n"
        return result



