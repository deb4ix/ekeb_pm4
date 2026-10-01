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