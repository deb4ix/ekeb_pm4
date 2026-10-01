def fine_fixed(days):
    if days < 0:
        return "Ошибка"

    if days <= 3:
        return 0

    return (days - 3) * 100

days_list = [-1, 0, 3, 4, 7, 10]

print("\nПОВТОРНАЯ ПРОВЕРКА ПОСЛЕ ИСПРАВЛЕНИЯ")
print("-" * 90)

for days in days_list:

    if days < 0:
        expected = "Ошибка"
    elif days <= 3:
        expected = 0
    else:
        expected = (days - 3) * 100

    actual = fine_fixed(days)

    status = "Пройдена" if actual == expected else "Не пройдена"

    print(
        f"Дни: {days} | "
        f"Ожидалось: {expected} | "
        f"Получено: {actual} | "
        f"Статус: {status}"
    )