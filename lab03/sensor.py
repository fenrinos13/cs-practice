# Ввод порога температуры и общего количества записей
threshold = float(input("Введите порог: "))
total_records = int(input("Введите количество записей: "))

error_count = 0

# Цикл для обработки каждой записи
for _ in range(total_records):
    record = input().strip()
    
    if record == "error":
        error_count += 1
    else:
        # Пока просто пропускаем корректные числа, займемся ими в следующем коммите
        pass

# Временный вывод для проверки логики
print(f"Всего записей: {total_records}")
print(f"Ошибок: {error_count}")
