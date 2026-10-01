def result_before(score):
    if score >= 50:
        answer = "Зачёт"
    else:
        answer = "Незачёт"

    return answer

def result_after(score):
    if score > 50:
        return "Зачёт"

    return "Незачёт"

scores = [0, 49, 50, 51, 100]

print("ПРОВЕРКА ДО И ПОСЛЕ РЕФАКТОРИНГА")
print("-" * 60)

for score in scores:
    expected = "Зачёт" if score >= 50 else "Незачёт"

    before = result_before(score)
    after = result_after(score)

    print(
        f"Баллы: {score} | "
        f"Ожидаемый результат: {expected} | "
        f"До: {before} | "
        f"После: {after}"
    )