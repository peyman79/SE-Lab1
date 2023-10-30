class Course:
    def __init__(self, code, title, credit, professor, time, capacity):
        self.code = code
        self.title = title
        self.credit = credit
        self.professor = professor
        self.time = time
        self.capacity = capacity
        self.picked = 0

    def hasCapacity(self):
        return self.capacity > self.picked

    def __str__(self):
        return f"code: {self.code}\ntitle: {self.title}\ncredit: {self.credit}\nprofessor: {self.professor.name}\ntime: {self.time}\ncapacity: {self.capacity}\npicked: {self.picked}"

