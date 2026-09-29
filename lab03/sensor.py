threshold = float(input())
total_records = int(input())

error_count = 0
alarm_count = 0
correct_count = 0
temperature_sum = 0.0
max_temperature = None

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
            
        if max_temperature is None or current_temp > max_temperature:
            max_temperature = current_temp

if correct_count > 0:
    average_temperature = temperature_sum / correct_count
else:
    average_temperature = 0.0


print(total_records)
print(error_count)
print(alarm_count)
print(f"{max_temperature:.1f}")
print(f"{average_temperature:.1f}")
