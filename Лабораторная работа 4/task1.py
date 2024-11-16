import json

file_input = "input.json"


def task() -> float:
    with open(file_input, 'r') as file:
        json_file = json.load(file)
        multiplication = [item["weight"] * item["score"] for item in json_file]
        result = sum(multiplication)
    return round(result, 3)


if __name__ == '__main__':
    print(task())
