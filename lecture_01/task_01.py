def result_fixed(score):
    if score >= 50:
        return "Зачёт"
    return "Незачёт"

scores = [0, 49, 50, 51, 100]

print("\nПОВТОРНАЯ ПРОВЕРКА ПОСЛЕ ИСПРАВЛЕНИЯ")
print("-" * 60)

for score in scores:
    expected = "Зачёт" if score >= 50 else "Незачёт"
    actual = result_fixed(score)

    status = "Пройдена" if actual == expected else "Не пройдена"

    print(
        f"Баллы: {score} | "
        f"Ожидалось: {expected} | "
        f"Получено: {actual} | "
        f"Статус: {status}"
    )