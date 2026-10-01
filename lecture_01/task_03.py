def purchase_fixed(price, quantity):
    return price * quantity

print("\nПОВТОРНАЯ ПРОВЕРКА ПОСЛЕ ИСПРАВЛЕНИЯ")
print("-" * 60)

result = purchase_fixed(700, 2)

expected = 1400

print("Ожидаемый результат:", expected)
print("Полученный результат:", result)

if result == expected:
    print("Статус: Пройдена")
else:
    print("Статус: Не пройдена")

balance = 5000 - purchase_fixed(700, 2)

print("\nСтоимость покупки:", purchase_fixed(700, 2))
print("Остаток:", balance)