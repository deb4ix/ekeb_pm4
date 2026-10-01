def print_cost(pages):
    if pages < 0:
        raise ValueError("Количество страниц не может быть отрицательным")

    total = pages * 30

    if pages >= 10:
        total = total * 0.9

    return total