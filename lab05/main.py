import tablestats

def main():
    filename = input().strip()
    with open(filename, "r", encoding="utf-8") as table:
        lines = table.readlines()
    rows = tablestats.read_rows(lines)
    counts = tablestats.count_types(rows)
    error_minutes = tablestats.total_minutes(rows, "ошибка")
    print(len(rows))
    print(len(counts))
    print(error_minutes)
    summary_csv = tablestats.to_csv(counts)
    with open("summary.csv", "w", encoding="utf-8") as out:
        out.write(summary_csv)
if __name__ == "__main__":
    main()
