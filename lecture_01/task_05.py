class Student:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_result(self):
        if self.score >= 50:
            return "Зачёт"

        return "Незачёт"


class GrantStudent(Student):

    def get_result(self):
        if self.score >= 70:
            return "Грант сохранён"

        return "Грант не сохранён"

print("\nПОВТОРНАЯ ПРОВЕРКА ОБЫЧНЫХ СТУДЕНТОВ")
print("-" * 80)

student_scores = [49, 50, 51]

for score in student_scores:

    expected = "Зачёт" if score >= 50 else "Незачёт"

    student = Student("Иван", score)
    actual = student.get_result()

    status = "Пройдена" if actual == expected else "Не пройдена"

    print(
        f"Баллы: {score} | "
        f"Ожидалось: {expected} | "
        f"Получено: {actual} | "
        f"Статус: {status}"
    )

print("\nПОВТОРНАЯ ПРОВЕРКА СТУДЕНТОВ НА ГРАНТЕ")
print("-" * 80)

grant_scores = [69, 70, 71]

for score in grant_scores:

    expected = (
        "Грант сохранён"
        if score >= 70
        else "Грант не сохранён"
    )

    student = GrantStudent("Пётр", score)
    actual = student.get_result()

    status = "Пройдена" if actual == expected else "Не пройдена"

    print(
        f"Баллы: {score} | "
        f"Ожидалось: {expected} | "
        f"Получено: {actual} | "
        f"Статус: {status}"
    )

