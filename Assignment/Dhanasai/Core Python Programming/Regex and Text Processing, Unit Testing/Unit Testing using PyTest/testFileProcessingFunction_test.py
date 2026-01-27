import pytest
import csv
def count_csv_rows(file_path):
    try:
        with open(file_path, "r", newline="") as f:
            reader = csv.reader(f)
            rows = list(reader)
            return len(rows)
    except FileNotFoundError:
        raise ValueError("File not found")
def test_count_csv_rows(tmp_path):
    temp_file = tmp_path / "test.csv"
    with open(temp_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age"])
        writer.writerow(["Alice", 30])
        writer.writerow(["Bob", 25])
    row_count = count_csv_rows(temp_file)
    assert row_count == 3
