def print_cost_before(pages):
    total = pages * 30

    if pages >= 10:
        total = total * 0.9

    return total

def print_cost_after(pages):
    if pages >= 10:
        return pages * 30 - 0.1

    return pages * 30

pages_list = [0, 1, 9, 10, 11, 20]

print("ПРОВЕРКА ДО И ПОСЛЕ РЕФАКТОРИНГА")
print("-" * 80)

for pages in pages_list:

    if pages >= 10:
        expected = pages * 30 * 0.9
    else:
        expected = pages * 30

    before = print_cost_before(pages)
    after = print_cost_after(pages)

    print(
        f"Страниц: {pages} | "
        f"Ожидаемый результат: {expected} | "
        f"До: {before} | "
        f"После: {after}"
    )