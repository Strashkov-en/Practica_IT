import json
def calculate_weighted_sum(json_file_path):
    # Открываем и читаем JSON файл
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    total_sum = 0.0

    for item in data:
        score = item.get("score", 0)
        weight = item.get("weight", 0)
        total_sum += score * weight

    result = round(total_sum, 3)
    return result
print(calculate_weighted_sum('input.json'))