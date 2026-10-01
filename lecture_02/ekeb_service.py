# Задание 1
def print_cost(pages):
    if pages < 0:
        raise ValueError("Количество страниц не может быть отрицательным")

    total = pages * 30

    if pages >= 10:
        total = total * 0.9

    return total

# Задание 2
def exam_result(score):
    if score < 0 or score > 100:
        raise ValueError("Недопустимый балл")

    if score >= 50:
        return "Зачёт"

    return "Незачёт"

# Задание 3
class Student:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def has_passed(self):
        return self.score >= 50

    def add_points(self, points):
        if points < 0:
            raise ValueError(
                "Количество баллов не может быть отрицательным"
            )

        self.score = self.score + points

        if self.score > 100:
            self.score = 100

        return self.score

    def status(self):
        if self.score >= 50:
            return "Зачёт"

        return "Незачёт"

# Задание 4
class GrantStudent(Student):

    def status(self):
        if self.score >= 70:
            return "Грант сохранён"

        return "Грант не сохранён"

    def grant_status(self):
        return self.status()