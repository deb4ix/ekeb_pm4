def print_cost(pages):
    if pages < 0:
        return 0

    total = pages * 30

    if pages > 10:
        total = total * 0.9

    return total