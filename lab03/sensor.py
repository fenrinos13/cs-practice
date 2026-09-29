threshold = float(input("Введите порог: "))
total_records = int(input("Введите количество записей: "))

error_count = 0
alarm_count = 0  

for _ in range(total_records):
    record = input().strip()
    
    if record == "error":
        error_count += 1
    else:
        current_temp = float(record)  

        if current_temp > threshold:
            alarm_count += 1

print(f"Всего записей: {total_records}")
print(f"Ошибок: {error_count}")
print(f"Превышений порога: {alarm_count}")

