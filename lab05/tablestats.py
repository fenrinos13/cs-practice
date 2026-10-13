def read_rows(lines):
    header = None
    rows = []

    for line in lines:е
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
