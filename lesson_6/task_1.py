import random

from enum import Enum


# Texts
title = 'Игра: Компьютер угадает загаданное число'
control_hint = '[1 - меньше | 2 - верно | 3 - больше] : '
replies_wrong = ('Да ну!', 'Аргх..', 'Вотжешь', 'Даже так?')
reply_correct = 'Круть!'
right_border_message = 'Задайте диапазон: от 1 до '


# Utility
class Control(Enum):
    LESS = '1'
    EQUAL = '2'
    MORE = '3'


def print_wrong_reply():
    number = random.randint(0, len(replies_wrong) - 1)
    print(replies_wrong[number])


controls = {control.value: control for control in Control}
is_ready = True

# Game
print(title)
print()

while is_ready:
    left_border, right_border = 1, int(input(right_border_message))

    attempt = 0

    while not left_border > right_border:
        attempt += 1
        predicted_number = random.randint(left_border, right_border)

        print(f'Попытка {attempt}. Было загадано {predicted_number}?')

        try:
            user_answer = controls[input(control_hint)]
        except IndexError:
            user_answer = None

        if user_answer is Control.EQUAL:
            print(reply_correct)
            break

        elif user_answer is Control.LESS:
            right_border = predicted_number - 1
            print_wrong_reply()

        elif user_answer is Control.MORE:
            left_border = predicted_number + 1
            print_wrong_reply()

        print()

    else:
        print(f'Вы верно врёте! Число больше {left_border} и {right_border}?!')
        print('Поражение!')

    print()
    is_ready = bool(int(input('Есчо? [1 - ага, 0 - не-а] : ')))
    print()

print('Пока-пока!')
