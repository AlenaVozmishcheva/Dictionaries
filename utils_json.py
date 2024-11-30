import json
import os

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Папка '{directory}' была создана.")
    else:
        print(f"Папка '{directory}' уже существует.")


def load_data_from_json(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Файл {file_name} не найден.")
        return None
    except json.JSONDecodeError:
        print(f"Ошибка декодирования JSON в файле {file_name}.")
        return None


def save_results_to_json(user_name, user_choice, correct_count, incorrect_count, result, directory='results'):
    create_directory(directory)

    results = {
        "Имя": user_name,
        "Уровень сложности": user_choice,
        "Правильные ответы": correct_count,
        "Неправильные ответы": incorrect_count,
        "Уровень знаний": result
    }


    file_name = os.path.join(directory, f"{user_name}_results.json")


    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(results, file, ensure_ascii=False, indent=4)

    print(f"Результаты сохранены в файл {file_name}")