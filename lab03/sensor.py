threshold = float(input("Введите порог: "))
total_records = int(input("Введите количество записей: "))

error_count = 0
alarm_count = 0
correct_count = 0       # Количество успешных измерений
temperature_sum = 0.0   # Сумма для расчета среднего
max_temperature = None  # Инициализируем None, чтобы корректно работал минус

for _ in range(total_records):
    record = input().strip()
    
    if record == "error":
        error_count += 1
    else:
        current_temp = float(record)
        correct_count += 1
        temperature_sum += current_temp
        
        if current_temp > threshold:
            alarm_count += 1
            
        # Поиск максимальной температуры
        if max_temperature is None or current_temp > max_temperature:
            max_temperature = current_temp

# Считаем среднее (из условия знаем, что хотя бы одно число верное, но делаем проверку)
if correct_count > 0:
    average_temperature = temperature_sum / correct_count
else:
    average_temperature = 0.0

print(f"Всего: {total_records}")
print(f"Ошибок: {error_count}")
print(f"Превышений: {alarm_count}")
print(f"Максимум: {max_temperature}")
print(f"Среднее: {average_temperature}")
