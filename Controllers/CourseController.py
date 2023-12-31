from Models.Course import Course

class CourseController:
    allCourses = []


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
                if course.hasCapacity():
                    student.courses.append(course)
                    course.picked += 1
                    return f"you picked course successfully!\nyour total credit: {student.getTotalCredit()}"
                else: 
                    return "this course capacity is full!"
    def dropCourse(self, courseCode, student):
        course = self.findCourseByCode(courseCode)
        if course == None: 
            return "no course with given id!"
        else:
            if student.hasCourse(course):
                student.courses.remove(course)
                course.picked -= 1
                return f"course dropped successfully!\nyour total credit: {student.getTotalCredit()}"
            else:
                return "you don't have this course!"

    def showAllCourses(self):
        return CourseController.showCourses(self.allCourses)
    
    def showAvailableCourses(self, student):
        availableCourses = []
        for course in self.allCourses:
            if course.hasCapacity() and course not in student.courses:
                availableCourses.append(course)
        return CourseController.showCourses(availableCourses)
    
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
    
    def editCourseTime(self, courseCode, newTime):
        course = self.findCourseByCode(courseCode)
        if course == None: 
            return "no course with given id!"
        else:
            course.time = newTime
            return "course time edited successfulley!"


    def showCourse(self, code):
        for course in self.allCourses:
            if course.code == code:
                return str(course)

    def showCourses(courses):
        result = f"courses count: {len(courses)} \n"
        result += "\n==================\n"
        for course in courses: 
            result += str(course)
            result += "\n==================\n"
        return result



