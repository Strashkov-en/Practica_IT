import csv
import json


def solve():
    with open('input.csv', mode='r', encoding='utf-8') as f:
        data = list(csv.DictReader(f))

    # Генерируем строку JSON
    output = json.dumps(data, indent=4, ensure_ascii=False)

    # Печатаем БЕЗ лишнего переноса строки в самом конце
    print(output, end='')


if __name__ == "__main__":
    solve()