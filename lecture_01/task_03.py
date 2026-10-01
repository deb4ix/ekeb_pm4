def purchase_before(price, quantity):
    return price * quantity

def purchase_after(price, quantity):
    print(price * quantity)


print("ПРОВЕРКА ДО И ПОСЛЕ РЕФАКТОРИНГА")
print("-" * 60)

old_result = purchase_before(700, 2)
new_result = purchase_after(700, 2)

print("Старая версия вернула:", old_result)
print("Новая версия вернула:", new_result)