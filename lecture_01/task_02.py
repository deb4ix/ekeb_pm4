def print_cost_fixed(pages):
    if pages >= 10:
        return pages * 30 * 0.9

    return pages * 30

pages_list = [0, 1, 9, 10, 11, 20]

print("\nПОВТОРНАЯ ПРОВЕРКА ПОСЛЕ ИСПРАВЛЕНИЯ")
print("-" * 80)

for pages in pages_list:

    if pages >= 10:
        expected = pages * 30 * 0.9
    else:
        expected = pages * 30

    actual = print_cost_fixed(pages)

    status = "Пройдена" if actual == expected else "Не пройдена"

    print(
        f"Страниц: {pages} | "
        f"Ожидалось: {expected} | "
        f"Получено: {actual} | "
        f"Статус: {status}"
    )