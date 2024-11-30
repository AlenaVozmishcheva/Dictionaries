from utils import get_user_level, base_program, get_result
from utils_json import load_data_from_json, save_results_to_json


def main():
    data = load_data_from_json("questions.json")
    answers = {}
    words = {}

    if data:
        my_list_of_questions_and_levels = data

        user_name = input("Введите ваше имя: ").strip().title()

        user_choice = input("Выберите уровень сложности:\n1 - легкий\n2 - средний\n3 - сложный\n").strip().lower()

        user_level = get_user_level(user_choice, my_list_of_questions_and_levels)

        test_words = base_program(user_level)

        test_answers = my_list_of_questions_and_levels[1]['levels']

        result = get_result(test_words, test_answers)
        print(f'Ваш уровень знаний: {result}')


        correct_count = len([key for key in test_words if test_words[key] is True])
        incorrect_count = len([key for key in test_words if test_words[key] is False])
        save_results_to_json(user_name,user_choice, correct_count, incorrect_count, result, directory='results')

if __name__ == "__main__":
    main()