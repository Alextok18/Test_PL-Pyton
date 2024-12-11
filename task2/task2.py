import sys
import math

if len(sys.argv) < 3:
    print("Укажите имена двух файлов.")
    sys.exit(1)

center_file = sys.argv[1]
points_file = sys.argv[2]

try:
    with open(center_file, 'r') as file:
        center_data = file.readlines()
        center_x, center_y = map(float, center_data[0].split())
        radius = float(center_data[1].strip())

    with open(points_file, 'r') as file:
        points = file.readlines()

    results = []

    for line in points:
        try:
            point_x, point_y = map(float, line.split())

            distance = math.sqrt((point_x - center_x) ** 2 + (point_y - center_y) ** 2)

            if distance < radius:
                results.append("1")  # Внутри
            elif distance == radius:
                results.append("0")  # На
            else:
                results.append("2")  # Вне
        except ValueError:
            print(f"Ошибка в строке '{line.strip()}'")

    for result in results:
        print(result)
except FileNotFoundError:
    print("Файл не найден.")
except ValueError:
    print("Некорректные данные.")
