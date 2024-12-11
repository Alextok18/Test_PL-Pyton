import json
import sys

def update_values(tests, values):
    if "id" in tests and tests["id"] in values:
        tests["value"] = values[tests["id"]]

    for key in ["values", "tests"]:
        if key in tests:
            for item in tests[key]:
                update_values(item, values)

def load_values(values_data):
    values_dict = {}
    for item in values_data.get("values", []):
        values_dict[item["id"]] = item["value"]
    return values_dict

def main():
    if len(sys.argv) != 4:
        print("Ошибка: укажите файлы tests.json, values.json и report.json.")
        return

    tests_file = sys.argv[1]
    values_file = sys.argv[2]
    report_file = sys.argv[3]

    try:
        with open(tests_file, "r", encoding="utf-8") as f:
            tests_data = json.load(f)

        with open(values_file, "r", encoding="utf-8") as f:
            values_data = json.load(f)

        values_dict = load_values(values_data)

        update_values(tests_data, values_dict)

        with open(report_file, "w", encoding="utf-8") as f:
            json.dump(tests_data, f, ensure_ascii=False, indent=4)

        print("Файл успешно сохранён:", report_file)
    except FileNotFoundError:
        print("Ошибка: файл не найден.")
    except json.JSONDecodeError:
        print("Ошибка: некорректный JSON.")
    except Exception as e:
        print("Ошибка:", e)

if __name__ == "__main__":
    main()
