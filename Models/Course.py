class Course:
    def __init__(self, code, title, credit, professor, time):
        self.code = code
        self.title = title
        self.credit = credit
        self.professor = professor
        self.time = time

    def __str__(self):
        return f"code: {self.code}\ntitle: {self.title}\ncredit: {self.credit}\nprofessor: {self.professor.name}\ntime: {self.time}"

