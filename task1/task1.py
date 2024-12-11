import sys


def main():
    if len(sys.argv) != 3:
        print("Введите два числа n и m")
        return
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    array = [i + 1 for i in range(n)]
    print(array)
    result_path = ""
    current_index = 0
    start_index = current_index;

    for _ in range(n):
        result_path += str(array[current_index])
        current_index = (current_index + m - 1) % n
        if start_index == current_index:
            break

    print("Полученный путь:", result_path)


if __name__ == "__main__":
    main()