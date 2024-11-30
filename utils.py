def get_user_level(user_choice, my_list_of_questions_and_levels):
    if user_choice == '1':
        words = my_list_of_questions_and_levels[0]['questions'][0]
        print(f"Вы выбрали легкий уровень сложности! Начнем!\n")
        return words
    elif user_choice == '2':
        words = my_list_of_questions_and_levels[0]['questions'][1]
        print(f"Вы выбрали средний уровень сложности! Начнем!\n")
        return words
    elif user_choice == '3':
        words = my_list_of_questions_and_levels[0]['questions'][2]
        print(f"Вы выбрали сложный вариант! Начнем!\n")
        return words
    else:
        words = my_list_of_questions_and_levels[0]['questions'][0]
        print(f"Вы выбрали легкий уровень сложности! Начнем!\n")
        return words


def base_program(level):
    answers = {}
    for key, value in level.items():
        print(f"Перевод слова {key}")
        print(f"слово из {len(value)} и начинается с {value[0].title()}")
        user_answer = input("Ваш ответ: ").strip().lower()

        if user_answer.lower() == value.lower():
            print(f"Верно! {key} - {value}")
            answers[key] = True
        else:
            print(f"Неверно верный ответ - {value}")
            answers[key] = False
    return answers

def get_result(answers, level):
    correct_answers = []
    incorrect_answers = []

    for key in answers:
        if answers[key] is True:
            correct_answers.append(key)
        else:
            incorrect_answers.append(key)

    if correct_answers:
        print(f"Правильно отвеченные слова: ")
        for answer in correct_answers:
            print(answer)
    else:
        print("Нет правильно отвеченных слов")


    if incorrect_answers:
        print(f"Неправильно отвеченные слова: ")
        for answer in incorrect_answers:
            print(answer)
    else:
        print("Неправильно отвеченных слов нет")


    for key, value in level.items():
        if len(correct_answers) == int(key):
            return value


