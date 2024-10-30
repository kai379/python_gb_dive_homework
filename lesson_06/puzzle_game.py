from random import choice


_attempts_story = {}


def story_log(desc_var: str, user_attempts: int):
    _attempts_story.setdefault(desc_var, [])
    _attempts_story[desc_var].append(user_attempts)


def puzzle(description: str, answer: list[str], number_of_attempts: int) -> int:
    print('Угадайте загадку')
    print(description)
    attempt = 1
    user_answer = input('Введите свой вариант: ')
    answer = list(map(lambda x: x.lower(), answer))
    while user_answer.lower() not in answer:
        print('Не верный ответ.')
        if attempt == number_of_attempts:
            print('Количество попыток закончено.')
            print(f'Правильные ответы: {', '.join(answer)}')
            return 0
        attempt += 1
        user_answer = input('Введите свой вариант: ')
    print('Ответ верный!!!')
    print(f'Вы угадали с {attempt} попытки')
    story_log(description, attempt)
    return attempt


def print_story_log():
    print('\n---История ответов---')
    for key, value in _attempts_story.items():
        print(f'Загадка: {key}\nОтгадана с {value} попытки\n----------')


def read_puzzle(puz_dict: dict[str:list[str]], amount: int):
    puzzle_amount = amount if amount <= len(puz_dict) else len(puz_dict)
    for _ in range(puzzle_amount):
        question = choice(list(puz_dict))
        answer = puz_dict.pop(question)
        puzzle(question, answer, puzzle_amount)


if __name__ == '__main__':
    puzzle_dict = {'Загадка 1': ['aaa', 'bbb', 'ccc'],
                   'Загадка 2': ['ddd', 'eee', 'fff'],
                   'Загадка 3': ['ggg', 'hhh', 'iii']}

    read_puzzle(puzzle_dict, 2)
    print_story_log()