import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    with open(INPUT_FILENAME, 'r') as input_file:
        csv_file = csv.DictReader(input_file)
        rows = list(csv_file)

    with open(OUTPUT_FILENAME, 'w') as output:
        output.write(json.dumps(rows, indent=4))

if __name__ == '__main__':
    # Нужно для проверки
    task()
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
