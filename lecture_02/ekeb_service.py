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
        return self.score > 50

    def add_points(self, points):
        self.score = self.score + points
        return self.score