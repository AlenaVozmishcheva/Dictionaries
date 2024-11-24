words_easy = {
    'family': 'семья',
    'minute': 'минута',
    'hand': 'рука',
    'people': 'люди',
    'evening': 'вечер',
}

words_medium = {
    'understand': 'понимать',
    'believe': 'верить',
    'feel': 'чувствовать',
    'close': 'закрывать',
    'choice': 'выбирать',
}

words_hard = {
    'rural': 'деревенский',
    'fortune': 'удача',
    'exercise': 'упражнение',
    'suggest': 'предлагать',
    'except': 'кроме',
}

levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично"
}

answers = {}

user_choice = input("Выберите уровень сложности:\n1 - легкий\n2 - средний\n3 - сложный\n").strip().lower()

if user_choice == '1':
    words = words_easy
elif user_choice == '2':
    words = words_medium
elif user_choice == '3':
    words = words_hard
else:
    words = words_easy

correct = 0

for english_word, russian_word in words.items():
    print(f"Перевод слова {english_word}")
    print(f"слово из {len(russian_word)} и начинается с {russian_word[0].title()}")
    user_answer = input("Ваш ответ: ")

    if user_answer.lower() == russian_word.lower():
        print(f"Верно! {english_word} - {russian_word}")
        correct += 1
        answers[english_word] = True
    else:
        print(f"Неверно верный ответ - {russian_word}")
        answers[english_word] = False

for word, answer in answers.items():
    if answer is True:
        print(f"Верно: {word}")
    else:
        print(f'Неверно: {word}')

for english_word, key in answers.items():
    if answers[english_word] is True:
        print(f"Правильно отвеченные слова: {english_word}")
    else:
        print(f"Неверно отвеченные слова: {english_word}")

print(f"Ваш ранг: {levels[correct]}")







