def fine_before(days):
    if days < 0:
        return "Ошибка"

    elif days <= 3:
        return 0

    else:
        return (days - 3) * 100

def fine_after(days):
    if days <= 3:
        return 0

    return days * 100

days_list = [-1, 0, 3, 4, 7, 10]

print("ПРОВЕРКА ДО И ПОСЛЕ РЕФАКТОРИНГА")
print("-" * 90)

for days in days_list:

    if days < 0:
        expected = "Ошибка"
    elif days <= 3:
        expected = 0
    else:
        expected = (days - 3) * 100

    before = fine_before(days)
    after = fine_after(days)

    print(
        f"Дни: {days} | "
        f"Ожидаемый результат: {expected} | "
        f"До: {before} | "
        f"После: {after}"
    )