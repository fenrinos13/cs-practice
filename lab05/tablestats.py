def read_rows(lines):
    header = None
    rows = []

    for line in lines:
        line = line.rstrip('\r\n')
        if not line:
            continue
        fields = [field.strip() for field in line.split(',')]

        if header is None:
            header = fields
            continue
        if len(fields) != len(header):
            continue

        row_dict = {}
        for i in range(len(header)):
            row_dict[header[i]] = fields[i]
        rows.append(row_dict)

    return rows

def count_types(rows):
    counts = {}
    for row in rows:
        kind = row.get('тип')
        if kind:
            counts[kind] = counts.get(kind, 0) + 1
    return counts

def total_minutes(rows, kind):
    total = 0.0
    has_kind = False
for row in rows:
        if row.get('тип') == kind:
            has_kind = True
            minutes_str = row.get('минуты', '')
            minutes_str = minutes_str.replace(',', '.')
            try:
                total += float(minutes_str)
            except ValueError:
                continue
    if not has_kind:
        return 0.0
    return round(total, 1)

def to_csv(counts):
    result = "тип,количество\n"
    for kind in sorted(counts.keys()):
        result += f"{kind},{counts[kind]}\n"
    return result
