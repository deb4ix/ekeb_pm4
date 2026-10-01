class StudentBefore:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_result(self):
        if self.score >= 50:
            return "Зачёт"

        return "Незачёт"


class GrantStudentBefore(StudentBefore):

    def get_result(self):
        if self.score >= 70:
            return "Грант сохранён"

        return "Грант не сохранён"


class StudentAfter:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_result(self):
        if self.score > 50:
            return "Зачёт"

        return "Незачёт"

class GrantStudentAfter(StudentAfter):
    pass


print("ПРОВЕРКА ОБЫЧНЫХ СТУДЕНТОВ")
print("-" * 80)

student_scores = [49, 50, 51]

for score in student_scores:

    expected = "Зачёт" if score >= 50 else "Незачёт"

    before = StudentBefore("Иван", score).get_result()
    after = StudentAfter("Иван", score).get_result()

    print(
        f"Баллы: {score} | "
        f"Ожидалось: {expected} | "
        f"До: {before} | "
        f"После: {after}"
    )


print("\nПРОВЕРКА СТУДЕНТОВ НА ГРАНТЕ")
print("-" * 80)

grant_scores = [69, 70, 71]

for score in grant_scores:

    expected = (
        "Грант сохранён"
        if score >= 70
        else "Грант не сохранён"
    )

    before = GrantStudentBefore("Пётр", score).get_result()
    after = GrantStudentAfter("Пётр", score).get_result()

    print(
        f"Баллы: {score} | "
        f"Ожидалось: {expected} | "
        f"До: {before} | "
        f"После: {after}"
    )
